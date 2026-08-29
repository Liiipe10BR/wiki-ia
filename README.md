# 🧠 Wikipédia para IAs — Projeto Pessoal

Uma base de conhecimento em Obsidian pensada para **dois leitores ao mesmo tempo**:
humanos (que leem prosa) e agentes de IA (que fazem RAG / embeddings e precisam de fatos atômicos, não de parágrafos bonitos).

## Por que isso existe

Wikipédia comum otimiza para leitura fluida. Isso é ótimo pra humano e péssimo pra
um agente que precisa extrair "X depende de Y" ou "regra A tem exceção B" sem
precisar "interpretar" texto solto. Cada nota aqui tem duas camadas:

1. **Camada Humana** — narrativa, contexto, links `[[wiki]]`, tom livre.
2. **Camada Máquina** — bloco YAML com relações estruturadas (`is_a`, `depends_on`,
   `conflicts_with`) e regras práticas (`rules_of_thumb`) com exceções explícitas.

## Estrutura de pastas

```
wiki-ia/
├── README.md              ← este arquivo
├── CONTRIBUTING.md         ← protocolo pra humanos E IAs contribuírem
├── _meta/
│   └── ESTADO-DO-PROJETO.md   ← "memória" do vault — LEIA PRIMEIRO se você é uma IA
├── _templates/
│   └── Template-Conceito.md   ← template mestre, copie pra criar nota nova
├── _index/
│   └── MOC.md              ← Map of Content, índice de tudo
├── Conceitos/
│   ├── RAG.md
│   ├── Model-Context-Protocol.md
│   ├── Embeddings.md
│   ├── Fine-tuning.md
│   ├── Banco-de-Dados-Vetorial.md
│   ├── Chunking.md
│   ├── Janela-de-Contexto.md
│   ├── Agente-de-IA.md
│   └── Avaliacao-de-RAG.md
├── Fontes/
│   └── README.md            ← protocolo de rastreamento de fontes reais
└── scripts/
    └── validar_links.py     ← checa links quebrados no vault (sintaxe wiki-link)
```

## Projeto aberto a contribuição de IAs

Este vault é escrito em conjunto por humanos e agentes de IA. Se você é uma
IA lendo isto: veja `_meta/ESTADO-DO-PROJETO.md` primeiro, depois
`CONTRIBUTING.md` pro protocolo completo.

## Convenções do frontmatter

| Campo | O que é | Exemplo |
|---|---|---|
| `tags` | classificação hierárquica | `wiki/agente`, `tipo/conceito` |
| `aliases` | nomes alternativos pra busca/link | `["RAG", "Retrieval Augmented Generation"]` |
| `data_criacao` | quando a nota nasceu | `2026-08-28` |
| `ultima_verificacao` | quando os fatos foram checados por último — **evita que a IA confie em algo defasado** | `2026-08-28` |
| `confianca` | 0 a 1, quão sólida é a informação | `0.92` |
| `embedding_prioritario` | se `true`, sinaliza pro pipeline de indexação que essa nota deve ter peso maior | `true` |

## Regras de uso (pra você, humano)

- **Nunca deixe a camada YAML desincronizada da narrativa.** Se mudar uma, revise a outra.
- Toda regra em `rules_of_thumb` que tiver exceção, escreva a exceção do lado —
  um agente sem contexto vai aplicar a regra ao pé da letra.
- `confianca` baixa (< 0.6) deveria ser tratado pelo pipeline como "não citar sem
  avisar que é incerto".
- Links `[[Conceito]]` entre notas são o que dá ao agente o grafo de relações —
  use bastante, mesmo na camada YAML (`depends_on: "[[Embeddings]]"`).

## Próximos passos sugeridos

- [ ] Definir o pipeline de indexação (o que lê o frontmatter e como)
- [ ] Criar mais notas em `Conceitos/`
- [x] ~~Adicionar uma pasta `Fontes/` se quiser rastrear de onde cada fato veio~~ — criada em 2026-08-28
- [x] ~~Script de validação: checar se todo `depends_on`/`conflicts_with` aponta pra uma nota que existe~~ — `scripts/validar_links.py`, criado em 2026-08-28
