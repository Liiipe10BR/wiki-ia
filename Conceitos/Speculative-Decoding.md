---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Speculative Decoding", "Decodificação especulativa", "Speculative sampling"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Speculative Decoding (Leviathan et al.)"
---

# ⚡ Speculative Decoding

> **Resumo para Humanos:**
> Acelerar a geração **sem mudar a distribuição** do modelo grande: um modelo
> *draft* propõe vários tokens; o modelo *target* verifica em paralelo e aceita
> o prefixo válido.

---

## 📖 1. Contexto Humano (Narrativa)

Decoding autoregressivo é serial: K tokens ≈ K passes do modelo grande.
**Speculative decoding** (Leviathan et al., arXiv:2211.17192, ICML 2023 Oral)
explora que subtarefas “fáceis” podem ser antecipadas por um modelo mais barato.
O draft gera candidatos; o target valida e, com o método de amostragem do paper,
a saída permanece **distribuicionalmente equivalente** ao decoding normal do
target — só mais rápida quando o draft acerta com frequência.

No paper, em T5-XXL, reportam cerca de 2×–3× de aceleração vs implementação
padrão, com saídas idênticas no regime descrito.

### O que não é

- Não é quantização nem MoE (embora combine com ambos)
- Não muda a “personalidade” do modelo — é otimização de **serving**
- Draft ruim → pouca aceitação → pouco speedup

Para agentes e APIs, speculative decoding aparece em backends de inferência;
o desenhador de [[Agente-de-IA]] sente **latência**, não o algoritmo. Ainda assim,
entender o trade-off evita confundir “modelo menor” com “resposta diferente”.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Speculative decoding — aceleração de inferência sem mudar distribuição"
relations:
  - is_a: "Algoritmo de decoding paralelo com verificação pelo modelo target"
  - related_to: "[[Quantizacao]]"
  - related_to: "[[Mixture-of-Experts]]"
  - related_to: "[[Roteamento-de-Modelos]]"
  - related_to: "[[Janela-de-Contexto]]"
rules_of_thumb:
  - "Regra 1: Meça taxa de aceitação do draft — sem ela não há speedup."
  - "Regra 2: Preserve equivalência de distribuição se a spec exigir bit-identical / same dist."
  - "Regra 3: Draft alinhado ao domínio do target costuma aceitar mais tokens."
  - "Exceção: Batch offline onde throughput importa mais que latência interativa pode priorizar outras otimizações."
```

---

## 🔗 3. Notas Relacionadas
- [[Quantizacao]]
- [[Mixture-of-Experts]]
- [[Roteamento-de-Modelos]]
- [[Janela-de-Contexto]]

## 📚 4. Fontes
- Ver `Fontes/Speculative-Decoding.md`.
- Leviathan et al., arXiv:2211.17192.
