# Fontes — FlashAttention

## [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
- Autores: Tri Dao et al.
- Usada para: motivação IO-aware; tiling HBM/SRAM; attention exata com menos memory traffic; speedups e contextos longos reportados no paper.
- Data de acesso: 2026-09-02
- Confiabilidade: arXiv:2205.14135.

## Observação de método
FlashAttention-2+ e implementações de framework evoluem a API; o conceito permanece attention exata otimizada para hierarquia de memória da GPU.
