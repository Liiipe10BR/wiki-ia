---
tags:
  - wiki/agente
  - tipo/meta
aliases: ["Estado do Projeto", "Memória do Vault", "Changelog"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-30
confianca: 1.0
embedding_prioritario: true
---


# 🧭 Estado do Projeto — LEIA ISTO PRIMEIRO

> **Se você é um agente de IA abrindo este vault pela primeira vez nesta
> sessão: leia este arquivo inteiro antes de criar, editar ou responder
> qualquer coisa sobre ele.** Este arquivo é a memória persistente do
> projeto — nenhuma IA individual lembra de sessões passadas, então este
> documento é o que substitui essa memória.

---

## O que é este projeto

Uma base de conhecimento em Obsidian com duas camadas (humana + máquina),
escrita colaborativamente por **humanos e agentes de IA**, pensada pra
alimentar RAG de forma confiável. Ver `README.md` na raiz pra estrutura
completa e `CONTRIBUTING.md` pra protocolo de contribuição.

## Status atual

| Item | Valor |
|---|---|
| Notas de conceito ativas | 15 (RAG, Embeddings, Model-Context-Protocol, Fine-tuning, Banco-de-Dados-Vetorial, Chunking, Janela-de-Contexto, Agente-de-IA, Avaliação-de-RAG, Proveniência-de-Dados, Reranking, Hybrid-Search, Alucinação, Tool-Calling, Grounding) |
| Contribuições humanas | 3 notas iniciais + estrutura do vault |
| Contribuições de IA | 12 notas novas + revisões, fontes e CI — Claude (várias sessões) + Grok (xAI, 6ª–13ª e Issue #13) + Replit (9ª contribuição) |
| Protocolo de contribuição | v1 — ver `CONTRIBUTING.md` |
| Divergências abertas | Nenhuma no momento |
| Ferramentas auxiliares | `scripts/validar_links.py` (validação de links `[[wiki]]` quebrados) + workflow CI `.github/workflows/validar-links.yml` |

## Changelog (mais recente primeiro)

- **2026-08-30** — Grok (xAI), Issue #13. Criou `Conceitos/Grounding.md` e `Fontes/Grounding.md` (AIS / Rashkin arXiv:2112.12870; ALCE / Gao arXiv:2305.14627; Attributed QA / Bohnet arXiv:2212.08037; Trust-Align arXiv:2409.11242). Distingue grounding de RAG; contexto recuperado ≠ evidência usada; recusa sem evidência; limites de self-citation. Atualizou `_index/MOC.md`, `Fontes/README.md` e ligação mínima em `Conceitos/Alucinacao.md`. `confianca` 0.92. Não duplica Alucinação nem RAG. PRs #9–#11 (Prompt-Injection) não foram tocados.
- **2026-08-30** — Grok (xAI), décima terceira IA a contribuir neste vault. Criou `Conceitos/Alucinacao.md` (taxonomia intrínseca/extrínseca, relação com RAG, Avaliação-de-RAG, Proveniência e Tool-Calling; regras de mitigação) e `Conceitos/Tool-Calling.md` (Toolformer, Gorilla, schema de tools, validação de argumentos, ligação a MCP e Agente-de-IA). Criou `Fontes/Alucinacao.md` (survey arXiv:2311.05232 / ACM TOIS; arXiv:2305.18248) e `Fontes/Tool-Calling.md` (arXiv:2302.04761, arXiv:2305.15334). Atualizou `_index/MOC.md` (lista + grafo), `Fontes/README.md` e este arquivo. `confianca` 0.93 em ambas, `embedding_prioritario: true`. Nenhuma divergência encontrada.
- **2026-08-30** — Grok (xAI), décima segunda IA a contribuir neste vault. Criou as notas `Conceitos/Reranking.md` (cross-encoders, late interaction ColBERT, listwise LLM rerankers; relação com RAG, Hybrid-Search, Avaliação-de-RAG e Janela-de-Contexto) e `Conceitos/Hybrid-Search.md` (sparse + dense + RRF; padrão de produção atual). Criou `Fontes/Reranking.md` (Nogueira & Cho arXiv:1901.04085, ColBERT arXiv:2004.12832, RankGPT/listwise) e `Fontes/Hybrid-Search.md`. Atualizou `_index/MOC.md` (lista + grafo) e este arquivo. `confianca` 0.93 (Reranking) e 0.92 (Hybrid-Search), `embedding_prioritario: true` em ambas. Nenhuma divergência encontrada.
- **2026-08-29** — Grok (xAI), décima-primeira IA a contribuir neste vault. Implementou a Issue #4: criou `.github/workflows/validar-links.yml` para executar `python3 scripts/validar_links.py .` automaticamente em Pull Requests que alterem arquivos Markdown ou scripts. O workflow falha se houver links `[[wiki]]` quebrados e não faz merge automático. Atualizou este arquivo.
- **2026-08-29** — Grok (xAI), décima IA a contribuir neste vault. Criou a nota `Conceitos/Proveniencia-de-Dados.md` respondendo à Issue #2, cobrindo definição, padrões (W3C PROV), relação com RAG/Avaliação-de-RAG/Agente-de-IA e regras práticas de preservação de metadados e cadeia de evidência. Criou `Fontes/Proveniencia-de-Dados.md` com fontes reais (W3C PROV, survey arXiv:2601.14311, Data Provenance Initiative / MIT, position paper ICML 2024 e survey de lifecycle provenance). Atualizou `_index/MOC.md` (lista + grafo) e este arquivo. `confianca` 0.92, `embedding_prioritario: true`. Nenhuma divergência encontrada.
- **2026-08-29** — Replit, nona IA a contribuir neste vault. Criou a nota `Conceitos/Avaliacao-de-RAG.md`, cobrindo a separação entre qualidade da recuperação, fidelidade e relevância da resposta, além de testes de regressão, casos sem resposta e calibração de avaliadores automáticos. Criou `Fontes/Avaliacao-de-RAG.md` com RAGAs (EACL 2024) e ARES (NAACL 2024), e atualizou o MOC, o README e o estado do projeto. `confianca` 0.92. Nenhuma divergência encontrada.
- **2026-08-29** — Grok (xAI), oitava IA a contribuir neste vault. Criou a nota nova `Conceitos/Agente-de-IA.md` (conceito central que faltava no grafo: loop Thought-Action-Observation, relação com MCP/RAG/Janela de Contexto/Fine-tuning). Fontes reais: ReAct (Yao et al., arXiv:2210.03629, ICLR 2023), Toolformer (Schick et al., arXiv:2302.04761, NeurIPS 2023) e documentação da doação do MCP à Agentic AI Foundation (dez/2025). Criou `Fontes/Agente-de-IA.md`, atualizou `_index/MOC.md` (lista + grafo) e este arquivo. `confianca` 0.93, `embedding_prioritario: true`. Nenhuma divergência encontrada.
- **2026-08-29** — Grok (xAI), sétima IA a contribuir neste vault. Fechou o item em aberto de `Fontes/` para as três notas restantes: criou `Fontes/Fine-tuning.md` (survey Instruction Tuning arXiv:2308.10792, LoRA arXiv:2106.09685, GPT-3), `Fontes/Chunking.md` (Late Chunking arXiv:2409.04701 + avaliações sistemáticas 2025–2026) e `Fontes/Janela-de-Contexto.md` (MECW arXiv:2509.21361, Lost in the Middle, surveys de long-context). Atualizou as três notas em `Conceitos/` (seções Fontes + `ultima_verificacao` + `confianca`: Fine-tuning 0.85→0.92, Chunking 0.85→0.90, Janela-de-Contexto 0.75→0.88) e o status de `Fontes/README.md`. Todas as 7 notas de conceito agora têm arquivo de fonte correspondente. Nenhuma divergência encontrada.
- **2026-08-28** — Grok (xAI), sexta IA a contribuir neste vault. Revisou e expandiu profundamente `Conceitos/Banco-de-Dados-Vetorial.md` (nota que estava com `confianca` 0.85 e fontes genéricas): adicionou seções sobre índices ANN (HNSW vs IVF, trade-offs de memória/recall/construção), ferramentas típicas (Pinecone, Weaviate, Milvus, Qdrant, Chroma, pgvector), hybrid search + filtros de metadado, e regras práticas mais granulares. Subiu `confianca` de 0.85 para 0.92. Criou `Fontes/Banco-de-Dados-Vetorial.md` com referências reais (Malkov & Yashunin para HNSW; Jégou et al. 2011 para PQ/IVF; documentação de produto e comparações públicas 2021–2026). Atualizou `contribuido_por` e o status deste arquivo. Nenhuma divergência encontrada.
- **2026-08-28** — Claude (Anthropic, Sonnet 5), quinta IA a contribuir neste vault, deu continuidade ao item em aberto de popular `Fontes/`: adicionou fonte real a `Conceitos/Embeddings.md`, que até então citava só "conhecimento geral consolidado" sem referência checável. Citou Mikolov et al. (2013), "Efficient Estimation of Word Representations in Vector Space" (word2vec). Criou `Fontes/Embeddings.md` e subiu `confianca` de 0.9 para 0.93. Rodou `scripts/validar_links.py` — nenhum link quebrado, nenhuma nota órfã. Nenhuma divergência encontrada.
- **2026-08-28** — Claude (Anthropic, Sonnet 5), quarta IA a contribuir neste vault, focou em popular `Fontes/` com fontes reais: (1) criou `Fontes/RAG.md` citando Lewis et al. 2020, arXiv:2005.11401; (2) corrigiu governança defasada de MCP (doação à Agentic AI Foundation em dez/2025) e criou `Fontes/Model-Context-Protocol.md`.
- **2026-08-28** — Claude (Anthropic, Sonnet 5), terceira IA: `Conceitos/Janela-de-Contexto.md`, pasta `Fontes/` + README, `scripts/validar_links.py`.
- **2026-08-28** — Claude (Anthropic, Sonnet 5), segunda IA: `Chunking.md` e atualização do MOC.
- **2026-08-28** — Claude (Anthropic, Sonnet 4.6) criou `Banco-de-Dados-Vetorial.md` e atualizou o MOC.
- **2026-08-28** — Claude (Anthropic, Sonnet 4.6) criou `Fine-tuning.md`, `CONTRIBUTING.md` e este arquivo de estado.
- **2026-08-28** — Vault criado pelo mantenedor humano com estrutura base: `README.md`, `_templates/Template-Conceito.md`, `_index/MOC.md`, e 3 notas iniciais (`RAG`, `Embeddings`, `Model-Context-Protocol`).

## Próximos passos sugeridos (em aberto pra quem pegar)

- [x] ~~Nota ainda faltando no grafo: "Chunking" é citado em `RAG.md`~~ — criada em 2026-08-28.
- [ ] Decidir hospedagem compartilhada (GitHub é o caminho mais óbvio — ver `CONTRIBUTING.md`).
- [x] ~~Script de validação de links `[[wiki]]` quebrados~~ — `scripts/validar_links.py`.
- [ ] Definir se `contribuido_por` deve virar campo obrigatório no template pra toda nota nova, não só nas escritas por IA.
- [x] ~~Criar uma nota sobre avaliação de RAG~~ — `Avaliacao-de-RAG.md`.
- [x] ~~`Fontes/` vazia de arquivos reais~~ — populada; Grounding.md adicionado em 2026-08-30.
- [ ] Rodar `scripts/validar_links.py` de novo depois de decidir se os placeholders `[[wiki]]`/`[[Conceito]]` no README e no template devem ser reescritos.
- [x] ~~Validação automática de links no GitHub Actions~~ — `.github/workflows/validar-links.yml`.
- [x] ~~Nota Grounding (separar de Alucinação)~~ — criada em 2026-08-30 (Issue #13).
- [ ] Notas candidatas ainda ausentes: Guardrails, Multi-Agent, Quantização, Prompt Engineering.

## Regra de manutenção deste arquivo

Qualquer agente (humano ou IA) que criar, editar ou remover uma nota **deve**
adicionar uma linha no Changelog acima, com data, autor/agente, e o que
mudou. Sem isso, o próximo agente que abrir o vault não sabe o que já foi
feito e corre risco de duplicar trabalho ou contradizer uma nota existente
sem perceber.
