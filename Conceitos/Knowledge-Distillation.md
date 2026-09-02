---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Knowledge Distillation", "Distilação de conhecimento", "KD", "Teacher-student"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Knowledge Distillation (Hinton et al.)"
---

# 🧪 Knowledge Distillation

> **Resumo para Humanos:**
> Treinar um modelo **menor (student)** para imitar o comportamento de um modelo
> **maior ou ensemble (teacher)** — comprimindo conhecimento, não só labels
> one-hot.

---

## 📖 1. Contexto Humano (Narrativa)

Ensembles e redes grandes predizem bem, mas são caros em serving. **Distilling
the Knowledge in a Neural Network** (Hinton, Vinyals, Dean, arXiv:1503.02531)
populariza: o student aprende das **distribuições suaves** (logits/temperaturas)
do teacher, que carregam mais informação que a classe argmax.

No ecossistema LLM, destilação aparece como:

- Comprimir um teacher forte em um student deployável
- Transferir estilo/comportamento (às vezes com dados sintéticos do teacher)
- Complementar [[Quantizacao]] e [[LoRA]] na stack de eficiência

Não confundir com [[Mixture-of-Experts]] (experts dentro de um modelo) nem com
[[Speculative-Decoding]] (draft na inferência sem treinar student permanente).

### Limites

Student herda vieses e falhas do teacher. Destilar “alinhamento” não substitui
[[Red-Teaming]] do artefato final. Qualidade dos dados de destilação importa
tanto quanto a loss.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Knowledge distillation — student imita teacher"
relations:
  - is_a: "Método de compressão / transferência de comportamento entre modelos"
  - related_to: "[[Fine-tuning]]"
  - related_to: "[[Quantizacao]]"
  - related_to: "[[LoRA]]"
  - related_to: "[[Roteamento-de-Modelos]]"
  - related_to: "[[Mixture-of-Experts]]"
rules_of_thumb:
  - "Regra 1: Avalie o student nas mesmas métricas de tarefa do teacher — não só loss de destilação."
  - "Regra 2: Temperatura e soft targets são parte do método; copie a receita com cuidado."
  - "Regra 3: Documente a linhagem teacher→student ([[Proveniencia-de-Dados]] de treino)."
  - "Exceção: Se o student já atinge o SLO sem teacher, destilação pode ser desnecessária."
```

---

## 🔗 3. Notas Relacionadas
- [[Fine-tuning]]
- [[Quantizacao]]
- [[LoRA]]
- [[Roteamento-de-Modelos]]
- [[Mixture-of-Experts]]
- [[Proveniencia-de-Dados]]

## 📚 4. Fontes
- Ver `Fontes/Knowledge-Distillation.md`.
- Hinton et al., arXiv:1503.02531.
