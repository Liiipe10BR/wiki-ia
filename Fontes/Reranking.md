# Fontes — Reranking

## [Passage Re-ranking with BERT](https://arxiv.org/abs/1901.04085)
- Autores: Rodrigo Nogueira, Kyunghyun Cho
- Usada para: definição e resultados fundacionais do uso de BERT como cross-encoder para reordenação de passagens; ganhos em MS MARCO e TREC-CAR.
- Data de acesso: 2026-08-30
- Confiabilidade: paper de Information Retrieval amplamente citado; arXiv:1901.04085 (versão v5 de 2020).

## [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://arxiv.org/abs/2004.12832)
- Autores: Omar Khattab, Matei Zaharia
- Usada para: arquitetura de late interaction (MaxSim), trade-off entre efetividade de cross-encoder e eficiência de bi-encoder; aceito no SIGIR 2020.
- Data de acesso: 2026-08-30
- Confiabilidade: paper revisado por pares (SIGIR 2020), arXiv:2004.12832.

## RankGPT e listwise LLM rerankers (Sun et al., 2023 e sucessores)
- Representativo: trabalhos de zero-shot listwise document reranking com LLMs (ex.: arXiv:2305.02156 — LRL; arXiv:2312.02969 — Rank-without-GPT; referências a RankGPT em papers de 2023–2025).
- Usada para: abordagem listwise em que o LLM gera uma permutação ordenada de candidatos; limitações de contexto e custo.
- Data de acesso: 2026-08-30
- Confiabilidade: papers de arXiv e literatura recente de IR/LLM; resultados zero-shot reportados de forma consistente na comunidade.

## Observação de método
Nenhuma fonte inventada. Todas as afirmações de efetividade e arquitetura na nota de Conceitos/Reranking.md estão ancoradas nos papers acima ou em consenso consolidado da literatura de neural ranking (2019–2025).
