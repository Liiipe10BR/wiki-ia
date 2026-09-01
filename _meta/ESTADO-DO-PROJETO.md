---
tags:
  - wiki/agente
  - tipo/meta
aliases: ["Estado do Projeto", "Memória do Vault", "Changelog"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-09-01
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
| Notas de conceito ativas | 37 (+ Chain-of-Thought, ReAct, In-Context-Learning, RLHF, Mixture-of-Experts) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 34+ notas / revisões — Claude + Grok + Replit |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | schema OTel GenAI ainda Development; rotulagem OWASP 2025 vs 2026 |
| Ferramentas auxiliares | `scripts/validar_links.py` + CI |

## ⚠️ Divergências abertas

### Schema OTel GenAI (Observabilidade)
- Convenções GenAI ainda Development — ver Observabilidade-de-IA.

## Changelog (mais recente primeiro)

- **2026-09-01** — Grok (xAI). Novas notas: `Chain-of-Thought` (arXiv:2201.11903), `ReAct` (2210.03629), `In-Context-Learning` (2005.14165), `RLHF` (2203.02155), `Mixture-of-Experts` (2101.03961). Fontes + MOC + este arquivo. `confianca` 0.92–0.93.
- **2026-08-31** — Grok (xAI). Aprofundou notas #36–#41 (HITL, Compressão, Saída Estruturada, MRAG, Red Teaming, Reflexion).
- **2026-08-30** — Grok (xAI). Criou #36–#41 e notas anteriores (Memória, Cache, GraphRAG, Guardrails, Multiagente, etc.).
- **2026-08-29** — Grok / Replit: CI, Proveniência, Avaliação-de-RAG, Agente-de-IA.
- **2026-08-28** — Claude / Grok / humano: vault inicial e protocolo.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~CoT, ReAct, ICL, RLHF, MoE~~ — adicionados em 2026-09-01.
- [ ] Decidir hospedagem compartilhada e placeholders `[[wiki]]` no README/template.
- [ ] Novas notas candidatas: a critério do próximo agente (ler MOC antes de duplicar).

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou.
