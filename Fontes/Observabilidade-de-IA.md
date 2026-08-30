# Fontes — Observabilidade-de-IA

## [Semantic conventions for generative AI systems (OpenTelemetry)](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- Usada para: status Development das convenções; sinais (events, exceptions, metrics, model spans, agent spans); existência de convenções por provedor e para MCP; plano de transição `OTEL_SEMCONV_STABILITY_OPT_IN`.
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial do projeto OpenTelemetry / semantic conventions. Status explícito: Development (não Stable).

## [GenAI model spans (semantic-conventions-genai)](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md)
- Usada para: spans de chamada a modelo; nome `{gen_ai.operation.name} {gen_ai.request.model}`; atributos de operação, modelo, mensagens, tools; aviso de que resultados de tool e conteúdo de prompt podem ser sensíveis; opção de gravar payload fora do span.
- Data de acesso: 2026-08-30
- Confiabilidade: repositório oficial de convenções GenAI do OpenTelemetry.

## [OpenInference specification](https://github.com/Arize-ai/openinference/blob/main/spec/README.md)
- Usada para: taxonomia `openinference.span.kind` (LLM, RETRIEVER, TOOL, AGENT, EVALUATOR, etc.); traces como árvore OTLP com significado de pipeline de IA.
- Data de acesso: 2026-08-30
- Confiabilidade: especificação pública do projeto OpenInference (Arize); complementar ao OTel, não substitui o padrão CNCF.

## [OpenInference configuration (redaction)](https://github.com/Arize-ai/openinference/blob/main/spec/configuration.md)
- Usada para: flags `OPENINFERENCE_HIDE_INPUTS` / `HIDE_OUTPUTS` / hide de mensagens, tools e embeddings — evidência de que o ecossistema trata prompt/completion como dado sensível.
- Data de acesso: 2026-08-30
- Confiabilidade: mesma spec OpenInference.

## [OWASP LLM02:2025 Sensitive Information Disclosure](https://genai.owasp.org/llmrisk/llm02-insecure-output-handling/)
- Usada para: risco de exposição de PII, dados de negócio e credenciais no contexto de aplicações LLM — aplicável a backends de trace que armazenam conversas.
- Data de acesso: 2026-08-30
- Confiabilidade: OWASP Gen AI Security Project, Top 10 for LLM Applications 2025.
- Observação: o slug da URL histórica (`llm02-insecure-output-handling`) não coincide com o título atual da página (Sensitive Information Disclosure). O número LLM02:2025 e o título da página em 2026-08-30 são os usados na nota.

## Observação de método
Nenhuma fonte inventada. Custo por token não é atributo estável único no OTel; a nota trata custo como derivado. Convenções GenAI permanecem em Development — a nota não afirma estabilidade do schema.
