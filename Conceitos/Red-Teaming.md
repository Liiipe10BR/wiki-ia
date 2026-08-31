---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Red Teaming", "Red team", "Avaliação adversarial", "Adversarial evaluation"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-31
confianca: 0.91
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #40; aprofundamento 2026-08-31 (processo, não exploits)"
---

# 🛡️ Red teaming

> **Resumo para Humanos:**
> Processo sistemático para **encontrar falhas de segurança e abuso** em LLMs e
> agentes *antes* (e depois) de confiar neles em produção — complementar a
> [[Avaliacao-de-Agentes]] de sucesso de tarefa.

---

## 📖 1. Contexto Humano (Narrativa)

Avaliação “feliz” pergunta: o agente completa a tarefa? **Red teaming**
pergunta: o que acontece se alguém *tentar* quebrar política, exfiltrar dados,
desviar tools ou injetar instruções via [[RAG]]?

### Escopo típico (sem detalhar exploits)

- Jailbreak / bypass de política de conteúdo
- [[Prompt-Injection]] direta e indireta (documento recuperado, e-mail, página)
- Uso indevido de [[Tool-Calling]] (argumentos maliciosos, over-scoping)
- Vazamento de system prompt, PII ou segredos
- Falhas de [[Guardrails]] e de [[HITL]] (aprovação social-engineered)

OWASP LLM Top 10 e guias de vendors **classificam riscos**; red team **testa**
se as mitigações aguentam. Esta nota **não** descreve como atacar sistemas.

### Manual vs automatizado

| Modo | Força | Fraqueza |
|------|--------|----------|
| Manual (especialistas) | Criatividade, contexto de negócio | Escala limitada |
| Automatizado (geradores, fuzzing de prompts) | Cobertura e regressão | Pode perder ataques novos |

O ideal em produção é **híbrido**: suite automatizada contínua + campanhas
manuais periódicas. Achados alimentam patches de policy, filtros, least
privilege e filas HITL — e entram em [[Observabilidade-de-IA]] como casos de
test.

### Relação com outras notas

- [[Prompt-Injection]] = *classe de ameaça*
- [[Guardrails]] = *controles*
- [[Avaliacao-de-Agentes]] = *sucesso/custo/trajetória*
- **Red teaming** = *processo adversarial* que tensiona os três

Divulgação responsável: documentar severidade e reprodução mínima **internamente**;
não publicar receitas de exploração no vault público.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Red teaming de LLMs e agentes"
relations:
  - is_a: "Processo de avaliação adversarial de segurança e abuso"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Prompt-Injection]]"
  - related_to: "[[Avaliacao-de-Agentes]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[HITL]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[RAG]]"
rules_of_thumb:
  - "Regra 1: Defina ameaças e ativos (dados, tools, usuários) antes de gerar casos."
  - "Regra 2: Inclua canais indiretos (RAG, tools, multiagente), não só o chat."
  - "Regra 3: Separe descoberta (red team) de mitigação (guardrails/HITL/patch)."
  - "Regra 4: Registre achados com severidade; sem tracking vira teatro de compliance."
  - "Regra 5: Não publique procedimentos operacionais de ataque em documentação pública."
  - "Exceção: Ambientes sintéticos isolados podem red-team de forma mais agressiva, ainda com registro."
```

---

## 🔗 3. Notas Relacionadas
- [[Guardrails]]
- [[Prompt-Injection]]
- [[Avaliacao-de-Agentes]]
- [[Observabilidade-de-IA]]
- [[HITL]]
- [[Tool-Calling]]
- [[RAG]]

## 📚 4. Fontes
- Ver `Fontes/Red-Teaming.md`.
- OWASP Top 10 for LLM Applications (taxonomia de risco).
