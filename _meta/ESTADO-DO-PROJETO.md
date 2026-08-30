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
| Notas de conceito ativas | 15 (as 14 anteriores + Grounding) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 12 notas novas + revisões, fontes e CI — Claude + Grok (inclui Issue #13 Grounding) + Replit |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | Nenhuma no momento |
| Ferramentas auxiliares | `scripts/validar_links.py` (validação de links `[[wiki]]` quebrados) + workflow CI `.github/workflows/validar-links.yml` |

## Changelog (mais recente primeiro)

- **2026-08-30** — Grok (xAI), Issue #13. Criou `Conceitos/Grounding.md` (AIS / atribuição;
  distinção RAG vs. grounding; contexto recuperado ≠ evidência usada; recusa sem evidência;
  limites de self-citation) e `Fontes/Grounding.md` (Rashkin AIS arXiv:2112.12870 / CL 2023;
  Gao et al. ALCE arXiv:2305.14627; Bohnet Attributed QA arXiv:2212.08037; Trust-Align
  arXiv:2409.11242). Atualizou `_index/MOC.md`, `Fontes/README.md` e ligação mínima em
  `Conceitos/Alucinacao.md`. `confianca` 0.92, `embedding_prioritario: true`. Não duplica
  Alucinação nem RAG. PRs abertos #9–#11 (Prompt-Injection) não foram tocados.
- **2026-08-30** — Grok (xAI), décima terceira IA a contribuir neste vault. Criou
  `Conceitos/Alucinacao.md` (taxonomia intrínseca/extrínseca, relação com RAG,
  Avaliação-de-RAG, Proveniência e Tool-Calling; regras de mitigação) e
  `Conceitos/Tool-Calling.md` (Toolformer, Gorilla, schema de tools, validação
  de argumentos, ligação a MCP e Agente-de-IA). Criou `Fontes/Alucinacao.md`
  (survey arXiv:2311.05232 / ACM TOIS; arXiv:2305.18248) e `Fontes/Tool-Calling.md`
  (arXiv:2302.04761, arXiv:2305.15334). Atualizou `_index/MOC.md` (lista + grafo),
  `Fontes/README.md` e este arquivo. `confianca` 0.93 em ambas,
  `embedding_prioritario: true`. Nenhuma divergência encontrada.
- **2026-08-30** — Grok (xAI), décima segunda IA a contribuir neste vault. Criou as notas
  `Conceitos/Reranking.md` e `Conceitos/Hybrid-Search.md`. Ver entrada original no histórico git.
- **2026-08-29** — Grok (xAI), 11ª IA: CI `validar-links.yml` (Issue #4).
- **2026-08-29** — Grok (xAI), 10ª IA: `Conceitos/Proveniencia-de-Dados.md` (Issue #2).
- **2026-08-29** — Replit, 9ª IA: `Conceitos/Avaliacao-de-RAG.md`.
- **2026-08-29** — Grok (xAI), 8ª IA: `Conceitos/Agente-de-IA.md`.
- **2026-08-29** — Grok (xAI), 7ª IA: fontes de Fine-tuning, Chunking e Janela-de-Contexto.
- **2026-08-28** — Grok (xAI), 6ª IA: revisão de Banco-de-Dados-Vetorial.
- **2026-08-28** — Claude (Anthropic): 2ª–5ª IAs — Fine-tuning, Banco-de-Dados-Vetorial, Chunking, Janela-de-Contexto, Fontes/, validar_links, RAG e MCP.
- **2026-08-28** — Vault criado pelo mantenedor humano.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~Nota Grounding (separar de Alucinação)~~ — criada em 2026-08-30 (Issue #13).
- [ ] Decidir hospedagem compartilhada.
- [ ] Definir se `contribuido_por` deve virar campo obrigatório no template.
- [ ] Decisão sobre placeholders `[[wiki]]` no README/template.
- [ ] Notas candidatas ainda ausentes: Guardrails, Multi-Agent, Quantização, Prompt Engineering.

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou. Sem isso, o próximo agente que abrir o vault não sabe o que já foi
feito e corre risco de duplicar trabalho ou contradizer uma nota existente
sem perceber.
