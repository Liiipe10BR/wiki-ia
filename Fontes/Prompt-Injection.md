# Fontes — Prompt-Injection

## [OWASP Top 10 for Large Language Model Applications — LLM01: Prompt Injection](https://genai.owasp.org/)
- Também: [LLM01_PromptInjection.md (repositório oficial)](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM01_PromptInjection.md)
- Usada para: definição de prompt injection; distinção direto vs indireto; reconhecimento de que RAG e fine-tuning não eliminam a vulnerabilidade; estratégias de mitigação (não eliminação).
- Data de acesso: 2026-08-30
- Confiabilidade: padrão de indústria OWASP (LLM Top 10 2025 / atualizações GenAI).

## [Model Context Protocol — Security and Trust & Safety](https://modelcontextprotocol.io/specification/2026-07-28)
- Usada para: princípios de consentimento do usuário, privacidade de dados e **tool safety** (tools como execução arbitrário; anotações de tool não confiáveis por padrão; consentimento antes de invocar tool).
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial da especificação MCP.

## [Authorization Security Considerations (MCP)](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations)
- Usada para: requisitos de segurança em clientes/servidores MCP (tokens, audience binding, comunicação segura) — reforça que segurança é responsabilidade da implementação, não só do protocolo de tools.
- Data de acesso: 2026-08-30
- Confiabilidade: especificação oficial MCP.

## [Rag ’n Roll: An End-to-End Evaluation of Indirect Prompt Manipulations in LLM-based Application Frameworks](https://arxiv.org/abs/2408.05025)
- Autores: De Stefano, Schönherr, Pellegrino (CISPA)
- Usada para: evidência de que injeção indireta em pipelines RAG completos é um problema de configuração e avaliação end-to-end, não só de prompt isolado.
- Data de acesso: 2026-08-30
- Confiabilidade: paper arXiv:2408.05025 (segurança de sistemas).

## Observação de método
Nenhuma fonte inventada. A nota não afirma que qualquer controle elimina o risco; alinha-se a OWASP (mitigar impacto) e à especificação MCP (consentimento e tool safety no host).
