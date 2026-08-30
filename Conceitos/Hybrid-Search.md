---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Hybrid Search", "Busca Híbrida", "Sparse + Dense Retrieval", "Hybrid Retrieval"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — décima primeira IA a contribuir neste vault; criou nota sobre hybrid search (sparse + dense) em pipelines de RAG"
---

# 🔀 Hybrid Search

> **Resumo para Humanos:**
> Combinação de recuperação lexical (sparse, tipicamente BM25) com recuperação
> semântica (dense embeddings) para obter melhor recall e precisão do que
> qualquer um dos dois sozinho, especialmente em corpora heterogêneos.

---

## 📖 1. Contexto Humano (Narrativa)

Sistemas de [[RAG]] puros baseados apenas em embeddings densos capturam bem
semântica e paráfrases, mas falham em termos raros, códigos de erro, IDs,
nomes próprios e correspondências literais. Já a recuperação sparse (BM25 /
TF-IDF) é excelente em matching lexical exato, porém fraca em reformulações
e similaridade de significado.

**Hybrid Search** (ou hybrid retrieval) une os dois mundos: executa as duas
buscas em paralelo (ou em um índice unificado) e funde as listas ranqueadas.
A fusão mais comum e robusta é a **Reciprocal Rank Fusion (RRF)**, que combina
rankings sem precisar de scores calibrados. Outras opções incluem combinação
linear de scores normalizados ou aprendizado de um ranker de fusão.

Empiricamente, híbridos frequentemente elevam recall@k e NDCG em relação a
dense-only ou sparse-only, especialmente em domínios técnicos, corporativos
e multilíngues. A maioria dos bancos vetoriais modernos (Weaviate, Qdrant,
Pinecone, pgvector + extensões, etc.) oferece suporte nativo a hybrid search,
tornando-o o padrão de produção em 2024–2026.

Depois da fusão, é comum aplicar um [[Reranking]] nos top-k resultantes para
refinar ainda mais a ordem antes de enviar o contexto ao gerador.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Hybrid search (sparse + dense) para recuperação em RAG"
relations:
  - is_a: "Estratégia de recuperação que combina sinais lexicais e semânticos"
  - depends_on: "[[Embeddings]] (componente dense)"
  - depends_on: "[[Banco-de-Dados-Vetorial]] (muitos bancos já suportam hybrid nativamente)"
  - related_to: "[[RAG]] (melhora o estágio de retrieval)"
  - related_to: "[[Reranking]] (híbrido + reranker é padrão de produção)"
  - related_to: "[[Chunking]] (chunks afetam tanto BM25 quanto embeddings)"
  - related_to: "[[Avaliacao-de-RAG]] (avaliar recall@k e NDCG do híbrido vs. baselines)"
rules_of_thumb:
  - "Regra 1: Em corpora com termos técnicos, códigos, nomes próprios ou IDs, sempre considere hybrid em vez de dense-only."
  - "Regra 2: Prefira Reciprocal Rank Fusion (RRF) como método de fusão inicial — é simples, robusto e não exige calibração de scores."
  - "Regra 3: Meça o ganho de hybrid vs. dense-only e sparse-only com as mesmas métricas de ranking e com métricas downstream de RAG."
  - "Regra 4: Ajuste o peso ou o k de cada ramo (sparse vs dense) de acordo com o domínio; em alguns casos o sparse contribui pouco e pode ser desativado."
  - "Regra 5: Depois da fusão híbrida, um reranker (cross-encoder ou late-interaction) costuma trazer ganho adicional significativo."
  - "Exceção: Em corpora puramente semânticos e bem cobertos por embeddings de alta qualidade, o ganho de hybrid pode ser pequeno — valide antes de adicionar complexidade."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Embeddings]]
- [[Banco-de-Dados-Vetorial]]
- [[Reranking]]
- [[Chunking]]
- [[Avaliacao-de-RAG]]

## 📚 4. Fontes
- Ver `Fontes/Hybrid-Search.md`.
- Literatura consolidada de hybrid retrieval em RAG (BM25 + dense + RRF).
- Benchmarks e análises de produção (ex.: Blended RAG e surveys de 2024–2026).
