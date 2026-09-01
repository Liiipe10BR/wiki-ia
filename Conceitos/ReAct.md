---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["ReAct", "Reason + Act", "Reasoning and Acting"]
data_criacao: 2026-09-01
ultima_verificacao: 2026-09-01
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — nota ReAct (Yao et al.)"
---

# 🔄 ReAct

> **Resumo para Humanos:**
> Padrão em que o modelo **alterna raciocínio em linguagem natural e ações**
> (consultas, tools) na mesma trajetória — em vez de só pensar *ou* só agir.

---

## 📖 1. Contexto Humano (Narrativa)

[[Chain-of-Thought]] melhora raciocínio interno, mas pode propagar erro sem
contato com o mundo. Planos de ação sem reflexão ficam opacos. **ReAct** (Yao
et al., arXiv:2210.03629) **sinergiza** os dois: traces do tipo
*Thought → Action → Observation* repetidos até a resposta.

No paper, em QA (HotpotQA) e fact-checking (FEVER), interagir com uma API
(Wikipedia) reduziu problemas de [[Alucinacao]] e propagação de erro típicos de
CoT puro nos setups descritos. Em benchmarks interativos (ALFWorld, WebShop),
ReAct superou métodos de imitação/RL reportados, com poucos exemplos
in-context.

### Por que importa para produção

A maior parte dos frameworks de [[Agente-de-IA]] e [[Tool-Calling]] implementa
uma variante desse loop. [[Model-Context-Protocol]] e tools concretas são o
*Action/Observation*; o *Thought* é [[Engenharia-de-Prompts]] + política do
agente.

### Limites

- Trajetórias longas estouram [[Janela-de-Contexto]]
- Thought malformado → Action inútil
- Observation adversária (documento injetado) → [[Prompt-Injection]]
- Não define sozinho [[Guardrails]] nem [[HITL]]

[[Reflexion]] age *entre tentativas*; ReAct age *dentro* de uma tentativa.
[[Sistemas-Multiagente]] podem distribuir papéis, mas o executor ainda costuma
ser ReAct-like.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "ReAct — raciocínio e ação intercalados"
relations:
  - is_a: "Padrão de trajetória Thought-Action-Observation"
  - depends_on: "[[Agente-de-IA]]"
  - related_to: "[[Chain-of-Thought]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[Reflexion]]"
  - related_to: "[[Model-Context-Protocol]]"
  - related_to: "[[Prompt-Injection]]"
rules_of_thumb:
  - "Regra 1: Limite passos Thought/Action; sem teto o agente loopa."
  - "Regra 2: Trate Observation como não confiável até validar (injection, lixo da tool)."
  - "Regra 3: Logue a trajetória completa para [[Observabilidade-de-IA]] e debug."
  - "Regra 4: Prefira actions com schema claro ([[Saida-Estruturada]] / tool schema)."
  - "Exceção: FAQ com RAG one-shot pode não precisar do loop ReAct completo."
```

---

## 🔗 3. Notas Relacionadas
- [[Agente-de-IA]]
- [[Chain-of-Thought]]
- [[Tool-Calling]]
- [[Engenharia-de-Prompts]]
- [[Alucinacao]]
- [[Reflexion]]
- [[Model-Context-Protocol]]
- [[Prompt-Injection]]

## 📚 4. Fontes
- Ver `Fontes/ReAct.md`.
- Yao et al., arXiv:2210.03629.
