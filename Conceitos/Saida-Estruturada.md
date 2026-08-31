---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Saída Estruturada", "Structured Output", "JSON Schema", "Constrained decoding", "JSON mode"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-31
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #38; aprofundamento 2026-08-31 (constrained decoding vs prompt-only JSON)"
---

# 📐 Saída estruturada

> **Resumo para Humanos:**
> Garantir (ou aproximar) que a geração **obedeça a um schema** — em geral JSON
> Schema — para integração com APIs, [[Tool-Calling]] e pipelines que quebram
> com texto “quase JSON”.

---

## 📖 1. Contexto Humano (Narrativa)

Sistemas agentic passam dados entre modelos, tools e serviços. Se a saída for
prosa livre, o próximo estágio precisa de parsers frágeis. **Saída estruturada**
restringe o espaço de geração.

### Três níveis (do frágil ao forte)

1. **Prompt-only** — “responda só em JSON”. Barato; **não garante** validade.
2. **Validação pós-hoc** — gera → valida schema → retry. Melhor; ainda pode
   loopar e gastar tokens.
3. **Constrained decoding** — em cada passo, só tokens compatíveis com o schema
   (ex.: JSON Schema → gramática). A OpenAI descreve Structured Outputs assim:
   `response_format` com `json_schema` e modo estrito; amostragem deixa de ser
   livre no vocabulário inteiro.

### Por que importa para agentes

- Argumentos de tool previsíveis
- Estado intermediário serializável
- Contratos entre agentes em [[Sistemas-Multiagente]]
- Menos falhas de parse em produção

### O que structured output **não** resolve

- Schema válido com **valor semanticamente errado** (data inventada, id errado)
- [[Alucinacao]] de conteúdo dentro de campos string
- Política de segurança — ainda precisa [[Guardrails]]
- Schema mal desenhado (enums incompletos, campos opcionais demais)

Boa prática: versionar schemas; tratar mudança como breaking change; testar com
casos limite (strings com aspas, unicode, campos vazios). Combinar com
[[Engenharia-de-Prompts]] para preencher *bem* o schema, não só para “caber” nele.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Saída estruturada e constrained decoding"
relations:
  - is_a: "Restrição de geração a um schema formal"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[Sistemas-Multiagente]]"
rules_of_thumb:
  - "Regra 1: Prefira schema estrito na API a 'responda em JSON' só no prompt."
  - "Regra 2: Valide negócio além da sintaxe (tipos certos ≠ política cumprida)."
  - "Regra 3: Versionar e documentar schemas; breaking changes quebram agents e clientes."
  - "Regra 4: Alinhe schema de tool ao schema de saída intermediária do agente."
  - "Regra 5: Reserve prosa livre para UX final; mantenha structured na camada de integração."
  - "Exceção: Prototipagem rápida pode começar com prompt-only JSON até estabilizar o contrato."
```

---

## 🔗 3. Notas Relacionadas
- [[Tool-Calling]]
- [[Engenharia-de-Prompts]]
- [[Guardrails]]
- [[Agente-de-IA]]
- [[Alucinacao]]
- [[Sistemas-Multiagente]]

## 📚 4. Fontes
- Ver `Fontes/Saida-Estruturada.md`.
- OpenAI, Introducing Structured Outputs in the API (2024).
