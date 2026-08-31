---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Compressão de Contexto", "Prompt Compression", "LLMLingua", "LongLLMLingua", "Context compression"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-31
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #37; aprofundamento 2026-08-31 com LLMLingua + LongLLMLingua"
---

# 🗜️ Compressão de contexto

> **Resumo para Humanos:**
> Reduzir tokens do prompt/contexto **preservando o que a tarefa ainda precisa**,
> para caber na [[Janela-de-Contexto]], cortar custo e latência — sem virar
> “sumarizei e perdi a prova”.

---

## 📖 1. Contexto Humano (Narrativa)

Com few-shot, histórico longo, [[RAG]] e observações de tools, o contexto
incha. Três pressões: **limite de janela**, **custo por token** e **latência**.
Compressão ataca a densidade do input.

### Famílias de abordagem

1. **Heurística** — truncar head/tail, manter últimas k mensagens
2. **Seleção** — top-k trechos via [[Embeddings]] / [[Reranking]] (mais retrieval
   seletivo do que “compressão de string”)
3. **Sumarização** — LLM resume histórico; risco de drift factual
4. **Compressão aprendida** — modelo menor marca tokens pouco informativos e
   remove

**LLMLingua** (Jiang et al., arXiv:2310.05736, EMNLP 2023) é referência de
prompt compression com small LM + alinhamento; reporta compressões altas com
perda limitada em ICL/raciocínio nos experimentos do paper. **LongLLMLingua**
(arXiv:2310.06839, ACL 2024) foca cenários de contexto longo: custo, queda de
performance e *position bias*; busca melhorar a percepção da informação-chave
no prompt comprimido.

### Onde encaixa no pipeline

- **Antes do LLM final** — comprimir system+histórico+RAG empilhado
- **No retrieval** — menos chunks, melhor rank (complementa [[Reranking]])
- **Na memória** — comprimir archival/recall em [[Memoria-de-Agentes]]

### Riscos

- Apagar citação/evidência → quebra [[Grounding]] e auditoria
- Compressão agressiva em diálogo multi-turn → perde restrições do usuário
- Avaliar só perplexidade ≠ avaliar sucesso da tarefa

Compressão **não** substitui [[Cache-Semantico]] (reuso de resposta) nem um
[[RAG]] bem dimensionado. Meça qualidade *pós-compressão* com as mesmas
métricas de [[Avaliacao-de-RAG]] / tarefa agentic.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Compressão de prompts e contexto para LLMs"
relations:
  - is_a: "Redução de tokens com objetivo de utilidade da tarefa"
  - related_to: "[[Janela-de-Contexto]]"
  - related_to: "[[RAG]]"
  - related_to: "[[Chunking]]"
  - related_to: "[[Reranking]]"
  - related_to: "[[Grounding]]"
  - related_to: "[[Memoria-de-Agentes]]"
  - related_to: "[[Cache-Semantico]]"
  - related_to: "[[Avaliacao-de-RAG]]"
rules_of_thumb:
  - "Regra 1: Defina orçamento de tokens e métrica de tarefa antes de escolher o compressor."
  - "Regra 2: Preserve evidências necessárias ao grounding; se a citação some, a compressão falhou mesmo com JSON válido."
  - "Regra 3: Prefira seleção/rerank de trechos RAG antes de comprimir cegamente o prompt inteiro."
  - "Regra 4: Separe política de compressão de histórico vs. de documentos recuperados."
  - "Regra 5: Reavalie quando mudar modelo — compressores não transferem perfeitamente."
  - "Exceção: Volume baixo e janela folgada podem adiar compressão até haver telemetria de custo."
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
- [[Avaliacao-de-RAG]]

## 📚 4. Fontes
- Ver `Fontes/Compressao-de-Contexto.md`.
- LLMLingua, arXiv:2310.05736 (EMNLP 2023).
- LongLLMLingua, arXiv:2310.06839 (ACL 2024).
