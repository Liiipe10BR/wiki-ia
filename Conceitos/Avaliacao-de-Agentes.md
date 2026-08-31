---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Avaliação de Agentes", "Agent Evaluation", "AgentBench", "Avaliação agentic"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.91
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #26 / avaliação de agentes além de Avaliação-de-RAG"
---

# 🧪 Avaliação de agentes

> **Resumo para Humanos:**
> Medir se um [[Agente-de-IA]] **completa tarefas** em ambientes interativos
> (tools, multi-turn, custo, segurança) — não só se a resposta textual está
> “certa” frente a um trecho recuperado.

---

## 📖 1. Contexto Humano (Narrativa)

[[Avaliacao-de-RAG]] separa recuperação, fidelidade e relevância da *resposta*
com base em contexto recuperado. Isso **não cobre** o que importa em agentes:
sequência de decisões, uso correto de [[Tool-Calling]], recuperação de erros,
loops, orçamento de tokens e efeitos no mundo.

**AgentBench** (Liu et al., arXiv:2308.03688, ICLR 2024) formalizou a necessidade
de avaliar LLMs *como agentes* em ambientes interativos multi-turn (código,
jogos, web, etc.). O diagnóstico recorrente: falhas de raciocínio de longo
prazo, decisão e *instruction following* — não só “o modelo não sabe o fato”.

O que costuma ser medido:

1. **Sucesso de tarefa** — completou o objetivo? (binário ou parcial)
2. **Trajetória** — quantos passos, quais tools, argumentos válidos?
3. **Custo e latência** — tokens, chamadas de API, tempo de parede
4. **Segurança / harm** — violou [[Guardrails]], executou ação perigosa?
5. **Robustez** — falha de tool, ambiente ruidoso, prompt adversarial

Offline (benchmarks fixos) ≠ online (produção com humanos e drift). LLM-as-judge
ajuda a escalar, mas herda vieses e não substitui checagem de efeito real da
tool. Em [[Sistemas-Multiagente]], a unidade de avaliação pode ser o *time*,
não o agente isolado — e a falha se propaga.

[[Observabilidade-de-IA]] é pré-requisito: sem traces de tools e decisões, só
se avalia o texto final. Não confunda score de AgentBench com garantia de
produção: ambientes de laboratório não têm a mesma distribuição de tickets,
permissões e dados sujos do mundo real.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Avaliação de agentes de IA em tarefas interativas multi-turn"
relations:
  - is_a: "Protocolo de medição de desempenho, custo e risco de agentes"
  - related_to: "[[Avaliacao-de-RAG]]"
  - depends_on: "[[Agente-de-IA]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[Sistemas-Multiagente]]"
  - related_to: "[[Alucinacao]]"
rules_of_thumb:
  - "Regra 1: Não use só métricas de RAG (faithfulness/relevância) para agentes com tools; meça sucesso de tarefa e validade da trajetória."
  - "Regra 2: Separe avaliação offline (benchmark) de online (produção); calibre ambas com amostragem humana."
  - "Regra 3: Registre custo (tokens, $) e número de tool calls por tarefa — qualidade sem orçamento é incompleta."
  - "Regra 4: LLM-as-judge é auxiliar; valide contra efeitos reais de tools e contra gold humano em amostra."
  - "Regra 5: Em multiagente, defina se a métrica é por agente ou pelo resultado do sistema."
  - "Exceção: Chat sem tools e sem estado pode reutilizar avaliações de geração clássicas; ainda assim separe alucinação de utilidade."
```

---

## 🔗 3. Notas Relacionadas
- [[Avaliacao-de-RAG]]
- [[Agente-de-IA]]
- [[Tool-Calling]]
- [[Guardrails]]
- [[Observabilidade-de-IA]]
- [[Sistemas-Multiagente]]
- [[Alucinacao]]

## 📚 4. Fontes
- Ver `Fontes/Avaliacao-de-Agentes.md`.
- AgentBench, arXiv:2308.03688 (ICLR 2024).
