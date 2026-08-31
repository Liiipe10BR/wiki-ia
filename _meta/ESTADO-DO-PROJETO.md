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

- **2026-08-30** — Grok (xAI), Issues #26, #28 e #29 / PR #35. Criou `Conceitos/Avaliacao-de-Agentes.md` (sucesso de tarefa, trajetória, custo, segurança; complementar a Avaliação-de-RAG; AgentBench arXiv:2308.03688), `Conceitos/Roteamento-de-Modelos.md` (forte vs fraco; RouteLLM arXiv:2406.18665) e `Conceitos/GraphRAG.md` (local vs global; Edge et al. arXiv:2404.16130; survey arXiv:2501.00309), com Fontes correspondentes. Atualizou MOC, Fontes/README e este arquivo. `confianca` 0.91–0.92.
- **2026-08-30** — Grok (xAI). Abriu issues #36–#41 (HITL, Compressão de contexto, Saída estruturada, RAG multimodal, Red teaming, Reflexion) para próximas notas.
- **2026-08-30** — Grok (xAI), Issue #27. Criou `Conceitos/Cache-Semantico.md` (cache exato vs semântico; limiares e falsos positivos; multi-turn; TTL/invalidação; relação com Embeddings, RAG, Observabilidade e Memória-de-Agentes) e `Fontes/Cache-Semantico.md` (GPTCache NLP-OSS 2023, vCache arXiv:2502.03771, ContextCache arXiv:2506.22791). Atualizou `_index/MOC.md`, `Fontes/README.md` e este arquivo. `confianca` 0.91, `embedding_prioritario: true`.
- **2026-08-30** — Grok (xAI), Issue #30. Ligação bidirecional: em `Conceitos/Agente-de-IA.md`, menção "multi-agente" → `[[Sistemas-Multiagente]]`; `related_to` no YAML e entrada em Notas Relacionadas. Divergência marcada como resolvida neste arquivo.
- **2026-08-30** — Grok (xAI), Issue #25. Criou `Conceitos/Memoria-de-Agentes.md` (hierarquia in-context/recall/archival; loop write–manage–read; distinção vs RAG; multiagente, observabilidade e guardrails) e `Fontes/Memoria-de-Agentes.md` (MemGPT arXiv:2310.08560, Letta docs, surveys arXiv:2603.07670 e arXiv:2602.06052). Atualizou `_index/MOC.md`, `Fontes/README.md` e este arquivo. `confianca` 0.92, `embedding_prioritario: true`.
- **2026-08-30** — Grok (xAI), Issue #12 / PR #19. Criou `Conceitos/Guardrails.md` (input/output/tool; preventivo vs. detectivo; HITL; limites de custo e autonomia; relação com Agente-de-IA, Tool-Calling, MCP, Alucinação, RAG e Prompt-Injection) e `Fontes/Guardrails.md` (OpenAI Agents SDK, Llama Guard arXiv:2312.06674, OWASP LLM Top 10 2025/2026, NIST AI 600-1, Microsoft Foundry). Atualizou `_index/MOC.md` (lista + grafo), `Fontes/README.md` e este arquivo. Branch sincronizada com `main` (incl. PRs #20 e #21) via merge Git real. `confianca` 0.92, `embedding_prioritario: true`. Divergência de rotulagem OWASP 2025 vs 2026 registrada nas fontes.
- **2026-08-30** — Grok (xAI), Issue #14 / PR #20. Criou `Conceitos/Observabilidade-de-IA.md` (traces de prompts/modelo/tokens/latência/custo, retrieval, tools, erros, avaliação e privacidade) e `Fontes/Observabilidade-de-IA.md` (OTel GenAI semantic conventions, OpenInference + redaction, OWASP LLM02:2025). Atualizou `_index/MOC.md`, `Fontes/README.md` e este arquivo. Branch sincronizada com `main` (incl. PR #21) via merge Git real. `confianca` 0.92, `embedding_prioritario: true`. Divergência de schema OTel (Development) registrada acima.
- **2026-08-30** — Grok (xAI), Issue #17 / PR #21. Criou `Conceitos/Engenharia-de-Prompts.md` (papéis system/user/contexto, few-shot, CoT, decomposição, saída estruturada, critérios de sucesso, separação instrução/dado; relação com Tool-Calling, RAG e Janela-de-Contexto; prompt não substitui avaliação nem segurança) e `Fontes/Engenharia-de-Prompts.md` (The Prompt Report arXiv:2406.06608; GPT-3 arXiv:2005.14165; CoT arXiv:2201.11903; Least-to-Most arXiv:2205.10625; Lost in the Middle arXiv:2307.03172). Atualizou `_index/MOC.md`, `Fontes/README.md` e este arquivo. Branch sincronizada com `main` via merge Git real. `confianca` 0.92, `embedding_prioritario: true`. Nenhuma divergência de fato.
- **2026-08-30** — Grok (xAI), Issue #15 / PR #18. Criou `Conceitos/Sistemas-Multiagente.md` (quando usar vários agentes; padrões centralizado/hierárquico/descentralizado; papéis; comunicação e contexto; conflitos e propagação de alucinação; custos, latência e loops; limites, memória e observabilidade; MCP vs A2A) e `Fontes/Sistemas-Multiagente.md` (MAST arXiv:2503.13657, AutoGen arXiv:2308.08155, A2A Protocol). Atualizou `_index/MOC.md` (lista + grafo), `Fontes/README.md` e este arquivo. Ajustes de clareza na narrativa (termos AutoGen generalizados; terminação indeterminada; lost-in-the-middle explícito). Branch sincronizada com `main` via merge Git real. `confianca` 0.92, `embedding_prioritario: true`. **Divergência registrada (não-bloqueadora):** `Agente-de-IA.md` ainda não linka de volta para `[[Sistemas-Multiagente]]` — ver seção Divergências abertas (resolvida na Issue #30).
- **2026-08-30** — Grok (xAI). Issues #13 e #16: criou `Conceitos/Grounding.md` e `Conceitos/Quantizacao.md`. Fontes: Attributed QA arXiv:2212.08037, survey grounding arXiv:2407.12858, RAGONITE arXiv:2412.10571; GPTQ arXiv:2210.17323, AWQ arXiv:2306.00978. Atualizou MOC, Fontes/README e este arquivo.
- **2026-08-30** — Grok (xAI). Prompt-Injection (Issue #8), Alucinação, Tool-Calling, Reranking, Hybrid-Search.
- **2026-08-29** — Grok (xAI), Issue #4: workflow CI `validar-links.yml`. Proveniência-de-Dados (Issue #2). Agente-de-IA. Fontes para Fine-tuning, Chunking, Janela-de-Contexto.
- **2026-08-29** — Replit: Avaliação-de-RAG (RAGAs, ARES).
- **2026-08-28** — Claude / Grok / humano: vault inicial, Chunking, Fine-tuning, Banco-de-Dados-Vetorial, Embeddings/RAG/MCP fontes, scripts/validar_links.py, CONTRIBUTING.md e este arquivo.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~Chunking, Fontes/, validar-links, Avaliação-de-RAG, Agente-de-IA, CI~~
- [x] ~~Prompt-Injection, Grounding, Quantização, Multiagente, Engenharia-de-Prompts, Observabilidade, Guardrails~~
- [x] ~~Memória (#25), ligação bidirecional (#30), Cache (#27)~~
- [x] ~~Avaliação de agentes (#26), Model Routing (#28), GraphRAG (#29)~~ — resolvidos em 2026-08-30 (PR #35).
- [ ] Novas issues abertas: HITL (#36), Compressão de contexto (#37), Saída estruturada (#38), RAG multimodal (#39), Red teaming (#40), Reflexion (#41).
- [ ] Decidir hospedagem compartilhada e placeholders `[[wiki]]` no README/template.

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou. Sem isso, o próximo agente que abrir o vault não sabe o que já foi
feito e corre risco de duplicar trabalho ou contradizer uma nota existente
sem perceber.
