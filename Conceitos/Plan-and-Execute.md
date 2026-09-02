---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Plan-and-Execute", "Plan and Execute", "Plan-and-Solve", "Planejar e executar"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.91
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Plan-and-Execute / Plan-and-Solve"
---

# 📋 Plan-and-Execute

> **Resumo para Humanos:**
> Separar **planejar** (lista de subpassos) de **executar** (tools/LLM por passo),
> com re-planejamento quando necessário — alternativa ao loop [[ReAct]] passo a
> passo.

---

## 📖 1. Contexto Humano (Narrativa)

No **ReAct**, o modelo decide a próxima ação a cada observação. Em tarefas
longas isso gera muitas chamadas ao LLM grande e planos míopes.
**Plan-and-Execute** formaliza:

1. **Planner** — gera um plano multi-step
2. **Executor** — cumpre cada passo (tools ou modelo menor)
3. **Re-planner** (opcional) — ajusta o plano com o que já aconteceu

A ideia de *planejar antes de resolver* aparece em **Plan-and-Solve Prompting**
(Wang et al., arXiv:2305.04091) no eixo de prompting zero-shot: dividir a tarefa
em subproblemas reduz erros de “passo faltando” frente a Zero-shot-CoT nos
datasets do paper. Em frameworks de agentes (ex.: padrões documentados em
LangGraph), a mesma separação planner/executor é usada para latência e custo:
o cérebro grande planeja; executores podem ser mais baratos.

### Trade-offs vs ReAct

| | ReAct | Plan-and-Execute |
|--|-------|------------------|
| Flexibilidade | Alta a cada step | Plano pode ficar obsoleto |
| Custo LLM grande | Por ação | Mais no planning / replan |
| Legibilidade | Trace intercalado | Plano explícito |

Não elimina [[Guardrails]] nem [[HITL]] em passos sensíveis. Planos ruins
executados com eficiência só falham mais rápido — avalie com
[[Avaliacao-de-Agentes]].

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Plan-and-Execute — separação de planejamento e execução"
relations:
  - is_a: "Padrão de orquestração de agentes"
  - related_to: "[[ReAct]]"
  - related_to: "[[Tree-of-Thoughts]]"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Sistemas-Multiagente]]"
  - related_to: "[[Avaliacao-de-Agentes]]"
rules_of_thumb:
  - "Regra 1: Replaneje quando observações invalidarem o plano — não execute cegamente."
  - "Regra 2: Marque passos que exigem HITL/guardrail no plano."
  - "Regra 3: Prefira executores baratos para subpassos mecânicos."
  - "Regra 4: Compare custo total com ReAct na sua carga real."
  - "Exceção: Tarefas de 1–2 tools raramente precisam de planner explícito."
```

---

## 🔗 3. Notas Relacionadas
- [[ReAct]]
- [[Tree-of-Thoughts]]
- [[Agente-de-IA]]
- [[Tool-Calling]]
- [[Sistemas-Multiagente]]
- [[Avaliacao-de-Agentes]]

## 📚 4. Fontes
- Ver `Fontes/Plan-and-Execute.md`.
- Wang et al., Plan-and-Solve, arXiv:2305.04091.
