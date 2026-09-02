---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["DPO", "Direct Preference Optimization", "Otimização direta de preferência"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — DPO (Rafailov et al.)"
---

# 📐 DPO (Direct Preference Optimization)

> **Resumo para Humanos:**
> Alinhar o modelo a preferências **sem treinar um reward model separado e sem
> loop RL clássico** — otimização direta com loss de classificação sobre pares
> preferidos/rejeitados.

---

## 📖 1. Contexto Humano (Narrativa)

[[RLHF]] clássico (InstructGPT) usa SFT → reward model → RL (ex.: PPO). Isso é
poderoso e operacionalmente pesado. **DPO** (Rafailov et al., arXiv:2305.18290)
reparametriza o problema: sob certas condições o policy ótimo tem forma
fechada, e o treino vira um **loss simples** em dados de preferência
(y_w ≻ y_l | x).

No paper, DPO iguala ou supera métodos RLHF em eixos como controle de sentimento,
sumarização e diálogo single-turn nos setups avaliados, com implementação mais
leve (sem amostrar o LM no loop de RL nem ajustar tantos hiperparâmetros de PPO).

### Onde encaixa

| Abordagem | Reward model | Loop RL |
|-----------|--------------|--------|
| RLHF (PPO) | Sim | Sim |
| **DPO** | Implícito na policy | Não |

DPO **não** elimina a necessidade de dados de preferência de qualidade. Também
não substitui [[Guardrails]] em runtime. Em stacks abertas, DPO (e variantes)
viurou caminho padrão de pós-treino alinhado junto com [[Fine-tuning]] / [[LoRA]].

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Direct Preference Optimization (DPO)"
relations:
  - is_a: "Método de alinhamento por preferência sem RL explícito"
  - related_to: "[[RLHF]]"
  - related_to: "[[Fine-tuning]]"
  - related_to: "[[LoRA]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Constitutional-AI]]"
rules_of_thumb:
  - "Regra 1: Qualidade e cobertura dos pares de preferência limitam o teto do DPO."
  - "Regra 2: Monitore regressões em tarefas úteis (reward hacking / over-optimization)."
  - "Regra 3: DPO alinha treino; prompt injection e tools ainda exigem controles de runtime."
  - "Regra 4: Combine com LoRA quando quiser adapters leves por domínio."
  - "Exceção: Se já há pipeline PPO maduro e estável, migrar só por moda não é obrigatório."
```

---

## 🔗 3. Notas Relacionadas
- [[RLHF]]
- [[Fine-tuning]]
- [[LoRA]]
- [[Guardrails]]
- [[Constitutional-AI]]

## 📚 4. Fontes
- Ver `Fontes/DPO.md`.
- Rafailov et al., arXiv:2305.18290.
