# Fontes — Cache Semântico

## [GPTCache: An Open-Source Semantic Cache for LLM Applications Enabling Faster Answers and Cost Savings](https://aclanthology.org/2023.nlposs-1.24/)
- Autor: Fu Bang
- Usada para: arquitetura clássica embedding → similaridade → hit/miss; motivação de custo e latência; ordem de magnitude de speedup em hits reportada no paper de demonstração.
- Data de acesso: 2026-08-30
- Confiabilidade: ACL Anthology, NLP-OSS 2023.

## [vCache: Verified Semantic Prompt Caching](https://arxiv.org/abs/2502.03771)
- Usada para: crítica a limiar estático global; cache semântico com garantia de taxa de erro definida pelo usuário; limiar adaptativo por entrada cacheada.
- Data de acesso: 2026-08-30
- Confiabilidade: arXiv:2502.03771 (aceito ICLR 2026, conforme comentário dos autores).

## [ContextCache: Context-Aware Semantic Cache for Multi-Turn Queries in Large Language Models](https://arxiv.org/abs/2506.22791)
- Usada para: falha do matching só na query isolada em diálogo multi-turn; necessidade de incorporar contexto conversacional no matching.
- Data de acesso: 2026-08-30
- Confiabilidade: arXiv:2506.22791.

## Observação de método
Nenhuma fonte inventada. GPTCache é tratado como referência histórica/open-source, não como padrão único de produção. Limiares, TTL e multi-turn são riscos de desenho, não detalhes de um produto.
