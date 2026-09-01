---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Mixture of Experts", "MoE", "Mixture-of-Experts", "Switch Transformer"]
data_criacao: 2026-09-01
ultima_verificacao: 2026-09-01
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — nota Mixture-of-Experts (Switch Transformers)"
---

# 🧩 Mixture-of-Experts (MoE)

> **Resumo para Humanos:**
> Arquitetura em que **só uma parte dos parâmetros** (experts) é ativada por
> token — muitos parâmetros no total, custo de compute por token mais controlado.

---

## 📖 1. Contexto Humano (Narrativa)

Transformers densos usam os mesmos pesos para todo token. Em **Mixture of
Experts**, camadas (em geral FFN) viram um conjunto de *experts* + um *router*
que escolhe quais experts rodam para cada entrada.

**Switch Transformers** (Fedus et al., arXiv:2101.03961) simplificam o roteamento
(ênfase em um expert por token no desenho Switch) e mostram que é possível
escalar parâmetros com FLOPs por token mais estáveis, com speedups de
pré-treino reportados frente a baselines densos no paper.

### Por que o praticante de agentes se importa

- Modelos abertos “grandes no papel” podem ser MoE: **parâmetros totais ≠
  custo de inferência linear**
- [[Roteamento-de-Modelos]] escolhe *qual modelo*; MoE roteia *dentro* do modelo
- [[Quantizacao]] e serving MoE têm trade-offs próprios (memória de todos os
  experts vs. compute esparso)

### Desafios clássicos

- Instabilidade de treino e balanceamento de experts
- Comunicação em multi-GPU
- Fine-tuning e batch size por expert
- Latência de roteamento em serving

MoE **não** é técnica de prompting nem de [[RAG]]; é escolha de **arquitetura
de modelo**. Para o vault, serve para não confundir “70B denso” com “N bilhões
esparsos”.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Mixture-of-Experts — ativação esparsa de parâmetros"
relations:
  - is_a: "Família de arquiteturas com roteamento para experts"
  - related_to: "[[Fine-tuning]]"
  - related_to: "[[Quantizacao]]"
  - related_to: "[[Roteamento-de-Modelos]]"
  - related_to: "[[Janela-de-Contexto]]"
rules_of_thumb:
  - "Regra 1: Ao comparar modelos, separe parâmetros totais de FLOPs/token e VRAM de serving."
  - "Regra 2: Benchmarks densos não transferem automaticamente para MoE no mesmo 'tamanho nominal'."
  - "Regra 3: Fine-tuning MoE pode exigir cuidados de roteamento e dados — não trate como denso."
  - "Exceção: Se você só consome API fechada, MoE é detalhe de provedor; foque em qualidade/custo da API."
```

---

## 🔗 3. Notas Relacionadas
- [[Fine-tuning]]
- [[Quantizacao]]
- [[Roteamento-de-Modelos]]
- [[Janela-de-Contexto]]

## 📚 4. Fontes
- Ver `Fontes/Mixture-of-Experts.md`.
- Fedus et al., Switch Transformers, arXiv:2101.03961.
