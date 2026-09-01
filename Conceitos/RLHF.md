---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["RLHF", "Reinforcement Learning from Human Feedback", "Alinhamento com feedback humano", "InstructGPT"]
data_criacao: 2026-09-01
ultima_verificacao: 2026-09-01
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — nota RLHF (Ouyang et al. / InstructGPT)"
---

# 🎯 RLHF

> **Resumo para Humanos:**
> **Alinhar** o modelo às preferências humanas com feedback: demonstrações +
> rankings → recompensa → fine-tuning por aprendizado por reforço (ou variantes).

---

## 📖 1. Contexto Humano (Narrativa)

Escalar o modelo **não** garante que ele siga a intenção do usuário. Ouyang et
al. (arXiv:2203.02155, InstructGPT) formalizam um caminho prático:

1. **SFT** — fine-tuning supervisionado com demonstrações de comportamento
   desejado
2. **Reward model** — treinado com rankings humanos de saídas
3. **RL** (ex.: PPO) — otimiza a política contra o reward model, com desvio
   controlado do modelo SFT

No paper, um InstructGPT de 1.3B foi preferido a um GPT-3 de 175B em avaliações
humanas na distribuição de prompts do estudo, com ganhos em veracidade e queda
de toxicidade nos eixos medidos — ainda com erros simples restantes.

### O que RLHF **não** é

- Não é [[In-Context-Learning]] (aqui há update de pesos)
- Não substitui [[Guardrails]] em runtime nem [[Red-Teaming]]
- Preferência humana ≠ verdade factual absoluta ([[Alucinacao]] pode persistir)

Variantes posteriores (RLAIF, DPO, etc.) mudam como a preferência entra no
treino; a ideia central permanece: **otimizar para preferência**, não só para
próxima-token no pré-treino.

### Ligação ao vault

- Pós-treino complementa [[Fine-tuning]] supervisionado
- Modelos “instruction-tuned” que você usa em [[Agente-de-IA]] em geral passaram
  por alguma forma de alinhamento
- [[HITL]] em produção é feedback *online*; RLHF clássico é feedback *offline*
  de treino

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "RLHF — alinhamento com feedback humano"
relations:
  - is_a: "Pipeline de pós-treino baseado em preferência humana"
  - related_to: "[[Fine-tuning]]"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[HITL]]"
  - related_to: "[[Red-Teaming]]"
  - related_to: "[[Agente-de-IA]]"
rules_of_thumb:
  - "Regra 1: Separe alinhamento de treino (RLHF/DPO) de controles de runtime (guardrails/HITL)."
  - "Regra 2: Dados de preferência enviesados produzem política enviesada."
  - "Regra 3: Avalie regressões em tarefas úteis após alinhamento — reward hacking existe."
  - "Regra 4: Não assuma que 'modelo aligned' = seguro sob prompt injection."
  - "Exceção: Apps só internas com prompts fixos podem priorizar SFT leve antes de RLHF completo."
```

---

## 🔗 3. Notas Relacionadas
- [[Fine-tuning]]
- [[Engenharia-de-Prompts]]
- [[Guardrails]]
- [[Alucinacao]]
- [[HITL]]
- [[Red-Teaming]]
- [[Agente-de-IA]]

## 📚 4. Fontes
- Ver `Fontes/RLHF.md`.
- Ouyang et al., arXiv:2203.02155.
