# Fontes — Speculative Decoding

## [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
- Autores: Yaniv Leviathan, Matan Kalman, Yossi Matias
- Usada para: definição do algoritmo; equivalência de distribuição; resultados de aceleração em T5-XXL no paper.
- Data de acesso: 2026-09-02
- Confiabilidade: arXiv:2211.17192; ICML 2023 Oral.

## Observação de método
Implementações de produto (Medusa, EAGLE, drafts nativos de vendors) variam; o núcleo é draft + verify sem alterar a lei do target.
