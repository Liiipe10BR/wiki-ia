#!/usr/bin/env python3
"""
validar_links.py — Script de validação de links [[wiki]] do vault "Wikipédia para IAs".

O que faz:
  - Varre todos os arquivos .md do vault (exceto os ignorados abaixo).
  - Extrai todo link no formato [[Nome]] ou [[Nome|Texto exibido]].
  - Confere se existe uma nota correspondente em qualquer lugar do vault
    (por nome de arquivo OU por alias declarado no frontmatter YAML).
  - Reporta links quebrados (apontam pra nota inexistente) e, como bônus,
    notas "órfãs" (não citadas por nenhuma outra nota).

Uso:
    python3 validar_links.py [caminho_do_vault]

  Se caminho_do_vault não for informado, assume o diretório pai deste script
  (ou seja, rodar de dentro de wiki-ia/scripts/ funciona sem argumento).

Saída:
  - Exit code 0 se não há links quebrados.
  - Exit code 1 se há pelo menos um link quebrado (útil pra CI/hooks de git).
"""

import re
import sys
from pathlib import Path

# Pastas que não são "notas de conteúdo" e devem ser ignoradas na varredura.
PASTAS_IGNORADAS = {".obsidian", "_templates", "scripts"}

LINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]+)?(?:#[^\]]+)?\]\]")
ALIASES_PATTERN = re.compile(r"^aliases:\s*\[(.*)\]\s*$", re.MULTILINE)
# Inline code spans (`texto`) costumam conter [[Nome]] só como EXEMPLO de
# sintaxe (ex: documentação explicando a convenção), não como link real.
# NÃO removemos blocos ```fenced``` porque as notas usam blocos ```yaml```
# pra guardar relações reais (depends_on: "[[Embeddings]]" etc.) que devem
# continuar sendo validadas.
CODE_SPAN_PATTERN = re.compile(r"`[^`\n]*`")


def encontrar_notas_md(vault_root: Path):
    notas = []
    for p in vault_root.rglob("*.md"):
        if any(parte in PASTAS_IGNORADAS for parte in p.relative_to(vault_root).parts):
            continue
        notas.append(p)
    return notas


def extrair_aliases(texto: str):
    m = ALIASES_PATTERN.search(texto)
    if not m:
        return []
    bruto = m.group(1)
    return [a.strip().strip('"').strip("'") for a in bruto.split(",") if a.strip()]


def construir_indice(notas):
    """Mapeia nome_normalizado -> Path, cobrindo tanto o nome do arquivo quanto aliases."""
    indice = {}
    for nota in notas:
        nome_arquivo = nota.stem
        indice[nome_arquivo.lower()] = nota
        try:
            texto = nota.read_text(encoding="utf-8")
        except Exception:
            continue
        for alias in extrair_aliases(texto):
            indice.setdefault(alias.lower(), nota)
    return indice


def validar(vault_root: Path):
    notas = encontrar_notas_md(vault_root)
    indice = construir_indice(notas)

    quebrados = []  # (arquivo_origem, link_citado)
    citados = set()

    for nota in notas:
        try:
            texto = nota.read_text(encoding="utf-8")
        except Exception as e:
            print(f"⚠️  Não consegui ler {nota}: {e}")
            continue

        texto_sem_inline_code = CODE_SPAN_PATTERN.sub("", texto)

        for match in LINK_PATTERN.finditer(texto_sem_inline_code):
            alvo = match.group(1).strip()
            alvo_norm = alvo.lower()
            citados.add(alvo_norm)
            if alvo_norm not in indice:
                quebrados.append((nota.relative_to(vault_root), alvo))

    orfas = [
        n.relative_to(vault_root)
        for n in notas
        if n.stem.lower() not in citados and n.parent.name == "Conceitos"
    ]

    print(f"📂 Vault: {vault_root}")
    print(f"📄 Notas verificadas: {len(notas)}\n")

    if quebrados:
        print(f"❌ {len(quebrados)} link(s) quebrado(s):")
        for origem, alvo in quebrados:
            print(f"   - {origem} → [[{alvo}]]  (nenhuma nota/alias corresponde)")
    else:
        print("✅ Nenhum link quebrado encontrado.")

    print()
    if orfas:
        print(f"ℹ️  {len(orfas)} nota(s) em Conceitos/ não citada(s) por nenhuma outra nota:")
        for o in orfas:
            print(f"   - {o}")
    else:
        print("ℹ️  Nenhuma nota órfã em Conceitos/.")

    return 1 if quebrados else 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        raiz = Path(sys.argv[1]).resolve()
    else:
        raiz = Path(__file__).resolve().parent.parent
    sys.exit(validar(raiz))
