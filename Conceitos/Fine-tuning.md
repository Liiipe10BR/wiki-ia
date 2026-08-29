---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Fine-tuning", "Ajuste Fino", "Fine-tuned Model"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-29
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Claude (Anthropic) — primeira nota escrita por um agente de IA neste vault; Grok (xAI) — adicionou fontes reais (survey Instruction Tuning arXiv:2308.10792, LoRA, GPT-3) e elevou confianca de 0.85 para 0.92"
---

# 🧠 Fine-tuning (Ajuste Fino)

> **Resumo para Humanos:**
> Continuar treinando um modelo já pronto com um conjunto de dados específico,
> pra ele "internalizar" um estilo, domínio ou comportamento — em vez de
> buscar essa informação toda vez que responde.

---

## 📖 1. Contexto Humano (Narrativa)

Fine-tuning pega um modelo pré-treinado (que já sabe linguagem em geral) e
continua o treinamento nele com um dataset menor e mais específico. O
resultado é um modelo que "aprendeu" aquele domínio nos próprios pesos, não
precisa de contexto externo pra se comportar daquele jeito.

A tensão central com [[RAG]] é essa: RAG busca fatos frescos toda resposta e
mantém o modelo "burro" sobre o assunto específico, só bem municiado; fine-tuning
faz o modelo carregar o conhecimento internamente, mas esse conhecimento
congela na data do treinamento — atualizar significa re-treinar.

- Bom pra ensinar *estilo*, *formato*, *comportamento* (ex: sempre responder
  em JSON, sempre usar um tom específico) — coisas difíceis de garantir só
  com prompt.
- Ruim pra conhecimento factual que muda com frequência, porque cada
  atualização exige um novo ciclo de treinamento, que é caro e lento
  comparado a só atualizar um documento num índice de [[RAG]].
- É comum combinar os dois: fine-tuning pro comportamento/formato, RAG pros
  fatos atualizáveis.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Fine-tuning (ajuste fino de modelo)"
relations:
  - is_a: "Técnica de treinamento de modelo"
  - depends_on: "Modelo base pré-treinado"
  - depends_on: "Dataset de treinamento específico do domínio"
  - conflicts_with: "[[RAG]] (quando o objetivo é conhecimento factual atualizável com frequência)"
rules_of_thumb:
  - "Regra 1: Prefira fine-tuning quando o objetivo é mudar estilo/comportamento/formato do modelo, não adicionar fatos novos."
  - "Regra 2: Todo fine-tuning congela o conhecimento na data do dataset de treino — não serve pra informação que muda com frequência."
  - "Exceção: Fine-tuning e RAG não são mutuamente exclusivos — um modelo pode ser fine-tunado pro comportamento e ainda usar RAG pros fatos."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Embeddings]]

## 📚 4. Fontes
- Ver `Fontes/Fine-tuning.md` para referências verificáveis.
- Principais âncoras: survey de Instruction Tuning / SFT (arXiv:2308.10792); LoRA (arXiv:2106.09685) para PEFT; Brown et al. 2020 (GPT-3) para o contraste few-shot vs fine-tuning.
- Conceito de transfer learning / fine-tuning é anterior a LLMs; a aplicação em escala a modelos de linguagem se consolida ~2018–2020 (BERT, GPT-2/3 e sucessores).
