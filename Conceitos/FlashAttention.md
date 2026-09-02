---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["FlashAttention", "Flash Attention", "Atenção IO-aware"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — FlashAttention (Dao et al.)"
---

# ⚡ FlashAttention

> **Resumo para Humanos:**
> Algoritmo de **attention exata** mais rápida e com menos memória, reduzindo
> idas e vindas entre HBM e SRAM da GPU via tiling — habilita contextos mais
> longos na prática.

---

## 📖 1. Contexto Humano (Narrativa)

Self-attention padrão é quadrática em tempo e memória na sequência. Em GPUs, o
gargalo frequentemente é **IO de memória**, não só FLOPs. **FlashAttention**
(Dao et al., arXiv:2205.14135) é IO-aware: calcula attention exata com tiling
para minimizar reads/writes em HBM.

O paper reporta speedups end-to-end de treino (ex.: BERT-large, GPT-2, long-range
arena) e viabiliza sequências longas com qualidade melhor em alguns benchmarks
do estudo. Versões posteriores (FlashAttention-2, etc.) refinaram performance;
o conceito útil ao vault é: **otimização de kernel de attention**, não um novo
tipo de modelo.

### Ligação prática

- Afeta [[Janela-de-Contexto]] viável em hardware real
- Complementa [[Quantizacao]] e [[Speculative-Decoding]] no eixo eficiência
- Quem só consome API raramente configura FA direto — mas explica por que
  contextos longos ficaram mais baratos/rápidos ao longo do tempo

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "FlashAttention — attention exata IO-aware"
relations:
  - is_a: "Algoritmo/kernel de attention eficiente em GPU"
  - related_to: "[[Janela-de-Contexto]]"
  - related_to: "[[Quantizacao]]"
  - related_to: "[[Speculative-Decoding]]"
  - related_to: "[[Mixture-of-Experts]]"
rules_of_thumb:
  - "Regra 1: Em serving self-hosted, verifique se o stack (PyTorch/SDPA, xFormers, etc.) usa FA ou equivalente."
  - "Regra 2: Não confunda speedup de kernel com mudança de qualidade do modelo — FA é exata no paper base."
  - "Regra 3: Contexto longo ainda consome tokens de API/custo de produto; FA não zera a conta."
  - "Exceção: Inferência só via API gerenciada — trate FA como detalhe do provedor."
```

---

## 🔗 3. Notas Relacionadas
- [[Janela-de-Contexto]]
- [[Quantizacao]]
- [[Speculative-Decoding]]
- [[Mixture-of-Experts]]

## 📚 4. Fontes
- Ver `Fontes/FlashAttention.md`.
- Dao et al., arXiv:2205.14135.
