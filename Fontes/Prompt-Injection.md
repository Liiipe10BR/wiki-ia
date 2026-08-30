# Fontes — Prompt-Injection

## [OWASP LLM01:2025 Prompt Injection](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM01_PromptInjection.md)
- Usada para: definição de prompt injection; distinção direto vs. indireto; afirmação de que RAG e fine-tuning não eliminam a vulnerabilidade; relação com jailbreak.
- Data de acesso: 2026-08-30
- Confiabilidade: documento oficial do OWASP Top 10 for LLM Applications (edição 2025 / v2.0). Página canônica do projeto: [genai.owasp.org](https://genai.owasp.org/).

## [Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- Autores: Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz
- Usada para: canal de injeção indireta em aplicações que recuperam ou integram conteúdo externo (web, e-mail, documentos).
- Data de acesso: 2026-08-30
- Confiabilidade: preprint arXiv:2302.12173 (2023); referência acadêmica padrão para XPIA / injeção indireta.

## [NIST AI 100-2e2025 — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://doi.org/10.6028/NIST.AI.100-2e2025)
- Autores: Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin (NIST Trustworthy and Responsible AI)
- Usada para: taxonomia governamental que separa prompt injection (NISTAML.018) e indirect prompt injection (NISTAML.015) em violações de disponibilidade, integridade e privacidade em GenAI.
- Data de acesso: 2026-08-30
- Confiabilidade: relatório oficial NIST, publicado em março de 2025; DOI 10.6028/NIST.AI.100-2e2025.

## [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices)
- Usada para: controles obrigatórios do protocolo (validação de token/audiência, não usar sessão como autenticação, consentimento) e para o ponto de que "LLM invocando tool inesperada" é controle de aplicação, não falha da especificação.
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial da especificação MCP (revisão 2025-06-18). Há revisões posteriores da spec; o princípio (responsabilidade de cliente/servidor/operador) permanece.

## [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)
- Usada para: menor privilégio por servidor/tool, inspeção de schemas (tool description como superfície de injeção), sandbox, validação de inputs/outputs, aprovação humana para chamadas sensíveis, não auto-aprovar tools.
- Data de acesso: 2026-08-30
- Confiabilidade: OWASP Cheat Sheet Series (página pública verificada em 2026-08-30).

## Observação de método
Nenhuma fonte inventada. A nota não afirma que filtro, schema, HITL ou MCP eliminam o risco; as próprias fontes descrevem mitigação parcial e responsabilidade compartilhada.
Divergência registrada: a numeração OWASP "LLM Top 10 2026" aparece em páginas do projeto GenAI, mas a ficha canônica consultada para LLM01 continua rotulada **LLM01:2025**. A substância (direto vs. indireto; RAG não elimina) é a mesma.
