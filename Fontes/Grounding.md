# Fontes — Grounding

## [Measuring Attribution in Natural Language Generation Models](https://arxiv.org/abs/2112.12870)
- Autores: Hannah Rashkin et al.
- Usada para: definição operacional de AIS (Attributable to Identified Sources) — o texto gerado sobre o mundo deve ser verificável contra uma fonte identificada e independente.
- Data de acesso: 2026-08-30
- Confiabilidade: artigo em *Computational Linguistics* 49(4), 2023 (DOI 10.1162/coli_a_00486); preprint arXiv:2112.12870.

## [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627)
- Autores: Tianyu Gao, Howard Yen, Jiatong Yu, Danqi Chen
- Usada para: geração com citações inline (ALCE); métricas de citation recall/precision; distinção entre recuperar documentos e atribuir frases a eles.
- Data de acesso: 2026-08-30
- Confiabilidade: EMNLP 2023; arXiv:2305.14627.

## [Attributed Question Answering: Evaluation and Modeling for Attributed Large Language Models](https://arxiv.org/abs/2212.08037)
- Autores: Bernd Bohnet et al.
- Usada para: tarefa de Attributed QA e o ponto de que atribuição é avaliável à parte da fluência.
- Data de acesso: 2026-08-30
- Confiabilidade: preprint arXiv:2212.08037 (v2, 2023).

## [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://arxiv.org/abs/2409.11242)
- Autores: Maojia Song et al. (Trust-Align)
- Usada para: groundedness das citações vs. veracidade da resposta; recusa quando a evidência recuperada não cobre a pergunta.
- Data de acesso: 2026-08-30
- Confiabilidade: preprint arXiv:2409.11242.

## Fontes de apoio (citadas na narrativa, sem generalizar números)
- Slobodkin et al., *Attribute First, then Generate* — arXiv:2403.17104 (atribuição em span, não só no documento).
- Lewis et al. 2020, RAG — arXiv:2005.11401 (pipeline de recuperação; já documentado em `Fontes/RAG.md`).

## Observação de método
Nenhuma fonte inventada. Grounding aqui é a propriedade da resposta (AIS / atribuição), não um sinônimo de RAG. Percentuais reportados em Trust-Align e ALCE não foram copiados como leis gerais do campo.
