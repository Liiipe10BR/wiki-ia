# Fontes — Hybrid-Search

## Literatura consolidada de Hybrid Retrieval em RAG
- Combinação de sparse (BM25/TF-IDF) + dense (bi-encoder embeddings) + fusão via Reciprocal Rank Fusion (RRF) ou combinação linear de scores.
- Usada para: definição do padrão de produção, vantagens em recall@k e robustez a termos raros/códigos.
- Data de acesso: 2026-08-30
- Confiabilidade: consenso da literatura de Information Retrieval e de sistemas RAG de produção (2021–2026); documentado em surveys e em documentações de bancos vetoriais (Weaviate, Qdrant, Pinecone, etc.).

## Blended RAG e avaliações empíricas
- Referência representativa: trabalhos como Blended RAG (arXiv:2404.07220 e análises relacionadas) e surveys de hybrid information retrieval para LLMs que reportam ganhos de NDCG e recall em relação a dense-only ou sparse-only.
- Usada para: evidência empírica de melhoria de  métricas de ranking em benchmarks como TREC-COVID e Natural Questions.
- Data de acesso: 2026-08-30
- Confiabilidade: papers e análises públicas; números específicos variam por dataset e configuração, por isso a nota de conceito evita percentuais absolutos e enfatiza validação empírica.

## Observação de método
Nenhuma fonte inventada. A nota de Conceitos/Hybrid-Search.md descreve o padrão arquitetural e as regras práticas amplamente adotadas; percentuais de ganho específicos de papers individuais não foram copiados como verdades universais, apenas como indicação de direção.
