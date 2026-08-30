# Fontes — Quantizacao

## [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference](https://arxiv.org/abs/1712.05877)
- Autores: Benoit Jacob et al. (Google)
- Usada para: distinção QAT vs inferência em inteiros; quantização de pesos e ativações em INT8; esquema com scale e zero-point.
- Data de acesso: 2026-08-30
- Confiabilidade: CVPR 2018 (IEEE/CVF); preprint arXiv:1712.05877.

## [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323)
- Autores: Elias Frantar, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh
- Usada para: PTQ one-shot em LLMs, 3–4 bits por peso, compressão e speedup reportados em GPU (A100/A6000) como evidência de trade-off, não como lei geral.
- Data de acesso: 2026-08-30
- Confiabilidade: ICLR 2023; arXiv:2210.17323.

## [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978)
- Autores: Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang et al. (MIT HAN Lab)
- Usada para: weight-only quantization consciente de ativações; importância desigual dos pesos; uso em compressão on-device.
- Data de acesso: 2026-08-30
- Confiabilidade: MLSys 2024 Best Paper; arXiv:2306.00978.

## [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
- Autores: Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer
- Usada para: relação entre quantização 4-bit (NF4) e fine-tuning via LoRA; memória reduzida sem igualar automaticamente “melhor qualidade em todo benchmark”.
- Data de acesso: 2026-08-30
- Confiabilidade: NeurIPS 2023 (versão estendida no arXiv:2305.14314).

## [Quantization concepts — Hugging Face Transformers](https://huggingface.co/docs/transformers/quantization/concept_guide)
- Usada para: vocabulário de produção (PTQ vs QAT, granularidade per-tensor/per-channel, backends múltiplos).
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial do ecossistema Transformers.

## Observação de método
Nenhuma fonte inventada. Números de speedup ou perplexidade dos papers não foram generalizados como válidos para todo modelo, hardware ou tarefa. A nota registra explicitamente que o ranking entre métodos depende do contexto.
