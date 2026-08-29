# Fontes — Embeddings

## [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- Usada para: origem do word2vec (Mikolov, Chen, Corrado e Dean, 2013) — o
  marco que popularizou embeddings densos e treináveis em escala para NLP,
  citado na nota como o ponto de virada prático da técnica.
- Data de acesso: 2026-08-28
- Confiabilidade: preprint arXiv amplamente citado (autores do Google);
  não passou por peer review formal em conferência no formato original,
  mas é a referência padrão de facto na literatura de NLP para word2vec.

## Nota sobre origem mais ampla do conceito
- A ideia de representar significado como vetor numérico (semântica
  distribucional) é anterior a 2013 — um marco reconhecido é Bengio et al.
  (2003), que propôs um modelo de linguagem neural aprendendo representações
  de palavras junto com os parâmetros do modelo. Word2vec não "inventou"
  embeddings, mas foi o que tornou a técnica prática e barata o suficiente
  pra virar padrão de produção. Por isso a nota em `Conceitos/Embeddings.md`
  cita word2vec como marco, não como origem absoluta do conceito.
