---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Quantização", "Quantization", "PTQ", "QAT", "Low-bit LLM"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #16; nota sobre quantização de modelos e trade-offs"
---

# 📉 Quantização

> **Resumo para Humanos:**
> Redução da precisão numérica dos pesos (e às vezes ativações/KV cache) de um
> modelo para caber em menos memória, inferir mais rápido e barato — com
> trade-offs de qualidade que dependem do método, do número de bits, do modelo
> e da tarefa.

---

## 📖 1. Contexto Humano (Narrativa)

Modelos grandes em FP16/BF16 consomem muita VRAM. **Quantização** representa
pesos (e opcionalmente ativações) com menos bits — tipicamente INT8, INT4 ou
formatos de baixa precisão — para reduzir memória e acelerar matrizes em
hardware compatível.

Dois regimes principais:

- **PTQ (post-training quantization):** quantiza um modelo já treinado, com
  calibração em um conjunto de dados; mais barato de aplicar. Exemplos
  influentes: GPTQ, AWQ, bitsandbytes.
- **QAT (quantization-aware training):** simula quantização durante o treino
  ou fine-tuning; em geral recupera mais qualidade em bits muito baixos, com
  custo de treino maior.

Há diferença entre quantizar só **pesos** (weight-only) e quantizar também
**ativações** (e KV cache). Weight-only é comum em inferência local; ativação
e KV afetam latência e memória de contexto longo.

Nenhuma técnica é universalmente “a melhor”: resultados variam com tamanho do
modelo, arquitetura, calibração, hardware (GPU, CPU, NPU) e se a tarefa é
geração aberta, raciocínio ou classificação. Relaciona-se a [[Fine-tuning]]
(QLoRA e similares combinam adaptadores com pesos quantizados) e a execução
local / edge.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Quantização de pesos e ativações em LLMs"
relations:
  - is_a: "Compressão de precisão numérica para eficiência de inferência (e às vezes treino)"
  - related_to: "[[Fine-tuning]] (QLoRA e variantes usam pesos quantizados + adaptadores)"
  - related_to: "[[Janela-de-Contexto]] (KV cache quantizado afeta memória de contexto longo)"
rules_of_thumb:
  - "Regra 1: Meça qualidade na sua tarefa e no seu modelo; benchmarks genéricos não transferem automaticamente."
  - "Regra 2: Distinga PTQ (barato, pós-treino) de QAT (mais caro, em geral melhor em bits extremos)."
  - "Regra 3: Weight-only vs pesos+ativações (+KV) muda o perfil de memória e velocidade."
  - "Regra 4: Bits mais baixos (ex.: 2–3) degradam mais; 4 e 8 bits são o ponto prático mais comum em 2024–2026."
  - "Regra 5: Não declare um método (GPTQ, AWQ, etc.) como vencedor universal — depende de hardware e workload."
  - "Exceção: Em protótipos, quantização agressiva pode ser aceitável se o usuário aceita perda de qualidade."
```

---

## 🔗 3. Notas Relacionadas
- [[Fine-tuning]]
- [[Janela-de-Contexto]]

## 📚 4. Fontes
- Ver `Fontes/Quantizacao.md`.
- GPTQ (Frantar et al.), AWQ (Lin et al.); surveys de low-bit / PTQ para LLMs.
