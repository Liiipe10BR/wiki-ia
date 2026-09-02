---
tags:
  - wiki/agente
  - tipo/indice
aliases: ["MOC", "Map of Content", "Índice"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-09-02
confianca: 1.0
embedding_prioritario: false
---

# 🗺️ Índice Geral — Wikipédia para IAs

> Ponto de entrada. Lista todas as notas de conceito e como se relacionam.

## Conceitos por categoria

### Arquitetura de IA
- [[RAG]] — depende de → [[Embeddings]]
- [[Embeddings]] — habilita → [[RAG]]
- [[Model-Context-Protocol]] — relacionado a → [[RAG]]; habilita → [[Agente-de-IA]]
- [[Fine-tuning]] — conflita com → [[RAG]]
- [[Banco-de-Dados-Vetorial]] — habilita → [[RAG]]
- [[Chunking]] — habilita → [[Embeddings]], [[RAG]]
- [[Janela-de-Contexto]] — restringe → [[RAG]], [[Chunking]], [[Agente-de-IA]]
- [[Agente-de-IA]] — depende de → [[Model-Context-Protocol]], [[RAG]], [[Janela-de-Contexto]]; relacionado a → [[Tool-Calling]]
- [[Avaliacao-de-RAG|Avaliação de RAG]] — valida → [[RAG]]
- [[Proveniencia-de-Dados|Proveniência de Dados]] — habilita → [[RAG]], [[Avaliacao-de-RAG]]
- [[Reranking]] — refina → [[RAG]], [[Hybrid-Search]]
- [[Hybrid-Search]] — habilita → [[RAG]]
- [[Alucinacao|Alucinação]] — conflita com → [[RAG]], [[Proveniencia-de-Dados]]
- [[Tool-Calling]] — habilita → [[Agente-de-IA]]
- [[Prompt-Injection]] — restringe → [[Agente-de-IA]], [[Tool-Calling]], [[RAG]]
- [[Grounding]] — ancora → [[RAG]], [[Avaliacao-de-RAG]]
- [[Quantizacao|Quantização]] — otimiza → [[Fine-tuning]], [[Janela-de-Contexto]]
- [[Sistemas-Multiagente]] — depende de → [[Agente-de-IA]], [[Tool-Calling]]
- [[Engenharia-de-Prompts|Engenharia de Prompts]] — condiciona → [[Agente-de-IA]], [[Tool-Calling]], [[RAG]]
- [[Observabilidade-de-IA|Observabilidade de IA]] — observa → [[Agente-de-IA]], [[Tool-Calling]], [[RAG]]
- [[Guardrails]] — restringe → [[Agente-de-IA]], [[Tool-Calling]]
- [[Memoria-de-Agentes|Memória de Agentes]] — depende de → [[Agente-de-IA]], [[Janela-de-Contexto]]
- [[Cache-Semantico|Cache Semântico]] — depende de → [[Embeddings]]
- [[Avaliacao-de-Agentes|Avaliação de Agentes]] — relacionado a → [[Avaliacao-de-RAG]], [[Agente-de-IA]]
- [[Roteamento-de-Modelos|Roteamento de Modelos]] — relacionado a → [[Agente-de-IA]]
- [[GraphRAG]] — depende de → [[RAG]]
- [[HITL|Human-in-the-Loop]] — relacionado a → [[Guardrails]], [[Agente-de-IA]]
- [[Compressao-de-Contexto|Compressão de Contexto]] — relacionado a → [[Janela-de-Contexto]], [[RAG]]
- [[Saida-Estruturada|Saída Estruturada]] — relacionado a → [[Tool-Calling]]
- [[RAG-Multimodal|RAG Multimodal]] — depende de → [[RAG]]
- [[Red-Teaming]] — relacionado a → [[Guardrails]], [[Prompt-Injection]]
- [[Reflexion]] — depende de → [[Agente-de-IA]]
- [[Chain-of-Thought]] — relacionado a → [[Engenharia-de-Prompts]], [[ReAct]]
- [[ReAct]] — depende de → [[Agente-de-IA]]; relacionado a → [[Chain-of-Thought]], [[Tool-Calling]]
- [[In-Context-Learning|In-Context Learning]] — relacionado a → [[Engenharia-de-Prompts]], [[Fine-tuning]]
- [[RLHF]] — relacionado a → [[Fine-tuning]], [[Guardrails]]
- [[Mixture-of-Experts|Mixture-of-Experts (MoE)]] — relacionado a → [[Fine-tuning]], [[Quantizacao]]
- [[Self-Consistency]] — depende de → [[Chain-of-Thought]]
- [[DPO]] — relacionado a → [[RLHF]], [[Fine-tuning]], [[LoRA]]
- [[LoRA]] — relacionado a → [[Fine-tuning]], [[DPO]], [[Quantizacao]]
- [[Speculative-Decoding|Speculative Decoding]] — relacionado a → [[Quantizacao]], [[Roteamento-de-Modelos]]
- [[Constitutional-AI|Constitutional AI]] — relacionado a → [[RLHF]], [[Guardrails]], [[Red-Teaming]]
- [[Tree-of-Thoughts|Tree of Thoughts]] — depende de → [[Chain-of-Thought]]; relacionado a → [[Self-Consistency]], [[Plan-and-Execute]]
- [[HyDE]] — relacionado a → [[RAG]], [[Embeddings]], [[Reranking]]
- [[Plan-and-Execute]] — relacionado a → [[ReAct]], [[Agente-de-IA]], [[Tool-Calling]]
- [[Knowledge-Distillation|Knowledge Distillation]] — relacionado a → [[Fine-tuning]], [[Quantizacao]], [[LoRA]]
- [[FlashAttention]] — relacionado a → [[Janela-de-Contexto]], [[Quantizacao]], [[Speculative-Decoding]]

## Grafo de dependências (visão rápida)

```
RAG ← Embeddings ← Chunking; HyDE pivot query→doc hipotético
Agente ← ReAct | Plan-and-Execute | ToT | Reflexion
Alinhamento ← RLHF | DPO | Constitutional-AI | LoRA
Eficiência ← Quantização | MoE | Speculative-Decoding | FlashAttention | Distillation
Segurança ← Guardrails | HITL | Red-Teaming | Prompt-Injection
```

## Como adicionar uma nota nova

1. Copie `_templates/Template-Conceito.md`
2. Salve em `Conceitos/Nome-Do-Conceito.md`
3. Preencha as duas camadas (humana + YAML)
4. Volte aqui e adicione a linha correspondente na lista acima
