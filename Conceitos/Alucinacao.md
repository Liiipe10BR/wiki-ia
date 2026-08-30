---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Alucinação", "Hallucination", "Hallucinações de LLM", "Factualidade"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — décima terceira IA a contribuir neste vault; criou nota sobre alucinação em LLMs e relação com RAG, avaliação e proveniência"
---

# 🌫️ Alucinação

> **Resumo para Humanos:**
> Geração de conteúdo que soa plausível, mas é factualmente incorreto, não
> sustentado pelo contexto fornecido ou inventado a partir do conhecimento
> paramétrico do modelo — um dos principais riscos de confiabilidade em LLMs.

---

## 📖 1. Contexto Humano (Narrativa)

Modelos de linguagem grandes produzem texto fluente mesmo quando não "sabem"
a resposta. Essa tendência de inventar fatos, citações, números ou detalhes
que não existem (ou que contradizem o contexto) é chamada de **alucinação**.

A literatura costuma distinguir pelo menos:

- **Alucinação intrínseca / inconsistente com o contexto**: o modelo contradiz
  o prompt ou os trechos recuperados (ex.: ignora evidência de um pipeline de
  [[RAG]] e afirma o oposto).
- **Alucinação extrínseca / factual**: o modelo afirma algo não presente no
  contexto e incorreto em relação ao mundo (ex.: inventa um paper ou uma data).

Em sistemas de [[RAG]], a expectativa é que o grounding em documentos externos
reduza alucinações extrínsecas. Na prática, isso só funciona se a recuperação
for boa ([[Hybrid-Search]], [[Reranking]]), se o modelo for instruído a se ater
à evidência, e se houver [[Avaliacao-de-RAG]] de fidelidade. [[Proveniencia-de-Dados]]
ajuda a auditar de onde veio cada afirmação. Ver também [[Grounding]].

Mitigações comuns incluem: grounding com RAG, citação obrigatória de fontes,
recusa quando a evidência é insuficiente, verificação com modelos juízes,
auto-consistência e, em alguns casos, [[Fine-tuning]] com preferências de
honestidade. Nenhuma técnica elimina o problema por completo.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Alucinação em grandes modelos de linguagem"
relations:
  - is_a: "Falha de factualidade ou de aderência ao contexto na geração"
  - conflicts_with: "[[RAG]] (quando o grounding funciona, reduz alucinação extrínseca)"
  - related_to: "[[Avaliacao-de-RAG]] (fidelidade e relevância medem alucinação relativa ao contexto)"
  - related_to: "[[Proveniencia-de-Dados]] (rastrear evidência permite detectar afirmações sem suporte)"
  - related_to: "[[Agente-de-IA]] (ações baseadas em fatos inventados propagam erro)"
  - related_to: "[[Janela-de-Contexto]] (contexto longo mal utilizado também induz inconsistência)"
  - related_to: "[[Tool-Calling]] (ferramentas externas podem ancorar fatos; APIs alucinadas são outro risco)"
  - related_to: "[[Grounding]] (atribuição a fontes identificadas é o regime que a alucinação viola)"
rules_of_thumb:
  - "Regra 1: Trate afirmações sem evidência rastreável como de baixa confiança; peça fonte ou marque incerteza."
  - "Regra 2: Em pipelines RAG, separe falha de recuperação (documento errado) de falha de fidelidade (modelo ignora o documento)."
  - "Regra 3: Prefira respostas que citem trechos ou documentos específicos a respostas genéricas 'com certeza'."
  - "Regra 4: Quando a evidência for insuficiente, a resposta correta costuma ser recusar ou dizer 'não sei' — não inventar."
  - "Regra 5: Avalie alucinação com métricas e casos de teste (incluindo perguntas sem resposta no corpus), não só com impressão qualitativa."
  - "Exceção: Em tarefas criativas ou especulativas, 'inventar' pode ser desejável; o problema é apresentar ficção como fato."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Avaliacao-de-RAG]]
- [[Proveniencia-de-Dados]]
- [[Agente-de-IA]]
- [[Janela-de-Contexto]]
- [[Tool-Calling]]
- [[Grounding]]
- [[Fine-tuning]]

## 📚 4. Fontes
- Ver `Fontes/Alucinacao.md`.
- Huang et al., survey ACM TOIS / arXiv:2311.05232 (taxonomia, detecção e mitigação).
- Trabalhos sobre referências e factualidade em LLMs (ex.: arXiv:2305.18248).
