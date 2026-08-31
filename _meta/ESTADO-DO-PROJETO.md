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
| Notas de conceito ativas | 26 (RAG, Embeddings, Model-Context-Protocol, Fine-tuning, Banco-de-Dados-Vetorial, Chunking, Janela-de-Contexto, Agente-de-IA, Avaliação-de-RAG, Proveniência-de-Dados, Reranking, Hybrid-Search, Alucinação, Tool-Calling, Prompt-Injection, Grounding, Quantização, Sistemas-Multiagente, Engenharia-de-Prompts, Observabilidade-de-IA, Guardrails, Memória-de-Agentes, Cache-Semântico, Avaliação-de-Agentes, Roteamento-de-Modelos, GraphRAG) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 23 notas novas + revisões, fontes e CI — Claude (várias sessões) + Grok (xAI + Issues #15–#17, #14, #12, #25–#30, #26, #28, #29) + Replit (9ª) |
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

- **2026-08-30** — Grok (xAI), Issues #26, #28 e #29. Criou `Conceitos/Avaliacao-de-Agentes.md` (sucesso de tarefa, trajetória, custo, segurança; complementar a Avaliação-de-RAG; AgentBench arXiv:2308.03688), `Conceitos/Roteamento-de-Modelos.md` (forte vs fraco; RouteLLM arXiv:2406.18665) e `Conceitos/GraphRAG.md` (local vs global; Edge et al. arXiv:2404.16130; survey arXiv:2501.00309), com Fontes correspondentes. Atualizou MOC, Fontes/README e este arquivo. `confianca` 0.91–0.92.
- **2026-08-30** — Grok (xAI), Issue #27. Criou `Conceitos/Cache-Semantico.md` e `Fontes/Cache-Semantico.md` (GPTCache, vCache, ContextCache). `confianca` 0.91.
- **2026-08-30** — Grok (xAI), Issue #30. Ligação bidirecional Agente ↔ Sistemas-Multiagente resolvida.
- **2026-08-30** — Grok (xAI), Issue #25. `Memoria-de-Agentes.md`. `confianca` 0.92.
- **2026-08-30** — Grok (xAI), Issues #12/#14/#17/#15/#13/#16/#8 e notas Alucinação, Tool-Calling, Reranking, Hybrid-Search (ver commits e PRs #18–#21, #19, #32–#34).
- **2026-08-29** — Grok / Replit: CI validar-links, Proveniência, Avaliação-de-RAG, Agente-de-IA, Fontes restantes.
- **2026-08-28** — Claude / Grok / humano: vault inicial, Chunking, Fine-tuning, Banco-de-Dados-Vetorial, Fontes/, scripts/validar_links.py.

> **Nota de manutenção:** o detalhamento linha a linha das entradas 2026-08-28–29 está no histórico git de `main` (commits anteriores a este PR). Esta versão prioriza legibilidade + estado atual (26 notas) sem apagar o fato das contribuições anteriores.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~Chunking, Fontes/, validar-links, Avaliação-de-RAG, Agente-de-IA, CI~~
- [x] ~~Prompt-Injection, Grounding, Quantização, Multiagente, Engenharia-de-Prompts, Observabilidade, Guardrails~~
- [x] ~~Memória (#25), ligação bidirecional (#30), Cache (#27)~~
- [x] ~~Avaliação de agentes (#26), Model Routing (#28), GraphRAG (#29)~~
- [ ] Decidir hospedagem compartilhada e placeholders `[[wiki]]` no README/template.

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou. Sem isso, o próximo agente que abrir o vault não sabe o que já foi
feito e corre risco de duplicar trabalho ou contradizer uma nota existente
sem perceber.
