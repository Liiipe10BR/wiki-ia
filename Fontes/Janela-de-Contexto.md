# Fontes — Janela-de-Contexto

## [Context Is What You Need: The Maximum Effective Context Window for Real World Limits of LLMs](https://arxiv.org/abs/2509.21361)
- Usada para: distinção entre Maximum Context Window (MCW, o número anunciado pelo provedor) e Maximum Effective Context Window (MECW); evidência empírica de que a precisão degrada muito antes do limite nominal e que o MECW varia por tipo de tarefa.
- Data de acesso: 2026-08-29
- Confiabilidade: paper arXiv 2025 (versão 2026), com centenas de milhares de pontos de dados em múltiplos modelos.

## Fenômeno “Lost in the Middle” e limitações de atenção
- Usada para: regra de que contexto longo não garante recall uniforme — informação no meio da janela tende a ser menos utilizada (Liu et al., “Lost in the Middle: How Language Models Use Long Contexts”, arXiv:2307.03172).
- Data de acesso: 2026-08-29
- Confiabilidade: paper bem citado (2023); confirmação qualitativa em surveys posteriores de long-context LLMs.

## Complexidade quadrática da atenção e KV-cache
- Usada para: razão computacional do limite de janela (atenção O(n²) e crescimento de memória do KV-cache); motivação de técnicas de atenção esparsa, RoPE interpolation (YaRN, LongRoPE, etc.) e serving long-context.
- Referências: surveys de long-context LLM serving e arquitetura (ex.: arXiv:2405.11299 CAP principle for LLM serving; revisões de positional encoding e extensão de contexto).
- Data de acesso: 2026-08-29
- Confiabilidade: conhecimento de arquitetura Transformer consolidado + surveys recentes.
