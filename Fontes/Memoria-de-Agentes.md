# Fontes — Memória de Agentes

## [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)
- Autores: Charles Packer et al. (UC Berkeley)
- Usada para: hierarquia de memória (in-context vs out-of-context); analogia com SO; virtual context management; self-editing via tools; multi-session chat e análise de documentos longos.
- Data de acesso: 2026-08-30
- Confiabilidade: paper arXiv:2310.08560 (out/2023, rev. 2024).

## [Agent memory & architecture — Letta Docs](https://docs.letta.com/guides/agents/architectures/memgpt)
- Usada para: vocabulário operacional core memory / recall / archival; tools de edição (`memory_insert`, `memory_replace`, `memory_rethink`) e busca; relação explícita paper MemGPT ↔ produto Letta.
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial do projeto sucessor open-source do MemGPT.

## [Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)
- Autor: Pengfei Du
- Usada para: formalização write–manage–read; taxonomia temporal / substrato / política de controle; cinco famílias de mecanismo (compressão no contexto, stores com retrieval, reflexão, contexto virtual hierárquico, políticas aprendidas); limites de avaliação e desafios abertos (consolidação, forgetting, privacidade).
- Data de acesso: 2026-08-30
- Confiabilidade: survey arXiv:2603.07670 (mar/2026).

## [A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents](https://arxiv.org/abs/2602.06052)
- Autores: Wei-Chieh Huang et al.
- Usada para: eixos substrato (paramétrico vs externo), mecanismo cognitivo (working / episódica / semântica / procedural) e sujeito (usuário vs agente); memória como suporte a self-evolution em horizontes longos; aceito em TMLR com Survey Certification (conforme comentário dos autores no arXiv).
- Data de acesso: 2026-08-30
- Confiabilidade: survey arXiv:2602.06052 (2026; v4 ago/2026).

## Observação de método
Nenhuma fonte inventada. A nota **não** trata MemGPT/Letta como único padrão de mercado; usa-os como referência histórica e operacional clara da hierarquia in-context vs archival. Surveys de 2026 sustentam a taxonomia e os limites (avaliação multi-sessão, consolidação, privacidade).

Memória de agente ≠ [[RAG]] de corpus documental: overlap de infraestrutura é real; o ciclo de escrita e a política de estado são o critério de separação usado na nota de conceito.
