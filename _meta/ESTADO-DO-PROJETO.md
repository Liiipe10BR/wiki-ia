---
tags:
  - wiki/agente
  - tipo/meta
aliases: ["Estado do Projeto", "Memória do Vault", "Changelog"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-30
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
| Notas de conceito ativas | 32 (26 anteriores + HITL, Compressão-de-Contexto, Saída-Estruturada, RAG-Multimodal, Red-Teaming, Reflexion) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 29 notas novas + revisões — Claude + Grok (incl. #36–#41) + Replit |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | schema OTel GenAI ainda Development (ver Observabilidade-de-IA); rotulagem OWASP 2025 vs 2026 (ver Guardrails/Fontes) |
| Ferramentas auxiliares | `scripts/validar_links.py` + workflow CI `.github/workflows/validar-links.yml` |

## ⚠️ Divergências abertas

### ~~Ligação bidirecional: Agente-de-IA ↔ Sistemas-Multiagente~~ (resolvida)
- **Resolvido em:** 2026-08-30, Issue #30.

### Schema OTel GenAI (Observabilidade)
- **Registrado em:** Issue #14 / PR #20 — convenções GenAI ainda Development.

## Changelog (mais recente primeiro)

- **2026-08-30** — Grok (xAI), Issues #36–#41. Criou `HITL`, `Compressao-de-Contexto` (LLMLingua arXiv:2310.05736), `Saida-Estruturada` (OpenAI Structured Outputs), `RAG-Multimodal` (surveys arXiv:2502.08826, 2504.08748), `Red-Teaming` (processo; OWASP LLM), `Reflexion` (arXiv:2303.11366). Fontes + MOC + este arquivo. `confianca` 0.90–0.92.
- **2026-08-30** — Grok (xAI), Issues #26, #28 e #29 / PR #35. Avaliação-de-Agentes, Roteamento-de-Modelos, GraphRAG.
- **2026-08-30** — Grok (xAI), Issues #27, #30, #25, #12, #14, #17, #15, #13, #16, #8 e notas de Reranking/Hybrid/Alucinação/Tool-Calling.
- **2026-08-29** — Grok / Replit: CI, Proveniência, Avaliação-de-RAG, Agente-de-IA, Fontes restantes.
- **2026-08-28** — Claude / Grok / humano: vault inicial, Chunking, Fine-tuning, Banco-de-Dados-Vetorial, Fontes/, validar_links.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~HITL (#36), Compressão (#37), Saída estruturada (#38), RAG multimodal (#39), Red teaming (#40), Reflexion (#41)~~ — resolvidos em 2026-08-30.
- [ ] Decidir hospedagem compartilhada e placeholders `[[wiki]]` no README/template.

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou.
