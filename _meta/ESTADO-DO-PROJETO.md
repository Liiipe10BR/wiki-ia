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
| Notas de conceito ativas | 14 (RAG, Embeddings, Model-Context-Protocol, Fine-tuning, Banco-de-Dados-Vetorial, Chunking, Janela-de-Contexto, Agente-de-IA, Avaliação-de-RAG, Proveniência-de-Dados, Reranking, Hybrid-Search, Alucinação, Tool-Calling) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 11 notas novas + revisões, fontes e CI — Claude (várias sessões) + Grok (xAI, 6ª–8ª, 10ª–13ª) + Replit (9ª) |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | Nenhuma no momento |
| Ferramentas auxiliares | `scripts/validar_links.py` + workflow CI `.github/workflows/validar-links.yml` |

## Changelog (mais recente primeiro)

- **2026-08-30** — Grok (xAI), décima terceira IA a contribuir neste vault. Criou
  `Conceitos/Alucinacao.md` (taxonomia intrínseca/extrínseca, relação com RAG,
  Avaliação-de-RAG, Proveniência e Tool-Calling; regras de mitigação) e
  `Conceitos/Tool-Calling.md` (Toolformer, Gorilla, schema de tools, validação
  de argumentos, ligação a MCP e Agente-de-IA). Criou `Fontes/Alucinacao.md`
  (survey arXiv:2311.05232 / ACM TOIS; arXiv:2305.18248) e `Fontes/Tool-Calling.md`
  (arXiv:2302.04761, arXiv:2305.15334). Atualizou MOC, Fontes/README e este arquivo.
  `confianca` 0.93 em ambas, `embedding_prioritario: true`. Nenhuma divergência.
- **2026-08-30** — Grok (xAI), décima segunda IA a contribuir neste vault. Criou as notas
  `Conceitos/Reranking.md` e `Conceitos/Hybrid-Search.md` com fontes e atualização do MOC.
  `confianca` 0.93 e 0.92. Nenhuma divergência encontrada.
- **2026-08-29** — Grok (xAI), décima-primeira IA a contribuir neste vault. Implementou a
  Issue #4: criou `.github/workflows/validar-links.yml`. Atualizou este arquivo.
- **2026-08-29** — Grok (xAI), décima IA a contribuir neste vault. Criou a nota
  `Conceitos/Proveniencia-de-Dados.md` e fontes (W3C PROV, surveys). Atualizou MOC.
- **2026-08-29** — Replit, nona IA a contribuir neste vault. Criou `Conceitos/Avaliacao-de-RAG.md`
  e fontes (RAGAs, ARES).
- **2026-08-29** — Grok (xAI), oitava IA. Criou `Conceitos/Agente-de-IA.md` (ReAct, Toolformer, MCP).
- **2026-08-29** — Grok (xAI), sétima IA. Completou Fontes/ para Fine-tuning, Chunking e Janela-de-Contexto.
- **2026-08-28** — Grok (xAI), sexta IA. Expandiu Banco-de-Dados-Vetorial e criou fontes.
- **2026-08-28** — Claude (Anthropic), quinta IA. Fontes de Embeddings; validar_links.py.
- **2026-08-28** — Claude (Anthropic), quarta IA. Fontes de RAG e correção MCP.
- **2026-08-28** — Claude (Anthropic), terceira IA. Janela-de-Contexto, pasta Fontes/, validar_links.py.
- **2026-08-28** — Claude (Anthropic), segunda IA. Chunking.md.
- **2026-08-28** — Claude (Anthropic), primeira IA. Fine-tuning, Banco-de-Dados-Vetorial, CONTRIBUTING, ESTADO.
- **2026-08-28** — Vault criado pelo mantenedor humano (estrutura base + RAG, Embeddings, MCP).

## Próximos passos sugeridos (em aberto pra quem pegar)

- [ ] Definir se `contribuido_por` deve virar campo obrigatório no template
  pra toda nota nova, não só nas escritas por IA.
- [ ] Rodar `scripts/validar_links.py` de novo depois de decidir se os
  placeholders `[[wiki]]`/`[[Conceito]]` no README e no template devem ser
  reescritos pra não aparecer como falso-positivo.
- [ ] Notas candidatas ainda ausentes: Guardrails, Multi-Agent, Quantização,
  Prompt Engineering, Grounding (se quiser separar de Alucinação).

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou. Sem isso, o próximo agente que abrir o vault não sabe o que já foi
feito e corre risco de duplicar trabalho ou contradizer uma nota existente
sem perceber.
