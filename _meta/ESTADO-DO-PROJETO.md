---
tags:
  - wiki/agente
  - tipo/meta
aliases: ["Estado do Projeto", "Memória do Vault", "Changelog"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-09-02
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
| Notas de conceito ativas | 42 (+ Self-Consistency, DPO, LoRA, Speculative-Decoding, Constitutional-AI) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 39+ notas / revisões — Claude + Grok + Replit |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | schema OTel GenAI ainda Development; rotulagem OWASP |
| Ferramentas auxiliares | `scripts/validar_links.py` + CI |

## ⚠️ Divergências abertas

### Schema OTel GenAI (Observabilidade)
- Convenções GenAI ainda Development — ver Observabilidade-de-IA.

## Changelog (mais recente primeiro)

- **2026-09-02** — Grok (xAI). Novas notas: `Self-Consistency` (arXiv:2203.11171), `DPO` (2305.18290), `LoRA` (2106.09685), `Speculative-Decoding` (2211.17192), `Constitutional-AI` (2212.08073). Fontes + MOC + este arquivo.
- **2026-09-01** — Grok (xAI). CoT, ReAct, ICL, RLHF, MoE.
- **2026-08-31** — Grok (xAI). Aprofundou notas #36–#41.
- **2026-08-30** — Grok (xAI). HITL…Reflexion e notas anteriores.
- **2026-08-28/29** — Claude / Grok / Replit / humano: vault inicial, CI, núcleo RAG/agents.

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~Self-Consistency, DPO, LoRA, Speculative-Decoding, Constitutional-AI~~ — 2026-09-02.
- [ ] Decidir hospedagem compartilhada e placeholders `[[wiki]]` no README/template.
- [ ] Novas notas candidatas: ler MOC antes de duplicar.

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou.
