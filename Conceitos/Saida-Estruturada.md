---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Saída Estruturada", "Structured Output", "JSON Schema", "Constrained decoding"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #38 / saída estruturada e constrained decoding"
---

# 📐 Saída estruturada

> **Resumo para Humanos:**
> Fazer o modelo gerar texto que **obedece a um schema** (em geral JSON) de
> forma confiável — para APIs, [[Tool-Calling]] e pipelines que quebram com
> vírgula a mais.

---

## 📖 1. Contexto Humano (Narrativa)

Pedir “responda em JSON” no prompt **não garante** JSON válido. **Saída
estruturada** usa *constrained decoding* (ou modo equivalente): a amostragem
só permite tokens compatíveis com o schema (ex.: JSON Schema convertido em
gramática).

A OpenAI documentou **Structured Outputs** na API (ago/2024): com
`response_format` + `json_schema` e modo estrito, a saída deve aderir ao
schema fornecido. Outros provedores expõem mecanismos semelhantes. Isso é
diferente de validar *depois* e pedir “tente de novo”.

Ainda assim: schema incompleto, enums ruins ou campos ambíguos geram JSON
*válido* e semanticamente errado. [[Guardrails]] e validação de negócio
continuam necessários. Em agentes, structured output estabiliza argumentos de
tools e estados intermediários — complemento de [[Engenharia-de-Prompts]], não
substituto.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Saída estruturada e constrained decoding para LLMs"
relations:
  - is_a: "Garantia (ou quase) de aderência a schema na geração"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[Alucinacao]]"
rules_of_thumb:
  - "Regra 1: Prefira schema estrito na API a 'por favor responda em JSON' no prompt."
  - "Regra 2: Valide semântica de negócio além da sintaxe (campo presente ≠ valor correto)."
  - "Regra 3: Versionar schemas; mudança silenciosa quebra clientes e tools."
  - "Regra 4: Em tool-calling, alinhe o schema da tool ao da saída intermediária."
  - "Exceção: Prosa livre para UX final pode coexistir com structured output só na camada de integração."
```

---

## 🔗 3. Notas Relacionadas
- [[Tool-Calling]]
- [[Engenharia-de-Prompts]]
- [[Guardrails]]
- [[Agente-de-IA]]
- [[Alucinacao]]

## 📚 4. Fontes
- Ver `Fontes/Saida-Estruturada.md`.
- OpenAI, Introducing Structured Outputs in the API (2024).
