---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Human-in-the-Loop", "HITL", "Humano no loop", "Aprovação humana"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.90
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #36 / Human-in-the-Loop em sistemas agentic"
---

# 👤 Human-in-the-Loop (HITL)

> **Resumo para Humanos:**
> Inserir **aprovação, correção ou tomada de controle humana** em pontos
> críticos do pipeline de um [[Agente-de-IA]] — não só “o modelo pede ajuda”
> no texto, mas uma interface real que bloqueia ou libera a ação.

---

## 📖 1. Contexto Humano (Narrativa)

Agentes que chamam tools podem enviar e-mail, mover dinheiro ou apagar dados.
[[Guardrails]] automáticos reduzem risco, mas não cobrem todos os casos de
ambiguidade, responsabilidade legal ou preferência do negócio. **HITL** coloca
um humano *no caminho crítico* (ou ao lado, em amostragem).

Formas comuns:

1. **Pré-aprovação** — tool de alto risco só executa após OK humano
2. **Pós-revisão** — ação executa; humano audita amostra ou exceções
3. **Escalação** — confiança baixa, custo alto ou domínio sensível → fila humana
4. **Correção** — humano edita a saída e o sistema aprende (ou só registra)

Trade-off central: **segurança e accountability** vs. **latência e custo
operacional**. Em produção, HITL sem [[Observabilidade-de-IA]] vira fila cega.
HITL não substitui [[Avaliacao-de-Agentes]]; alimenta dados para ela.

Não confundir com o modelo *escrever* “consulte um especialista” sem haver
canal de escalação. Sem UI, política e SLA, não há loop humano.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Human-in-the-Loop em pipelines de agentes e LLMs"
relations:
  - is_a: "Padrão de controle humano em sistemas semi-autônomos"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[Avaliacao-de-Agentes]]"
  - related_to: "[[Prompt-Injection]]"
rules_of_thumb:
  - "Regra 1: Liste tools/ações que exigem pré-aprovação humana por política (irreversível, financeiro, PII, produção)."
  - "Regra 2: Defina SLA e fallback se o humano não responder (timeout ≠ aprovação implícita)."
  - "Regra 3: Registre quem aprovou, o quê e por quê — sem isso não há auditoria."
  - "Regra 4: Use pós-revisão amostral para volume alto; pré-aprovação para risco alto."
  - "Regra 5: HITL não é desculpa para omitir guardrails automáticos."
  - "Exceção: Ambientes só de pesquisa/demo podem operar sem HITL se não houver efeito no mundo real."
```

---

## 🔗 3. Notas Relacionadas
- [[Guardrails]]
- [[Agente-de-IA]]
- [[Tool-Calling]]
- [[Observabilidade-de-IA]]
- [[Avaliacao-de-Agentes]]
- [[Prompt-Injection]]

## 📚 4. Fontes
- Ver `Fontes/HITL.md`.
- Conceito transversal em frameworks de agents e em [[Guardrails]] (aprovação de ações).
