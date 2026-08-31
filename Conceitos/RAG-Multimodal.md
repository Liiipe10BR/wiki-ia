---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["RAG Multimodal", "Multimodal RAG", "MRAG", "Vision RAG"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-31
confianca: 0.91
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #39; aprofundamento 2026-08-31 com surveys MRAG"
---

# 🖼️ RAG multimodal

> **Resumo para Humanos:**
> Especialização de [[RAG]] em que **consulta e/ou corpus** envolvem mais de uma
> modalidade (texto, imagem, às vezes áudio/vídeo): recuperar evidência certa e
> gerar resposta **ancorada** nela.

---

## 📖 1. Contexto Humano (Narrativa)

O RAG textual indexa chunks e [[Embeddings]] de linguagem. Manuais, slides,
PDFs escaneados e UIs reais misturam figura, tabela e layout. **RAG multimodal
(MRAG)** estende retrieval e geração para esse mundo.

### Por que não é “só OCR + RAG”

OCR transforma imagem em texto e reusa o pipeline clássico — útil, mas perde
estrutura visual, diagramas e relações espaciais. MRAG de verdade enfrenta:

- **Alinhamento cross-modal** — o que a query em texto deve buscar na imagem?
- **Indexação** — embedding multimodal único vs. índices por modalidade + fusão
- **Granularidade** — página, região (bbox), frame, slide
- **Fusão** — no retrieval, no contexto do LLM, ou nos dois

Surveys (arXiv:2502.08826; arXiv:2504.08748) organizam datasets, métricas e
familias de métodos; o consenso útil para o vault: **cross-modal reasoning**
acrescenta falhas que o RAG unimodal não tinha.

### Pipelines típicos (visão de engenharia)

1. Captioning/descrição de imagens → índice textual (simples; erro no caption propaga)
2. Encoder multimodal compartilhado (ex.: família CLIP-like) → busca por similaridade
3. Retrievers separados + late fusion / rerank
4. Agentic: o [[Agente-de-IA]] escolhe tool de visão vs. busca textual

### Avaliação e riscos

[[Avaliacao-de-RAG]] clássica (faithfulness/relevância textual) **não cobre**
alucinação do tipo “o modelo inventou um número que não está no gráfico”.
[[Grounding]] e [[Proveniencia-de-Dados]] devem apontar modalidade e trecho
(página, região). Custo de indexação e atualização costuma ser maior que no RAG
só texto.

MRAG **não** substitui [[GraphRAG]] nem hybrid search textual quando o corpus é
predominantemente texto. Escolha pela natureza dos documentos e das perguntas.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "RAG multimodal (MRAG)"
relations:
  - is_a: "Especialização de RAG para múltiplas modalidades"
  - depends_on: "[[RAG]]"
  - related_to: "[[Embeddings]]"
  - related_to: "[[Grounding]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[Proveniencia-de-Dados]]"
  - related_to: "[[Avaliacao-de-RAG]]"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[GraphRAG]]"
rules_of_thumb:
  - "Regra 1: Mapeie modalidades do corpus e das queries antes de escolher encoder único vs. índices separados."
  - "Regra 2: Proveniência por modalidade (doc, página, bbox, frame) — senão não há auditoria."
  - "Regra 3: Avalie alucinação visual e textual; métricas só de texto mascaram erro em figuras."
  - "Regra 4: Corpus quase só texto: OCR seletivo + RAG clássico pode ser suficiente."
  - "Regra 5: Não trate um survey ou um produto como definição única de MRAG."
  - "Exceção: Query e corpus estritamente textuais não precisam de pipeline multimodal."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Embeddings]]
- [[Grounding]]
- [[Alucinacao]]
- [[Proveniencia-de-Dados]]
- [[Avaliacao-de-RAG]]
- [[Agente-de-IA]]
- [[GraphRAG]]

## 📚 4. Fontes
- Ver `Fontes/RAG-Multimodal.md`.
- Survey multimodal RAG, arXiv:2502.08826.
- Survey MRAG, arXiv:2504.08748.
