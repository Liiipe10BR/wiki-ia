---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["HyDE", "Hypothetical Document Embeddings", "Documento hipotético"]
data_criacao: 2026-09-02
ultima_verificacao: 2026-09-02
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — HyDE (Gao et al.)"
---

# 📄 HyDE (Hypothetical Document Embeddings)

> **Resumo para Humanos:**
> Para melhorar retrieval **zero-shot**: o LLM gera um **documento hipotético**
> que responderia a query; esse texto é embeddado e usado para buscar no corpus
> real — filtrando detalhes inventados via vizinhança densa.

---

## 📖 1. Contexto Humano (Narrativa)

Queries curtas e documentos longos vivem em “estilos” diferentes no espaço de
[[Embeddings]]. **HyDE** (Gao et al., arXiv:2212.10496) pivoia:

1. LLM instruction-tuned gera um *documento hipotético* para a query
2. Encoder denso (ex.: Contriever no paper) embedda o hipotético
3. Busca por similaridade traz documentos **reais** da vizinhança

O hipotético pode alucinar fatos; o gargalo denso + corpus real **ancora** a
busca. O paper reporta ganhos fortes sobre Contriever unsupervised e
performance comparável a retrievers fine-tuned em vários tasks/idiomas nos
experimentos.

### Onde encaixa no [[RAG]]

- Alternativa/complemento a query rewriting clássico
- Útil quando não há labels de relevância para treinar retriever
- Custo: +1 geração LLM antes do retrieval

Não substitui [[Reranking]] nem [[Grounding]] na geração final. O documento
hipotético **não** deve ser citado como fonte — só os chunks reais recuperados.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "HyDE — retrieval via embeddings de documentos hipotéticos"
relations:
  - is_a: "Técnica de query expansion / pivot dense retrieval"
  - related_to: "[[RAG]]"
  - related_to: "[[Embeddings]]"
  - related_to: "[[Hybrid-Search]]"
  - related_to: "[[Reranking]]"
  - related_to: "[[Grounding]]"
  - related_to: "[[Alucinacao]]"
rules_of_thumb:
  - "Regra 1: Nunca use o documento hipotético como evidência citada — só o corpus real."
  - "Regra 2: Meça recall/precision vs query direta; HyDE não é grátis (tokens + latência)."
  - "Regra 3: Combine com rerank se o top-k vier ruidoso."
  - "Exceção: Queries já longas e bem alinhadas ao estilo do corpus podem não precisar de HyDE."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Embeddings]]
- [[Hybrid-Search]]
- [[Reranking]]
- [[Grounding]]
- [[Alucinacao]]

## 📚 4. Fontes
- Ver `Fontes/HyDE.md`.
- Gao et al., arXiv:2212.10496.
