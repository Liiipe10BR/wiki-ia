---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Embeddings", "Vetores Semânticos", "Embedding Vectors"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-28
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Claude (Anthropic, Sonnet 5), quinta IA a contribuir neste vault — adicionou fonte real (Mikolov et al., 2013) e subiu confianca de 0.9 para 0.93"
---

# 🧠 Embeddings (Vetores Semânticos)

> **Resumo para Humanos:**
> Forma de transformar texto (ou imagem, áudio) em uma lista de números onde
> coisas com significado parecido ficam "próximas" matematicamente.

---

## 📖 1. Contexto Humano (Narrativa)

Um embedding é a "impressão digital numérica" de um pedaço de conteúdo. Dois
textos com significados parecidos geram vetores próximos no espaço
matemático, mesmo que usem palavras completamente diferentes — é assim que
buscas por "carro" também encontram trechos sobre "automóvel".

É a peça que torna [[RAG]] possível: sem embeddings, buscar "por significado"
em vez de "por palavra exata" seria muito mais difícil.

- A qualidade do embedding define o teto de qualidade de qualquer busca
  semântica construída em cima dele.
- Embeddings ficam desatualizados se o modelo que os gerou mudar — misturar
  vetores de modelos diferentes no mesmo banco quebra a busca silenciosamente.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Embeddings (vetores semânticos)"
relations:
  - is_a: "Representação numérica de conteúdo"
  - depends_on: "Modelo de embedding (ex: text-embedding-3, voyage-3)"
  - enables: "[[RAG]]"
  - conflicts_with: "Busca por palavra-chave exata (quando sinônimos importam mais que precisão literal)"
rules_of_thumb:
  - "Regra 1: Nunca misture embeddings gerados por modelos diferentes no mesmo índice de busca."
  - "Regra 2: Re-indexe tudo se trocar de modelo de embedding — vetores antigos e novos não são comparáveis."
  - "Exceção: Se a busca precisa ser exata (ex: buscar um ID, um código), use busca por palavra-chave, não embeddings."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]

## 📚 4. Fontes
- Ver `Fontes/Embeddings.md` — o marco moderno mais citado é Mikolov et al.
  (2013), "Efficient Estimation of Word Representations in Vector Space"
  (word2vec), que popularizou embeddings densos e treináveis em escala pra
  NLP. A ideia de representação distribuída de significado é mais antiga
  (ex: Bengio et al., 2003, modelo de linguagem neural), mas word2vec é o
  ponto de virada prático que o texto acima descreve.
- Uso em produção (bancos vetoriais como Pinecone, Weaviate, Chroma):
  conhecimento geral consolidado do setor, sem paper único de origem —
  mantido como está, sem fonte específica verificável.
