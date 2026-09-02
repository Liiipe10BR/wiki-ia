---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Self-Consistency", "Self consistency", "Consistência interna", "SC decoding"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Self-Consistency (Wang et al., ICLR 2023)"
---

# 🎲 Self-Consistency

> **Resumo para Humanos:**
> Em vez de uma única cadeia gulosa de [[Chain-of-Thought]], **amostrar várias
> trajetórias de raciocínio** e escolher a resposta final **mais consistente**
> (voto / marginalização).

---

## 📖 1. Contexto Humano (Narrativa)

CoT com decoding guloso depende de um único caminho. **Self-Consistency** (Wang
et al., arXiv:2203.11171, ICLR 2023) propõe: amostrar caminhos diversos e
agregar a resposta final — a intuição é que problemas difíceis admitem várias
linhas de raciocínio que convergem na mesma resposta correta.

O paper reporta ganhos amplos sobre CoT guloso em GSM8K, SVAMP, AQuA,
StrategyQA e ARC-challenge nos setups avaliados (ex.: +17.9 pontos em GSM8K no
estudo).

### Custo vs qualidade

| | CoT guloso | Self-Consistency |
|--|------------|------------------|
| Chamadas | 1 | N amostras |
| Tokens | 1× | ~N× |
| Robustez | Frágil a um erro no meio | Mais estável se a maioria acerta |

É técnica de **decoding / agregação**, não de treino. Combina bem com
[[In-Context-Learning]] e [[Engenharia-de-Prompts]]. Em agentes, use quando a
resposta final for discreta (número, opção, label); para geração aberta longa o
“voto” é menos natural.

Não substitui [[Grounding]] nem tools: caminhos consistentes podem ser
consistentemente errados.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Self-Consistency — agregação de múltiplos caminhos CoT"
relations:
  - is_a: "Estratégia de decoding sobre Chain-of-Thought"
  - depends_on: "[[Chain-of-Thought]]"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[In-Context-Learning]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[Roteamento-de-Modelos]]"
rules_of_thumb:
  - "Regra 1: Use quando a resposta final for agregável (número, escolha, label)."
  - "Regra 2: Orce N amostras — SC multiplica custo de tokens."
  - "Regra 3: Temperatura > 0 é necessária para diversidade de caminhos."
  - "Regra 4: Consistência ≠ verdade; ainda valide com tools/RAG se o risco for alto."
  - "Exceção: Tarefas one-shot baratas ou respostas abertas longas podem não valer SC."
```

---

## 🔗 3. Notas Relacionadas
- [[Chain-of-Thought]]
- [[Engenharia-de-Prompts]]
- [[In-Context-Learning]]
- [[Alucinacao]]
- [[Roteamento-de-Modelos]]

## 📚 4. Fontes
- Ver `Fontes/Self-Consistency.md`.
- Wang et al., arXiv:2203.11171 (ICLR 2023).
