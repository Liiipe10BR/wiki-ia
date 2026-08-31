---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Compressão de Contexto", "Prompt Compression", "LLMLingua", "Context compression"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.91
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #37 / compressão de contexto e prompts"
---

# 🗜️ Compressão de contexto

> **Resumo para Humanos:**
> Reduzir o número de tokens enviados ao modelo **sem jogar fora** o que ainda
> importa para a tarefa — para caber na [[Janela-de-Contexto]], cortar custo e
> latência.

---

## 📖 1. Contexto Humano (Narrativa)

Prompts crescem com few-shot, histórico, [[RAG]] e tools. A janela tem limite;
o preço escala com tokens. **Compressão de contexto** tenta manter o sinal e
remover o ruído.

**LLMLingua** (Jiang et al., arXiv:2310.05736, EMNLP 2023) é referência de
*prompt compression* aprendida: um modelo menor estima importância de tokens e
remove os menos críticos, reportando compressões altas com perda limitada em
cenários de ICL e raciocínio nos experimentos do paper.

Outras famílias: sumarizar histórico; selecionar top-k trechos via
[[Embeddings]]/[[Reranking]]; truncar heurístico (head/tail). Risco comum:
**apagar a evidência** de que o [[Grounding]] dependia — a resposta fica
fluente e menos auditável.

Compressão **não** substitui retrieval bem feito nem [[Cache-Semantico]]. Em
[[Memoria-de-Agentes]], comprimir archival/recall é decisão de gestão de
memória, não só de prompt.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Compressão de prompts e contexto para LLMs"
relations:
  - is_a: "Técnica de redução de tokens preservando utilidade da tarefa"
  - related_to: "[[Janela-de-Contexto]]"
  - related_to: "[[RAG]]"
  - related_to: "[[Chunking]]"
  - related_to: "[[Reranking]]"
  - related_to: "[[Grounding]]"
  - related_to: "[[Memoria-de-Agentes]]"
  - related_to: "[[Cache-Semantico]]"
rules_of_thumb:
  - "Regra 1: Meça qualidade da tarefa *depois* de comprimir; compressão sem métrica é chute."
  - "Regra 2: Não comprima além do ponto em que some a citação/evidência necessária ao grounding."
  - "Regra 3: Prefira seleção/rerank de trechos recuperados antes de comprimir cegamente o prompt inteiro."
  - "Regra 4: Separe compressão de histórico de diálogo e compressão de corpus RAG — objetivos diferentes."
  - "Exceção: Demos com orçamento folgado podem enviar contexto completo até haver telemetria de custo."
```

---

## 🔗 3. Notas Relacionadas
- [[Janela-de-Contexto]]
- [[RAG]]
- [[Chunking]]
- [[Reranking]]
- [[Grounding]]
- [[Memoria-de-Agentes]]
- [[Cache-Semantico]]

## 📚 4. Fontes
- Ver `Fontes/Compressao-de-Contexto.md`.
- LLMLingua, arXiv:2310.05736 (EMNLP 2023).
