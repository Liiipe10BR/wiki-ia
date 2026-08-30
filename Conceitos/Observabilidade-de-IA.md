---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Observabilidade", "Tracing", "LLM Observability", "Observabilidade de IA", "Observabilidade e Tracing"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — nota sobre observabilidade e tracing de aplicações de IA (Issue #14)"
---

# 📊 Observabilidade de IA

> **Resumo para Humanos:**
> Registrar, correlacionar e analisar o caminho de uma requisição em sistemas
> de IA — prompts, modelo, tokens, latência, recuperação, ferramentas,
> erros e avaliações — sem tratar o conteúdo das conversas como log público.

---

## 📖 1. Contexto Humano (Narrativa)

Observabilidade clássica (métricas, logs e traces distribuídos) não basta
sozinha para um [[Agente-de-IA]] ou um pipeline de [[RAG]]. O caminho de uma
requisição inclui chamadas de modelo, recuperação de documentos, [[Tool-Calling]],
retries e, muitas vezes, avaliação humana ou automática. Sem um *trace*
árvore, falhas viram "o modelo errou" — sem saber *em qual passo*.

O padrão técnico de referência é o **OpenTelemetry**. As
[convenções semânticas GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
definem spans e atributos `gen_ai.*` (operação, provedor, modelo, tokens,
instruções, mensagens de entrada/saída, execução de ferramenta). O status
documentado em 2026 ainda é **Development**: instrumentações antigas não
devem mudar o schema emitido por padrão sem um opt-in de estabilidade.
Há também convenções específicas para agentes e para [[Model-Context-Protocol]].

**OpenInference** (Arize) é uma convenção complementar sobre OTLP: cada span
carrega `openinference.span.kind` (`LLM`, `RETRIEVER`, `RERANKER`, `TOOL`,
`AGENT`, `EMBEDDING`, `CHAIN`, `GUARDRAIL`, `EVALUATOR`, `PROMPT`). A spec
também define flags para *esconder* inputs, outputs e parâmetros — o
reconhecimento explícito de que o conteúdo do prompt é dado sensível.

O que registrar, na prática (alinhado à Issue #14):

- **Prompt e versão de instrução** — hash ou ID de template, não
  necessariamente o texto integral em produção.
- **Modelo e provedor** — `gen_ai.request.model`, `gen_ai.provider.name`.
- **Tokens, latência e custo** — usage de input/output e duração da operação;
  custo é derivado de tabela de preços, não um campo estável único no OTel.
- **Documentos recuperados** — IDs, ranks, scores; texto só com política de
  retenção (liga a [[RAG]] e [[Avaliacao-de-RAG]]).
- **Chamadas de ferramentas** — nome, argumentos validados, resultado,
  latência e erro (liga a [[Tool-Calling]]).
- **Erros, recusas e retries** — `error.type`, status do span, número de
  tentativas; recusa de safety é evento distinto de timeout de API.
- **Avaliações e feedback humano** — span `EVALUATOR` ou evento posterior
  ligado ao `trace_id` / `gen_ai.conversation.id`.

Risco de privacidade: gravar conversas completas replica PII, segredos e
dados de terceiros num backend de telemetria. A OWASP LLM02:2025 (*Sensitive
Information Disclosure*) trata exposição de informação sensível no contexto
da aplicação LLM. A própria spec OTel GenAI alerta que atributos de
conteúdo (instruções, mensagens, resultado de tool) podem ser sensíveis e
sugere armazenar o payload fora do span (referência/URI) quando volume ou
regulação exigirem. Isso se conecta a [[Proveniencia-de-Dados]]: o trace é
cadeia de evidência operacional, não um dump irrestrito do contexto.

Divergência registrada, não resolvida: o ecossistema ainda convive com
atributos antigos (`gen_ai.prompt` / `gen_ai.completion`) e o schema mais
novo (`gen_ai.input.messages` / `gen_ai.output.messages`). Backends e
libraries não são intercambiáveis só porque todos "falam OTel".

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Observabilidade e tracing de aplicações e agentes de IA"
relations:
  - is_a: "Prática de telemetria específica para sistemas GenAI"
  - depends_on: "[[Agente-de-IA]] (o loop thought-action-observation é o que o trace reconstrói)"
  - related_to: "[[Tool-Calling]] (cada tool vira span filho com args, resultado e erro)"
  - related_to: "[[RAG]] (retriever e documentos citados são spans/atributos próprios)"
  - related_to: "[[Avaliacao-de-RAG]] (notas de qualidade devem ligar ao mesmo trace_id)"
  - related_to: "[[Proveniencia-de-Dados]] (trace preserva cadeia operacional; não substitui proveniência do corpus)"
  - related_to: "[[Model-Context-Protocol]] (OTel define convenções mcp.* além de gen_ai.*)"
  - related_to: "[[Alucinacao]] (trace de retrieval + geração é evidência para classificar falha)"
rules_of_thumb:
  - "Regra 1: Use um trace_id por turno/requisição e spans filhos para LLM, retrieval, tool, embedding e avaliação."
  - "Regra 2: Grave modelo, operação, tokens e latência em todo span de inferência; sem isso não há custo nem SLO."
  - "Regra 3: Versionar prompts/instruções (ID ou hash) é obrigatório; o texto integral é opcional e deve respeitar política de retenção."
  - "Regra 4: Não envie PII, segredos ou documentos regulados para o backend de traces sem redação, hashing ou armazenamento separado."
  - "Regra 5: Correlacione avaliação e feedback humano ao mesmo identificador de conversa/trace; avaliação órfã não fecha o ciclo."
  - "Regra 6: Trate recusa de safety, timeout, argumento inválido de tool e alucinação de API como classes de erro distintas."
  - "Exceção: Em protótipo local de baixo risco, gravar input/output completos acelera o debug — desde que esses traces não virem dataset de treino nem saiam da máquina."
```

---

## 🔗 3. Notas Relacionadas
- [[Agente-de-IA]]
- [[Tool-Calling]]
- [[RAG]]
- [[Avaliacao-de-RAG]]
- [[Proveniencia-de-Dados]]
- [[Model-Context-Protocol]]
- [[Alucinacao]]

## 📚 4. Fontes
- Ver `Fontes/Observabilidade-de-IA.md`.
- OpenTelemetry Semantic Conventions for Generative AI (status Development).
- OpenInference specification (Arize), incluindo configuração de redaction.
- OWASP LLM02:2025 Sensitive Information Disclosure.
