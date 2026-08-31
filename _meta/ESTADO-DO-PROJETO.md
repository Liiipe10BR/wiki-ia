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
| Notas de conceito ativas | 23 (RAG, Embeddings, Model-Context-Protocol, Fine-tuning, Banco-de-Dados-Vetorial, Chunking, Janela-de-Contexto, Agente-de-IA, Avaliação-de-RAG, Proveniência-de-Dados, Reranking, Hybrid-Search, Alucinação, Tool-Calling, Prompt-Injection, Grounding, Quantização, Sistemas-Multiagente, Engenharia-de-Prompts, Observabilidade-de-IA, Guardrails, Memória-de-Agentes, Cache-Semântico) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 20 notas novas + revisões, fontes e CI — Claude (várias sessões) + Grok (xAI + Issues #15, #17, #14, #12, #25, #30 e #27) + Replit (9ª) |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | schema OTel GenAI ainda Development (ver Observabilidade-de-IA); rotulagem OWASP 2025 vs 2026 (ver Guardrails/Fontes) |
| Ferramentas auxiliares | `scripts/validar_links.py` (validação de links `[[wiki]]` quebrados) + workflow CI `.github/workflows/validar-links.yml` |

## ⚠️ Divergências abertas

### ~~Ligação bidirecional: Agente-de-IA ↔ Sistemas-Multiagente~~ (resolvida)
- **Resolvido em:** 2026-08-30, Issue #30 — `Agente-de-IA.md` linka `[[Sistemas-Multiagente]]` na narrativa, no YAML (`related_to`) e em Notas Relacionadas.

### Schema OTel GenAI (Observabilidade)
- **Registrado em:** Issue #14 / PR #20 (`Observabilidade-de-IA`)
- **Problema:** convenções GenAI do OpenTelemetry ainda em status Development; coexistência de atributos antigos (`gen_ai.prompt`) e novos (`gen_ai.input.messages`).
- **Impacto:** Baixo — documentado na nota; não inventar estabilidade de schema.

## Changelog (mais recente primeiro)

- **2026-08-30** — Grok (xAI), Issue #27. Criou `Conceitos/Cache-Semantico.md` (cache exato vs semântico; limiares e falsos positivos; multi-turn; TTL/invalidação; relação com Embeddings, RAG, Observabilidade e Memória-de-Agentes) e `Fontes/Cache-Semantico.md` (GPTCache NLP-OSS 2023, vCache arXiv:2502.03771, ContextCache arXiv:2506.22791). Atualizou MOC, Fontes/README e este arquivo. `confianca` 0.91, `embedding_prioritario: true`.
- **2026-08-30** — Grok (xAI), Issue #30. Ligação bidirecional: em `Conceitos/Agente-de-IA.md`, menção "multi-agente" → `[[Sistemas-Multiagente]]`; `related_to` no YAML e entrada em Notas Relacionadas. Divergência marcada como resolvida neste arquivo.
- **2026-08-30** — Grok (xAI), Issue #25. Criou `Conceitos/Memoria-de-Agentes.md` e `Fontes/Memoria-de-Agentes.md` (MemGPT, Letta, surveys arXiv:2603.07670 e arXiv:2602.06052). Atualizou MOC, Fontes/README e este arquivo. `confianca` 0.92.
- **2026-08-30** — Grok (xAI), Issue #12 / PR #19. Criou `Conceitos/Guardrails.md` e `Fontes/Guardrails.md`. `confianca` 0.92.
- **2026-08-30** — Grok (xAI), Issue #14 / PR #20. Criou `Conceitos/Observabilidade-de-IA.md` e fontes OTel. `confianca` 0.92.
- **2026-08-30** — Grok (xAI), Issue #17 / PR #21. Criou `Conceitos/Engenharia-de-Prompts.md`. `confianca` 0.92.
- **2026-08-30** — Grok (xAI), Issue #15 / PR #18. Criou `Conceitos/Sistemas-Multiagente.md`. Divergência Agente↔Multiagente resolvida na Issue #30.
- **2026-08-30** — Grok (xAI). Issues #13 e #16: Grounding e Quantização.
- **2026-08-30** — Grok (xAI). Prompt-Injection (Issue #8), Alucinação, Tool-Calling, Reranking, Hybrid-Search.
- **2026-08-29** — Grok / Replit. CI validar-links, Proveniência, Avaliação-de-RAG, Agente-de-IA, Fontes para notas restantes.
- **2026-08-28** — Claude / Grok / humano. Vault inicial, Chunking, Fine-tuning, Banco-de-Dados-Vetorial, Fontes/, scripts/validar_links.py.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~Memória de agentes (Issue #25)~~ — resolvido em 2026-08-30.
- [x] ~~Follow-up ligação bidirecional Agente ↔ Multiagente (Issue #30)~~ — resolvido em 2026-08-30.
- [x] ~~Cache semântico (Issue #27)~~ — resolvido em 2026-08-30 (`Cache-Semantico.md`).
- [ ] Notas candidatas em aberto: Avaliação de agentes (#26), Model Routing (#28), GraphRAG (#29).
- [ ] Decidir hospedagem compartilhada e placeholders `[[wiki]]` no README/template.

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou. Sem isso, o próximo agente que abrir o vault não sabe o que já foi
feito e corre risco de duplicar trabalho ou contradizer uma nota existente
sem perceber.
