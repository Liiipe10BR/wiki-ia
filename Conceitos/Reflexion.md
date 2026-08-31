---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Reflexion", "Self-reflection", "Verbal reinforcement learning", "Auto-crítica de agente"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-31
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #41; aprofundamento 2026-08-31 a partir do paper Reflexion"
---

# 🔁 Reflexion

> **Resumo para Humanos:**
> Depois de uma falha (ou sinal de feedback), o agente **escreve uma reflexão
em linguagem natural**, guarda isso em memória episódica e **tenta de novo** —
> reforço verbal, sem atualizar pesos do modelo.

---

## 📖 1. Contexto Humano (Narrativa)

No loop ReAct ([[Agente-de-IA]]), o modelo intercala pensamento e ação numa
trajetória. Se a tarefa falha, um retry cego repete os mesmos erros.
**Reflexion** (Shinn et al., arXiv:2303.11366, NeurIPS 2023) propõe:

1. Executar tentativa
2. Receber feedback (teste unitário, ambiente, juiz, score)
3. **Verbalizar** o que deu errado e o que mudar
4. Armazenar a reflexão em buffer episódico
5. Nova tentativa condicionada a essas lições

O paper enfatiza flexibilidade do feedback (escalar ou texto; externo ou
simulado) e mostra ganhos em decisão sequencial, coding e raciocínio nos setups
avaliados (ex.: melhoria reportada em HumanEval pass@1 no estudo).

### Relação com outras ideias do vault

- [[Memoria-de-Agentes]] — reflexões são conteúdo natural da memória episódica /
  recall entre tentativas
- [[Engenharia-de-Prompts]] — o *prompt* de reflexão importa tanto quanto o de
  ação
- [[Avaliacao-de-Agentes]] — medir se a reflexão **mudou a trajetória**, não se
  o texto “parece introspectivo”
- [[Sistemas-Multiagente]] — um agente “crítico” pode gerar a reflexão para o
  executor

### Custos e falhas

- Mais tokens por tarefa (várias tentativas + texto de reflexão)
- Reflexão vaga (“preciso ser mais cuidadoso”) não corrige bug real
- Loops se o limite de retries for alto e o feedback for ruidoso
- Não substitui tools corretas nem remove [[Alucinacao]] factual sozinha

Use quando houver **sinal de erro utilizável** (teste falhou, tool retornou
erro, métrica de ambiente). Evite em one-shot barato sem orçamento.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Reflexion — reforço verbal entre tentativas de agentes"
relations:
  - is_a: "Padrão de agente com auto-crítica verbal e memória episódica"
  - depends_on: "[[Agente-de-IA]]"
  - related_to: "[[Memoria-de-Agentes]]"
  - related_to: "[[Avaliacao-de-Agentes]]"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[Sistemas-Multiagente]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[Tool-Calling]]"
rules_of_thumb:
  - "Regra 1: Limite retries com reflexão; sem orçamento vira loop caro."
  - "Regra 2: Exija feedback concreto (teste, erro de tool, score) — reflexão sem sinal é teatro."
  - "Regra 3: Persista reflexões úteis além da janela da sessão."
  - "Regra 4: Avalie mudança de trajetória/sucesso, não só fluência da auto-crítica."
  - "Regra 5: Não use Reflexion como único mitigador de alucinação factual."
  - "Exceção: Tarefas one-shot baratas podem não justificar o overhead."
```

---

## 🔗 3. Notas Relacionadas
- [[Agente-de-IA]]
- [[Memoria-de-Agentes]]
- [[Avaliacao-de-Agentes]]
- [[Engenharia-de-Prompts]]
- [[Sistemas-Multiagente]]
- [[Alucinacao]]
- [[Tool-Calling]]

## 📚 4. Fontes
- Ver `Fontes/Reflexion.md`.
- Shinn et al., Reflexion, arXiv:2303.11366 (NeurIPS 2023).
