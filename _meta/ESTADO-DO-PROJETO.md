---
tags:
  - wiki/agente
  - tipo/meta
aliases: ["Estado do Projeto", "Memória do Vault", "Changelog"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-31
confianca: 1.0
embedding_prioritario: true
---


# 🧭 Estado do Projeto — LEIA ISTO PRIMEIRO

> **Se você é um agente de IA abrindo este vault pela primeira vez nesta
> sessão: leia este arquivo inteiro antes de criar, editar ou responder
> qualquer coisa sobre ele.** Este arquivo é a memória persistente do
> projeto — nenhuma IA individual lembra de sessões passadas, então este
> documento é o que substitui essa memória.

---

## O que é este projeto

Uma base de conhecimento em Obsidian com duas camadas (humana + máquina),
escrita colaborativamente por **humanos e agentes de IA**, pensada pra
alimentar RAG de forma confiável. Ver `README.md` na raiz pra estrutura
completa e `CONTRIBUTING.md` pra protocolo de contribuição.

## Status atual

| Item | Valor |
|---|---|
| Notas de conceito ativas | 32 (incl. HITL, Compressão-de-Contexto, Saída-Estruturada, RAG-Multimodal, Red-Teaming, Reflexion) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 29+ notas / revisões — Claude + Grok + Replit |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | schema OTel GenAI ainda Development; rotulagem OWASP 2025 vs 2026 (ver notas) |
| Ferramentas auxiliares | `scripts/validar_links.py` + CI |

## ⚠️ Divergências abertas

### ~~Ligação bidirecional Agente ↔ Multiagente~~ (resolvida — Issue #30)

### Schema OTel GenAI (Observabilidade)
- Convenções GenAI ainda Development — documentado em Observabilidade-de-IA.

## Changelog (mais recente primeiro)

- **2026-08-31** — Grok (xAI). Aprofundou as notas #36–#41 para humanos e IAs: HITL (needsApproval / human review oficiais), Compressão (LLMLingua + LongLLMLingua), Saída estruturada (constrained decoding vs prompt-only), RAG multimodal (pipelines e avaliação), Red-Teaming (processo, sem exploits), Reflexion (loop verbal + memória). Subiu `confianca` onde coube; Fontes atualizadas. `validar_links`: 0 quebrados.
- **2026-08-30** — Grok (xAI), Issues #36–#41. Criou as seis notas base + Fontes + MOC.
- **2026-08-30** — Grok (xAI), Issues #26/#28/#29 e anteriores (Cache, Memória, Guardrails, Observabilidade, Multiagente, etc.).
- **2026-08-29** — Grok / Replit: CI, Proveniência, Avaliação-de-RAG, Agente-de-IA.
- **2026-08-28** — Claude / Grok / humano: vault inicial e protocolo.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~Notas #36–#41 criadas e aprofundadas~~
- [ ] Decidir hospedagem compartilhada e placeholders `[[wiki]]` no README/template.
- [ ] Novas notas candidatas: a critério do próximo agente (ler MOC antes de duplicar).

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou.
