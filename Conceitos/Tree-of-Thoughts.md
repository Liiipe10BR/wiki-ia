---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Tree of Thoughts", "ToT", "Árvore de pensamentos"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Tree of Thoughts (Yao et al., NeurIPS 2023)"
---

# 🌳 Tree of Thoughts (ToT)

> **Resumo para Humanos:**
> Generaliza [[Chain-of-Thought]]: em vez de **uma** cadeia linear, explora uma
> **árvore** de pensamentos intermediários, com avaliação, lookahead e
> backtracking.

---

## 📖 1. Contexto Humano (Narrativa)

CoT é greedy e left-to-right. **Tree of Thoughts** (Yao et al., arXiv:2305.10601,
NeurIPS 2023) trata “pensamentos” como nós: o modelo propõe vários candidatos,
avalia quais valem a pena expandir e pode voltar atrás.

No paper, em Game of 24, GPT-4 + CoT resolveu ~4% dos casos no setup descrito;
ToT chegou a ~74%. Também avaliaram escrita criativa e mini-cruzadinhas —
tarefas que exigem planejamento ou busca, não só um passo de raciocínio.

### Comparação rápida

| | CoT | Self-Consistency | ToT |
|--|-----|------------------|-----|
| Estrutura | Cadeia | Várias cadeias + voto | Árvore + busca |
| Backtrack | Não | Não | Sim |
| Custo | 1× | N× | Alto (ramos × profundidade) |

ToT é **inferência deliberada**, não treino. Em agentes, aparece quando o
problema precisa de exploração (quebra-cabeça, plano multi-hipótese). Para FAQ
com [[RAG]], costuma ser overkill frente a ReAct simples.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Tree of Thoughts — busca deliberada sobre pensamentos intermediários"
relations:
  - is_a: "Framework de inferência que generaliza Chain-of-Thought"
  - depends_on: "[[Chain-of-Thought]]"
  - related_to: "[[Self-Consistency]]"
  - related_to: "[[ReAct]]"
  - related_to: "[[Plan-and-Execute]]"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[Janela-de-Contexto]]"
rules_of_thumb:
  - "Regra 1: Reserve ToT para tarefas com espaço de busca real; não use por padrão em todo prompt."
  - "Regra 2: Defina orçamento de nós/expansões — ToT explode tokens rápido."
  - "Regra 3: A função de avaliação dos pensamentos é tão crítica quanto a geração."
  - "Regra 4: Logue a árvore para debug ([[Observabilidade-de-IA]])."
  - "Exceção: Problemas one-shot factuais com RAG raramente precisam de ToT."
```

---

## 🔗 3. Notas Relacionadas
- [[Chain-of-Thought]]
- [[Self-Consistency]]
- [[ReAct]]
- [[Plan-and-Execute]]
- [[Agente-de-IA]]
- [[Janela-de-Contexto]]

## 📚 4. Fontes
- Ver `Fontes/Tree-of-Thoughts.md`.
- Yao et al., arXiv:2305.10601.
