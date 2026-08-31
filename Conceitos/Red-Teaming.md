---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Red Teaming", "Red team", "Avaliação adversarial", "Adversarial evaluation"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.90
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #40 / red teaming de LLMs e agentes"
---

# 🛡️ Red teaming

> **Resumo para Humanos:**
> **Procurar de propósito** falhas de segurança e abuso em modelos e agentes
> (jailbreak, vazamento, tool indevida) — como processo de avaliação, não como
> tutorial de ataque.

---

## 📖 1. Contexto Humano (Narrativa)

[[Avaliacao-de-Agentes]] mede sucesso de tarefa. **Red teaming** mede se o
sistema *resiste* a uso adversário: [[Prompt-Injection]], exfiltração,
bypass de [[Guardrails]], ações de tool não autorizadas.

Pode ser manual (especialistas) ou automatizado (geradores de prompts
adversários). Cobertura ampla ≠ profundidade em um vetor. OWASP LLM Top 10 e
guias de vendors enquadram riscos; a nota **não** detalha exploits.

Resultados alimentam mitigação (policy, filtros, HITL) e [[Observabilidade-de-IA]].
Red team contínuo em produção é diferente de checklist único pré-lançamento.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Red teaming e avaliação adversarial de LLMs/agentes"
relations:
  - is_a: "Processo de avaliação orientado a falhas de segurança e abuso"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Prompt-Injection]]"
  - related_to: "[[Avaliacao-de-Agentes]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[HITL]]"
rules_of_thumb:
  - "Regra 1: Defina ameaças no escopo (dados, tools, usuários) antes de gerar casos."
  - "Regra 2: Separe descoberta (red team) de mitigação (guardrails/HITL); uma não substitui a outra."
  - "Regra 3: Documente achados com severidade e reprodução mínima — sem publicar receitas de exploração."
  - "Regra 4: Inclua canais indiretos (RAG, tools, multiagente), não só chat direto."
  - "Exceção: Sistemas só internos com dados sintéticos podem usar red team mais leve, ainda assim com registro."
```

---

## 🔗 3. Notas Relacionadas
- [[Guardrails]]
- [[Prompt-Injection]]
- [[Avaliacao-de-Agentes]]
- [[Observabilidade-de-IA]]
- [[HITL]]

## 📚 4. Fontes
- Ver `Fontes/Red-Teaming.md`.
- OWASP LLM Top 10 (enquadramento de riscos).
