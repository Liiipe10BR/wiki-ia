# Fontes — Guardrails

## [Guardrails — OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/guardrails/)
- Usada para: distinção input / output / tool guardrails; tripwire; execução paralela vs. bloqueante; fronteiras do workflow (input só no primeiro agente da cadeia, output só no final).
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial do SDK.

## [Guardrails — OpenAI Agents SDK (JS)](https://openai.github.io/openai-agents-js/guides/guardrails/)
- Usada para: mesma taxonomia em outra implementação oficial; `runInParallel: false` para não gastar o modelo caro.
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial.

## [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674)
- Autores: Hakan Inan et al. (Meta GenAI)
- Usada para: safeguard de entrada/saída baseado em LLM; taxonomia de risco; classificação de prompt e de resposta.
- Data de acesso: 2026-08-30
- Confiabilidade: paper arXiv:2312.06674 (dez/2023).

## [OWASP Top 10 for LLM Applications 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- Usada para: LLM01 Prompt Injection; LLM05 Improper Output Handling (tratar saída do modelo como não confiável); LLM06 Excessive Agency (funcionalidade, permissão e autonomia excessivas; HITL e menor privilégio).
- Data de acesso: 2026-08-30
- Confiabilidade: documento comunitário OWASP; PDF v2025 em genai.owasp.org.

## [OWASP GenAI LLM Top 10 2026](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10)
- Usada para: registrar reordenação (Excessive Agency sobe a LLM03:2026; Unbounded Consumption; Improper Output Handling como LLM10:2026). Não tratar um único número de ID como estável entre edições.
- Data de acesso: 2026-08-30
- Confiabilidade: repositório canônico do projeto OWASP GenAI; release de 4 ago 2026.

## [NIST AI 600-1 — Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)
- Usada para: enquadrar guardrails como ações de gestão de risco (Govern, Map, Measure, Manage) e riscos de GenAI (conteúdo nocivo, injeção, confabulação, privacidade), não como garantia técnica única.
- Data de acesso: 2026-08-30
- Confiabilidade: publicação NIST, jul/2024.

## [Guardrails and controls overview — Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/guardrails/guardrails-overview)
- Usada para: definição operacional (guardrail = coleção de controles); pontos de intervenção (user input, tool call, tool response, output).
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial Microsoft; agent guardrails em preview na data da verificação.

## Observação de método
Nenhuma fonte inventada. Divergência menor de rotulagem: IDs OWASP 2025 ≠ 2026 para o mesmo risco (ex.: Excessive Agency é LLM06:2025 e LLM03:2026). A nota de conceito usa o *nome* do risco e cita as duas edições.

Prompt injection é tratado aqui só como pressão sobre guardrails. A nota `Conceitos/Prompt-Injection.md` ainda não está em `main` (PRs #9, #10 e #11 da Issue #8); esta contribuição não a duplica.
