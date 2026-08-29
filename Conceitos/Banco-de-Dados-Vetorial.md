---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Banco de Dados Vetorial", "Vector Database", "Vector Store", "Vector DB"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-28
confianca: 0.92
embedding_prioritario: false
contribuido_por: "Claude (Anthropic) — nota original; Grok (xAI) — revisão profunda e expansão (índices HNSW/IVF, trade-offs, fontes reais, hybrid search)"
---

# 🧠 Banco de Dados Vetorial

> **Resumo para Humanos:**
> Um banco de dados feito pra guardar [[Embeddings]] e buscar rápido "o que
> é matematicamente parecido com isto aqui", em vez de "o que bate com esta
> palavra exata". É a infraestrutura que torna [[RAG]] viável em escala.

---

## 📖 1. Contexto Humano (Narrativa)

Banco de dados relacional clássico busca por igualdade ou faixa (`WHERE id = 5`
ou `price BETWEEN 10 AND 20`). Banco vetorial busca por *proximidade* num
espaço de centenas ou milhares de dimensões: dado um vetor de consulta
(geralmente o embedding de uma pergunta), ele encontra os vetores mais
próximos já armazenados.

Busca exata (k-NN) em alta dimensão é computacionalmente cara demais em
escala. Por isso quase todos os sistemas de produção usam **ANN
(Approximate Nearest Neighbor)** — índices que aceitam uma pequena perda
controlada de recall em troca de latência ordens de magnitude menor.

É a peça de infraestrutura que faz [[RAG]] funcionar em produção: sem um
jeito eficiente de guardar e recuperar embeddings, cada consulta teria que
comparar contra todo o dataset na força bruta.

### Índices principais

Dois algoritmos dominam a prática:

- **HNSW (Hierarchical Navigable Small World)** — grafo hierárquico de
  proximidade. Alta recall "out of the box", boa com dados dinâmicos
  (inserts/updates frequentes), mas consome mais memória (tipicamente
  2–5× o tamanho dos vetores brutos). É o default em Qdrant, Weaviate,
  Pinecone, pgvector e a maioria dos sistemas modernos.
- **IVF (Inverted File Index)** — particiona o espaço com k-means em
  clusters. Na consulta, só procura nos clusters mais próximos (`nprobe`).
  Mais eficiente em memória e construção mais rápida, mas a recall depende
  fortemente de tuning e o índice "envelhece" com inserts (precisa de
  rebuild periódico em muitos casos). Variantes comuns: IVF-Flat, IVF-PQ
  (com Product Quantization para compressão).

### Ferramentas típicas (2021–2026)

- **Nativos dedicados**: Pinecone (managed, 2019), Weaviate, Milvus/Zilliz,
  Qdrant, Chroma.
- **Extensões de bancos existentes**: pgvector (PostgreSQL, 2021), suporte
  nativo em MongoDB Atlas, Elasticsearch, Redis, SingleStore etc.
- A tendência recente é a "comoditização": muitos bancos tradicionais
  adicionaram suporte a vetores, reduzindo a necessidade de um sistema
  dedicado só para embeddings em vários casos de uso.

### Hybrid search

Na prática, busca vetorial pura raramente basta. Sistemas de produção
quase sempre combinam:
- Similaridade de embedding + filtros de metadado (data, fonte, tenant…)
- Ou fusão com busca lexical (BM25 / full-text) via RRF (Reciprocal Rank
  Fusion) ou scores ponderados.

Isso resolve casos em que o embedding sozinho não captura restrições
exatas (ex.: "só documentos de 2026" ou "só desta pasta").

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Banco de dados vetorial"
relations:
  - is_a: "Infraestrutura de armazenamento e busca"
  - depends_on: "[[Embeddings]]"
  - enables: "[[RAG]] em escala de produção"
  - related_to: "[[Chunking]]"
rules_of_thumb:
  - "Regra 1: Índices aproximados (HNSW, IVF) trocam precisão exata por velocidade — aceitável na maioria dos casos de RAG, não em buscas que exigem 100% de recall."
  - "Regra 2: HNSW é o default sensato para a maioria dos workloads de RAG (< ~10-50M vetores, dados dinâmicos, necessidade de alta recall)."
  - "Regra 3: IVF (ou IVF-PQ) quando memória ou tempo de construção do índice são o gargalo, ou datasets muito grandes e relativamente estáticos."
  - "Regra 4: Filtro por metadado + busca vetorial (ou hybrid search com lexical) resolve casos que busca vetorial pura não resolve sozinha."
  - "Exceção: Datasets pequenos (poucos milhares a dezenas de milhares de vetores) muitas vezes não precisam de banco vetorial dedicado — busca por força bruta em memória já é rápida o suficiente e tem recall perfeito."
  - "Exceção: Se o sistema já roda em PostgreSQL e o volume não é extremo, pgvector + HNSW costuma ser suficiente e evita introduzir mais um componente de infraestrutura."
```

---

## 🔗 3. Notas Relacionadas
- [[Embeddings]]
- [[RAG]]
- [[Chunking]]

## 📚 4. Fontes
- Ver `Fontes/Banco-de-Dados-Vetorial.md`.
- Conceito de ANN e índices: literatura clássica de information retrieval +
  implementações modernas (HNSW original de Malkov & Yashunin; IVF/PQ de
  Jégou et al.).
- Ecossistema de produtos: documentação oficial e comparações públicas de
  Pinecone, Weaviate, Milvus, Qdrant, pgvector (2021–2026).
