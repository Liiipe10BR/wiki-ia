# Fontes — Chunking

## [Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models](https://arxiv.org/abs/2409.04701)
- Usada para: técnica de “late chunking” (embutir o documento inteiro primeiro e depois agregar por chunk), mostrando que chunking não é só corte pré-embedding; melhora recall em documentos com referências cruzadas.
- Data de acesso: 2026-08-29
- Confiabilidade: paper arXiv 2024 (Jina AI et al.), validado empiricamente e adotado por embedders de contexto longo.

## Práticas e avaliações sistemáticas de chunking em RAG (2025–2026)
- Usada para: trade-offs de tamanho de chunk, overlap, estratégias fixed / sentence / semantic / recursive / parent-document; confirmação de que chunking estrutural ou por sentença costuma superar fixed-size cego em corpora com estrutura, e de que overlap tem benefício misto (às vezes nulo em benchmarks recentes).
- Referências representativas:
  - “A Systematic Analysis of Chunking Strategies for Reliable Question Answering” (avaliação end-to-end com SPLADE + gerador; overlap sem benefício mensurável em seu setup).
  - Avaliações cross-domain de 36 métodos de segmentação (paragraph-group e content-aware superando fixed-length).
  - Guias de engenharia (LangChain recursive character, parent-document retrieval, hierarchical/RAPTOR).
- Data de acesso: 2026-08-29
- Confiabilidade: literatura de engenharia + papers de avaliação; não há um único paper “fundador” do conceito — chunking é prática consolidada de pipelines de RAG desde a adoção ampla de embeddings densos.
