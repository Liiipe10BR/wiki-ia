---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Human-in-the-Loop", "HITL", "Humano no loop", "Aprovação humana", "Human review"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-31
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #36; aprofundamento 2026-08-31 com docs oficiais de human review / needsApproval"
---

# 👤 Human-in-the-Loop (HITL)

> **Resumo para Humanos:**
> Colocar um **humano no caminho crítico** do sistema — aprovar, rejeitar ou
> corrigir ações sensíveis de um [[Agente-de-IA]] — com interface, política e
> registro, não só com a frase “consulte um especialista” gerada pelo modelo.

---

## 📖 1. Contexto Humano (Narrativa)

Um agente que só gera texto raramente exige HITL formal. O risco sobe quando há
[[Tool-Calling]] com efeito no mundo: cancelar pedido, transferir valor, enviar
e-mail, alterar produção, invocar MCP com dados sensíveis. [[Guardrails]]
automáticos (input/output/tool) bloqueiam padrões conhecidos; **HITL** cobre o
que a política exige julgamento humano ou responsabilidade legal.

### O que é HITL de verdade

HITL operacional tem três peças:

1. **Ponto de interrupção** — a execução **pausa** antes (ou depois) de uma ação
2. **Canal humano** — UI, fila, ticket ou API onde alguém decide
3. **Retomada** — o runtime **aprova ou rejeita** e continua (ou aborta) com
   estado preservado

Sem (2) e (3), “o modelo pediu ajuda” é só texto.

### Padrões de inserção no pipeline

| Padrão | Quando | Custo típico |
|--------|--------|----------------|
| **Pré-aprovação** | Ação irreversível / financeira / PII / produção | Alta latência; alto controle |
| **Pós-revisão** | Volume alto; amostragem ou só exceções | Menor latência; risco residual |
| **Escalação condicional** | Confiança baixa, valor alto, domínio sensível | Depende da taxa de escalação |
| **Correção com feedback** | Humano edita saída; sistema registra | Útil para [[Avaliacao-de-Agentes]] |

Documentação de productização (ex.: OpenAI Agents SDK) formaliza **tool
approval**: tools com `needsApproval` interrompem o run; a aplicação chama
aprovar/rejeitar e retoma o estado. Guardrails automáticos e human review são
apresentados como controles **complementares**, não substitutos.

### O que medir

- Taxa de interrupção e tempo até decisão (SLA)
- Aprovações vs rejeições por tipo de tool
- Falsos positivos (humano bloqueia o correto) e falsos negativos (aprovou o
  errado)
- Timeout: **silêncio ≠ aprovação** — defina fallback explícito

[[Observabilidade-de-IA]] deve registrar *quem* decidiu, *sobre qual*
interruption e o payload da tool. Sem isso não há auditoria nem melhoria de
política.

### Limites

HITL não elimina [[Prompt-Injection]] nem substitui least privilege em tools.
Em [[Sistemas-Multiagente]], defina se a aprovação é por agente ou pelo
resultado agregado do time. HITL em excesso mata a automação; em falta, o
sistema age sem accountability.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Human-in-the-Loop em pipelines de agentes e LLMs"
relations:
  - is_a: "Padrão de controle humano com pausa, decisão e retomada"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[Avaliacao-de-Agentes]]"
  - related_to: "[[Prompt-Injection]]"
  - related_to: "[[Sistemas-Multiagente]]"
  - related_to: "[[Red-Teaming]]"
rules_of_thumb:
  - "Regra 1: Classifique tools por risco (irreversível, financeiro, PII, produção) e marque pré-aprovação por política, não por feeling do modelo."
  - "Regra 2: Timeout sem resposta humana nunca deve ser tratado como aprovação implícita."
  - "Regra 3: Persista interruptions e decisões (ator, timestamp, tool, args) para auditoria e avaliação."
  - "Regra 4: Combine guardrails automáticos (baratos, sempre ligados) com HITL (caros, seletivos)."
  - "Regra 5: Meça fila e SLA; HITL sem capacidade humana vira deadlock."
  - "Exceção: Ambientes só de pesquisa/demo sem efeito no mundo real podem operar sem HITL formal."
```

---

## 🔗 3. Notas Relacionadas
- [[Guardrails]]
- [[Agente-de-IA]]
- [[Tool-Calling]]
- [[Observabilidade-de-IA]]
- [[Avaliacao-de-Agentes]]
- [[Prompt-Injection]]
- [[Sistemas-Multiagente]]
- [[Red-Teaming]]

## 📚 4. Fontes
- Ver `Fontes/HITL.md`.
- OpenAI Agents SDK — Human in the loop / needsApproval.
- OpenAI API — Guardrails and human review.
