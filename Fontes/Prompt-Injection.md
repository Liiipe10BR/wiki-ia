# Fontes — Prompt-Injection

## [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- Usada para: definição de prompt injection; distinção direto/indireto; cenário de documento alterado em RAG; mitigations (menor privilégio, HITL, segregação de conteúdo externo); afirmação de que RAG e fine-tuning não eliminam a vulnerabilidade.
- Data de acesso: 2026-08-30
- Confiabilidade: documento comunitário canônico do OWASP GenAI Security Project.

## [OWASP GenAI LLM Top 10 2026 (repositório oficial)](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10)
- Usada para: LLM01:2026 permanece Prompt Injection; Excessive Agency sobe para LLM03:2026 — contexto de risco agentic.
- Data de acesso: 2026-08-30
- Confiabilidade: publicação oficial do projeto OWASP (release 2026, 4 de agosto de 2026).

## [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- Autores: Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz
- Usada para: formalização de injeção indireta; payload em dados recuperados (web, arquivos) sem o atacante falar com o modelo; taxonomia de impactos.
- Data de acesso: 2026-08-30
- Confiabilidade: paper arXiv:2302.12173; versão em *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security* (AISec 2023).

## [NIST AI 100-2e2025 — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://doi.org/10.6028/NIST.AI.100-2e2025)
- Usada para: IDs NISTAML de prompt injection e indirect prompt injection; distinção entre ataque direto no canal do usuário e indireto via terceiro.
- Data de acesso: 2026-08-30
- Confiabilidade: relatório oficial NIST (edição 2025).

## [MCP Security Best Practices (documentação oficial)](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices)
- Usada para: MCP não implica ferramenta segura; riscos de confused deputy, token passthrough e SSRF; consentimento e validação de tokens.
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial do Model Context Protocol.

## [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)
- Usada para: tratar parâmetros e retornos de tool como untrusted; não autoaprovar tool calls; validar input/output; HITL; isolamento entre servidores MCP.
- Data de acesso: 2026-08-30
- Confiabilidade: OWASP Cheat Sheet Series.

## Observação de método
Nenhuma fonte inventada. A nota afirma explicitamente que mitigations reduzem impacto e não eliminam o risco — alinhado a OWASP LLM01 ("it is unclear if there are fool-proof methods of prevention").
