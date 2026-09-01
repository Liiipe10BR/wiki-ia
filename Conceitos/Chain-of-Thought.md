---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Chain-of-Thought", "CoT", "Cadeia de pensamento", "Chain of Thought prompting"]
data_criacao: 2026-09-01
ultima_verificacao: 2026-09-01
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — nota Chain-of-Thought (Wei et al.)"
---

# 🧠 Chain-of-Thought (CoT)

> **Resumo para Humanos:**
> Fazer o modelo **escrever passos intermediários** de raciocínio antes da
> resposta final — em vez de saltar direto ao resultado.

---

## 📖 1. Contexto Humano (Narrativa)

Em tarefas de aritmética, senso comum ou raciocínio simbólico, pedir só a
resposta final costuma falhar. **Chain-of-Thought prompting** (Wei et al.,
arXiv:2201.11903) mostra que *demonstrar* cadeias de pensamento em few-shot
(ou induzir “pense passo a passo”) melhora o desempenho em modelos
suficientemente grandes.

No paper, poucos exemplares CoT em um modelo de 540B atingiram resultados
fortes em GSM8K, superando baselines sem passos intermediários nos setups
avaliados. O ganho **não** é mágica de prompt isolada: depende de escala do
modelo e da qualidade dos exemplares.

### Variantes comuns

| Variante | Ideia |
|----------|--------|
| **Few-shot CoT** | Exemplos com raciocínio explícito no prompt |
| **Zero-shot CoT** | Instrução do tipo “pense passo a passo” sem exemplares |
| **Self-consistency** | Várias cadeias + votação na resposta final |

### Onde encaixa no vault

- Base de [[Engenharia-de-Prompts]] para raciocínio
- [[ReAct]] **intercala** CoT-like *thought* com **ações** (tools)
- [[Reflexion]] reflete *depois* da tentativa; CoT raciocina *durante*
- Consome [[Janela-de-Contexto]] — cadeias longas competem com [[RAG]]

### Limites

CoT pode **alucinar passos** plausíveis e errados ([[Alucinacao]]). Não
substitui ferramentas, retrieval nem verificação. Em produção, meça tarefa e
custo de tokens, não só “parece mais inteligente”.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Chain-of-Thought prompting e raciocínio intermediário"
relations:
  - is_a: "Técnica de prompting que externaliza passos de raciocínio"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[In-Context-Learning]]"
  - related_to: "[[ReAct]]"
  - related_to: "[[Reflexion]]"
  - related_to: "[[Janela-de-Contexto]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[Agente-de-IA]]"
rules_of_thumb:
  - "Regra 1: Use CoT quando a tarefa exigir multi-step; para classificação simples o custo pode não valer."
  - "Regra 2: Exemplares CoT de qualidade > quantidade de exemplares ruins."
  - "Regra 3: Não trate passos intermediários como fatos verificados sem grounding."
  - "Regra 4: Orce tokens — CoT alonga o contexto e o custo."
  - "Exceção: Modelos pequenos podem não exibir o mesmo ganho reportado em escala grande."
```

---

## 🔗 3. Notas Relacionadas
- [[Engenharia-de-Prompts]]
- [[In-Context-Learning]]
- [[ReAct]]
- [[Reflexion]]
- [[Janela-de-Contexto]]
- [[Alucinacao]]
- [[Agente-de-IA]]

## 📚 4. Fontes
- Ver `Fontes/Chain-of-Thought.md`.
- Wei et al., arXiv:2201.11903.
