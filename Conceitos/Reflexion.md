---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Reflexion", "Self-reflection", "Verbal reinforcement learning"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #41 / Reflexion e self-reflection em agentes"
---

# 🔁 Reflexion

> **Resumo para Humanos:**
> O agente **escreve uma reflexão** sobre o erro ou o feedback da tarefa,
> guarda isso em memória episódica e tenta de novo — reforço *linguístico*,
> não update de pesos.

---

## 📖 1. Contexto Humano (Narrativa)

ReAct intercala pensamento e ação numa trajetória. **Reflexion** (Shinn et al.,
arXiv:2303.11366, NeurIPS 2023) adiciona: após falha (ou sinal de recompensa),
o agente verbaliza o que deu errado e reutiliza essa reflexão em tentativas
seguintes. O paper reporta ganhos em coding, decisão sequencial e raciocínio
linguístico nos setups avaliados (ex.: HumanEval pass@1 elevado vs. baseline
do estudo).

Diferença de retry cego: há **memória de lições**, alinhada a
[[Memoria-de-Agentes]]. Custo: mais tokens e risco de loops se a reflexão for
vaga. Não resolve sozinho [[Alucinacao]] factual nem substitui tools corretas.
Em [[Sistemas-Multiagente]], reflexão pode ser por agente ou por crítico
separado.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Reflexion — reforço verbal e memória episódica de agentes"
relations:
  - is_a: "Padrão de agente com auto-crítica verbal entre tentativas"
  - depends_on: "[[Agente-de-IA]]"
  - related_to: "[[Memoria-de-Agentes]]"
  - related_to: "[[Avaliacao-de-Agentes]]"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[Sistemas-Multiagente]]"
  - related_to: "[[Alucinacao]]"
rules_of_thumb:
  - "Regra 1: Limite o número de retries com reflexão; reflexão sem orçamento vira loop caro."
  - "Regra 2: Exija feedback concreto (teste falhou, tool erro) — reflexão sem sinal é teatro."
  - "Regra 3: Persista reflexões úteis na memória episódica; não só no contexto da sessão."
  - "Regra 4: Avalie se a reflexão mudou a trajetória, não só se o texto 'parece' introspectivo."
  - "Exceção: Tarefas one-shot baratas podem não justificar o overhead de Reflexion."
```

---

## 🔗 3. Notas Relacionadas
- [[Agente-de-IA]]
- [[Memoria-de-Agentes]]
- [[Avaliacao-de-Agentes]]
- [[Engenharia-de-Prompts]]
- [[Sistemas-Multiagente]]
- [[Alucinacao]]

## 📚 4. Fontes
- Ver `Fontes/Reflexion.md`.
- Shinn et al., arXiv:2303.11366 (NeurIPS 2023).
