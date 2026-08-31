# Fontes — Roteamento de Modelos

## [RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665)
- Autores: Isaac Ong et al. (LMSYS / colaboradores)
- Usada para: formulação do problema de routing forte vs fraco; treino com preferência humana e augmentação; redução de custo em benchmarks sem colapso de qualidade agregada; capacidade de transferência entre pares de modelos.
- Data de acesso: 2026-08-30
- Confiabilidade: arXiv:2406.18665 (v4 fev/2025).

## [RouteLLM — LMSYS framework](https://github.com/lm-sys/routellm)
- Usada para: enquadramento prático de router como camada de serving; motivação custo vs qualidade.
- Data de acesso: 2026-08-30
- Confiabilidade: repositório oficial associado ao paper.

## Observação de método
Números de “85% de redução de custo” dependem do benchmark e do par de modelos; a nota não os trata como garantia de produção. Heurísticas e cascatas coexistentes com routers aprendidos.
