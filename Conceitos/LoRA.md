---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["LoRA", "Low-Rank Adaptation", "Adaptação de baixa ordem", "PEFT LoRA"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — LoRA (Hu et al.)"
---

# 🔧 LoRA (Low-Rank Adaptation)

> **Resumo para Humanos:**
> **Congelar** os pesos do modelo base e treinar só **matrizes de baixa ordem**
> injetadas nas camadas — fine-tuning barato, adapters trocáveis, pouca ou
> nenhuma latência extra na inferência.

---

## 📖 1. Contexto Humano (Narrativa)

Fine-tuning completo de um LLM grande é caro em memória e em armazenamento por
variante. **LoRA** (Hu et al., arXiv:2106.09685) congela W₀ e aprende
ΔW ≈ BA com rank r ≪ dimensões originais. No paper, em GPT-3 175B, reportam
ordens de magnitude menos parâmetros treináveis e menos memória GPU vs
fine-tuning Adam completo, com qualidade on-par ou melhor nos benchmarks
avaliados, e **sem** latência extra típica de adapters sequenciais (os deltas
podem ser mesclados).

### Por que importa no vault

- Especialização de domínio sem copiar o modelo inteiro
- Combina com [[DPO]] / [[RLHF]] em stacks PEFT
- Vários adapters (clientes, idiomas, tools) sobre o mesmo base
- [[Quantizacao]] + LoRA (QLoRA e afins) é padrão de treino em GPU única

### Limites

Rank baixo demais subajusta; rank alto perde a vantagem. LoRA **não** define a
objetivo de alinhamento — só *como* atualizar pesos com poucos parâmetros.
Escolha de módulos (q/v/proj) e r é hiperparâmetro de engenharia.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "LoRA — adaptação de baixa ordem para fine-tuning eficiente"
relations:
  - is_a: "Método PEFT com matrizes low-rank"
  - related_to: "[[Fine-tuning]]"
  - related_to: "[[DPO]]"
  - related_to: "[[RLHF]]"
  - related_to: "[[Quantizacao]]"
  - related_to: "[[Mixture-of-Experts]]"
rules_of_thumb:
  - "Regra 1: Comece com r pequeno e suba se o gap para full FT for inaceitável."
  - "Regra 2: Versionar adapters como artefatos — são o produto do fine-tune."
  - "Regra 3: Em serving, decida merge vs multi-adapter dinâmico conforme latência/ops."
  - "Regra 4: LoRA não substitui dados bons nem avaliação de regressão."
  - "Exceção: Modelos já minúsculos podem full-FT sem drama."
```

---

## 🔗 3. Notas Relacionadas
- [[Fine-tuning]]
- [[DPO]]
- [[RLHF]]
- [[Quantizacao]]
- [[Mixture-of-Experts]]

## 📚 4. Fontes
- Ver `Fontes/LoRA.md`.
- Hu et al., arXiv:2106.09685.
