---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["RAG Multimodal", "Multimodal RAG", "MRAG", "Vision RAG"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.90
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #39 / RAG multimodal"
---

# 🖼️ RAG multimodal

> **Resumo para Humanos:**
> Estender [[RAG]] para corpora e queries que misturam **texto, imagem** (e às
> vezes áudio/vídeo): recuperar evidência multimodal e gerar resposta ancorada.

---

## 📖 1. Contexto Humano (Narrativa)

O RAG clássico assume chunks de texto e [[Embeddings]] textuais. Documentos
reais têm figuras, tabelas, slides e scans. **RAG multimodal** (MRAG) recupera
e funde evidência de mais de uma modalidade.

Surveys recentes (ex.: arXiv:2502.08826; arXiv:2504.08748) organizam desafios:
alinhamento cross-modal, fusão no retrieval vs. na geração, benchmarks e
métricas além de faithfulness textual. Pipelines comuns: (a) embedding
multimodal único; (b) índices separados por modalidade + fusão; (c) captioning
de imagens para reentrar no índice textual.

Riscos: alucinar conteúdo “visto” na imagem; perder layout; custo de indexação.
[[Grounding]] e [[Proveniencia-de-Dados]] precisam apontar *qual* trecho/imagem
sustenta a afirmação. [[Avaliacao-de-RAG]] textual não basta sozinha.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "RAG multimodal — recuperação e geração com múltiplas modalidades"
relations:
  - is_a: "Especialização de RAG para dados multimodais"
  - depends_on: "[[RAG]]"
  - related_to: "[[Embeddings]]"
  - related_to: "[[Grounding]]"
  - related_to: "[[Alucinacao]]"
  - related_to: "[[Proveniencia-de-Dados]]"
  - related_to: "[[Avaliacao-de-RAG]]"
rules_of_thumb:
  - "Regra 1: Não assuma um único embedding multimodal como solução universal; valide no seu corpus."
  - "Regra 2: Preserve proveniência por modalidade (página, bbox, frame)."
  - "Regra 3: Avalie alucinação visual e textual separadamente quando possível."
  - "Regra 4: Para documentos predominantemente texto, RAG textual + OCR seletivo pode ser mais simples que MRAG completo."
  - "Exceção: Query só-texto sobre corpus só-texto não precisa de pipeline multimodal."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Embeddings]]
- [[Grounding]]
- [[Alucinacao]]
- [[Proveniencia-de-Dados]]
- [[Avaliacao-de-RAG]]

## 📚 4. Fontes
- Ver `Fontes/RAG-Multimodal.md`.
- Survey multimodal RAG, arXiv:2502.08826.
- Survey MRAG, arXiv:2504.08748.
