---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Graph RAG", "GraphRAG", "RAG com grafos", "Knowledge Graph RAG"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #29 / GraphRAG e recuperação orientada a grafos"
---

# 🕸️ GraphRAG

> **Resumo para Humanos:**
> Variante de [[RAG]] que indexa o corpus como **grafo de entidades e relações**
> (e, em algumas linhas, sumários de comunidades) para responder melhor a
> perguntas *globais* sobre o conjunto de documentos — não só “ache o parágrafo
> parecido”.

---

## 📖 1. Contexto Humano (Narrativa)

O [[RAG]] vetorial clássico brilha em perguntas *locais*: a resposta está em
poucos trechos semanticamente próximos. Falha em perguntas do tipo “quais são
os temas principais deste corpus?” — isso é sumarização orientada a query em
escala, não retrieval de k vizinhos.

O trabalho da Microsoft **From Local to Global** (Edge et al., arXiv:2404.16130)
propõe **GraphRAG**: (1) extrair grafo de entidades/relações dos documentos com
LLM; (2) detectar comunidades e pré-gerar sumários; (3) na pergunta, gerar
respostas parciais por comunidade e agregar. Em perguntas de *sensemaking*
global sobre corpora ~1M tokens, reportam ganhos de abrangência e diversidade
frente a baseline só vetorial.

Isso **não** substitui [[Hybrid-Search]] nem [[Reranking]] para factoid local.
Trade-offs honestos:

- **Custo de indexação** — muitas chamadas de LLM para extrair entidades
- **Atualização** — documento novo pode exigir re-extração / invalidação de
  comunidades
- **Ruído de extração** — entidades erradas viram arestas erradas
- **Latência de query** — map-reduce sobre comunidades pode ser caro

[[Proveniencia-de-Dados]] importa: de qual comunidade/documento veio cada
afirmação parcial? Surveys posteriores (ex.: arXiv:2501.00309) tratam GraphRAG
como família ampla (não um único produto). Combine com [[Embeddings]] e busca
vizinha quando a pergunta for local.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "GraphRAG — RAG com grafo de conhecimento e sumários de comunidade"
relations:
  - is_a: "Arquitetura de recuperação aumentada orientada a grafo"
  - depends_on: "[[RAG]]"
  - related_to: "[[Hybrid-Search]]"
  - related_to: "[[Reranking]]"
  - related_to: "[[Embeddings]]"
  - related_to: "[[Proveniencia-de-Dados]]"
  - related_to: "[[Avaliacao-de-RAG]]"
  - related_to: "[[Chunking]]"
rules_of_thumb:
  - "Regra 1: Use GraphRAG quando a pergunta exige visão global do corpus; para factoid local, prefira RAG denso/hybrid + rerank."
  - "Regra 2: Orce o custo de construção do grafo e de atualização incremental — indexação GraphRAG costuma ser bem mais cara que embedding de chunks."
  - "Regra 3: Trate extração de entidades como etapa ruidosa; avalie qualidade do grafo, não só a resposta final."
  - "Regra 4: Preserve proveniência (documento → entidade → comunidade → resposta parcial)."
  - "Regra 5: Não apresente GraphRAG como substituto universal do RAG vetorial."
  - "Exceção: Corpus pequeno e estável pode justificar reindexação completa a cada mudança."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Hybrid-Search]]
- [[Reranking]]
- [[Embeddings]]
- [[Proveniencia-de-Dados]]
- [[Avaliacao-de-RAG]]
- [[Chunking]]

## 📚 4. Fontes
- Ver `Fontes/GraphRAG.md`.
- Edge et al., arXiv:2404.16130.
- Survey GraphRAG, arXiv:2501.00309.
