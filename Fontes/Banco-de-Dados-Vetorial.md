# Fontes — Banco de Dados Vetorial

## HNSW (Hierarchical Navigable Small World)
- Trabalho original: Malkov, Y. A., & Yashunin, D. A. (2018/2020). "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs". *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
- Usado para: descrição do índice grafo-hierárquico, comportamento de recall/latência e popularidade como default em produção.
- Confiabilidade: paper revisado por pares, base teórica amplamente citada e implementada (hnswlib, Faiss, etc.).

## IVF / Product Quantization
- Jégou, H., Douze, M., & Schmid, C. (2011). "Product Quantization for Nearest Neighbor Search". *IEEE TPAMI*.
- Usado para: base do IVF + compressão PQ; trade-off memória vs. precisão.
- Confiabilidade: paper clássico de IR/ANN, fundação de muitas implementações (Faiss IVF-PQ etc.).

## Ecossistema de produtos (contexto histórico e estado da arte ~2021–2026)
- Documentação e histórias oficiais/públicas de Pinecone (fundado 2019, launch público ~2021), Weaviate, Milvus/Zilliz (desenvolvimento desde ~2018–2019), Qdrant, Chroma e pgvector (PostgreSQL extension, 2021).
- Comparações e análises de mercado (ex.: Superlinked Vector DB Comparison, artigos técnicos sobre HNSW vs IVF em produção).
- Usado para: lista de ferramentas típicas, tendência de comoditização (bancos tradicionais adicionando suporte a vetores) e recomendações práticas de quando usar HNSW vs IVF.
- Data de acesso das referências consolidadas: 2026-08-28.
- Confiabilidade: documentação de produto + análises técnicas públicas; não é paper único, mas consenso observável do ecossistema.

## Hybrid search / filtros de metadado
- Prática padrão documentada em docs oficiais (ex.: Supabase, Qdrant, Weaviate, Pinecone) e implementações de RRF / score fusion.
- Usado para: afirmação de que busca vetorial pura raramente basta em produção e da importância de filtros + lexical.
