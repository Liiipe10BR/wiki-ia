---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Constitutional AI", "CAI", "IA constitucional", "RLAIF constitucional"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Constitutional AI (Bai et al., Anthropic)"
---

# 📜 Constitutional AI (CAI)

> **Resumo para Humanos:**
> Treinar um assistente **menos nocivo** usando uma **lista de princípios**
> (“constituição”) e **feedback de IA** (crítica/revisão), com bem menos labels
> humanos de “isso é harmful” do que o RLHF clássico de harmlessness.

---

## 📖 1. Contexto Humano (Narrativa)

**Constitutional AI** (Bai et al., arXiv:2212.08073, Anthropic) propõe
supervisionar o modelo com princípios escritos por humanos + auto-crítica e
revisão geradas por IA:

1. **Fase supervisionada** — amostrar respostas, gerar críticas/revisões conforme
   a constituição, fine-tune nas revisões
2. **Fase RL** — preferências geradas por IA (RLAIF-style) para harmlessness,
   ainda ancoradas nos princípios

O objetivo reportado no paper: assistente **harmless mas não evasivo** — responde
explicando objeções em vez de só recusar. Chain-of-thought entra para tornar a
decisão mais legível a juízes humanos.

### Relação com o vault

| Conceito | Papel |
|----------|--------|
| [[RLHF]] | Preferência humana densa |
| **CAI** | Preferência/princípios + AI feedback |
| [[DPO]] | Método de otimização (pode consumir pares CAI-like) |
| [[Guardrails]] | Controle em **runtime**, não só treino |
| [[Red-Teaming]] | Testa se a constituição “segura” de verdade |

CAI **não** é garantia ética universal: a constituição é escolha de desenho, e
modelos alinhados ainda falham sob pressão adversária. Runtime ([[Guardrails]],
[[HITL]]) continua necessário.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Constitutional AI — alinhamento via princípios e AI feedback"
relations:
  - is_a: "Pipeline de alinhamento com constituição + RLAIF"
  - related_to: "[[RLHF]]"
  - related_to: "[[DPO]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Red-Teaming]]"
  - related_to: "[[Chain-of-Thought]]"
  - related_to: "[[HITL]]"
rules_of_thumb:
  - "Regra 1: Trate a constituição como artefato versionado e revisável."
  - "Regra 2: CAI no treino ≠ política completa em produção — combine com guardrails."
  - "Regra 3: Avalie evasividade vs utilidade; harmless absoluto pode ser inútil."
  - "Regra 4: Red-team princípios e lacunas; texto bonito não basta."
  - "Exceção: Sistemas internos de baixo risco podem usar só policy de prompt + guardrails leves."
```

---

## 🔗 3. Notas Relacionadas
- [[RLHF]]
- [[DPO]]
- [[Guardrails]]
- [[Red-Teaming]]
- [[Chain-of-Thought]]
- [[HITL]]

## 📚 4. Fontes
- Ver `Fontes/Constitutional-AI.md`.
- Bai et al., arXiv:2212.08073.
