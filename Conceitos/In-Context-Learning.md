---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["In-Context Learning", "ICL", "Few-shot", "Zero-shot", "Aprendizado in-context"]
data_criacao: 2026-09-01
ultima_verificacao: 2026-09-01
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — nota In-Context Learning (Brown et al. / GPT-3)"
---

# 📚 In-Context Learning (ICL)

> **Resumo para Humanos:**
> O modelo **aprende a tarefa a partir do prompt** (instruções e/ou exemplos),
> **sem atualizar pesos** — zero-shot, one-shot ou few-shot.

---

## 📖 1. Contexto Humano (Narrativa)

**Language Models are Few-Shot Learners** (Brown et al., arXiv:2005.14165)
popularizou a ideia de que modelos grandes executam tarefas novas só com texto
de demonstração no contexto. GPT-3 foi avaliado em zero/one/few-shot *sem*
gradient update: a “programação” é o próprio prompt.

### Espectro

| Modo | O que vai no prompt |
|------|---------------------|
| **Zero-shot** | Só instrução |
| **One-shot** | Instrução + 1 exemplo |
| **Few-shot** | Instrução + k exemplos |

[[Chain-of-Thought]] é ICL em que os exemplares incluem **raciocínio**, não só
pares entrada/saída. [[RAG]] pode ser visto como ICL em que os “exemplos” são
passagens recuperadas (não necessariamente rotuladas como demos de tarefa).

### ICL vs [[Fine-tuning]]

| | ICL | Fine-tuning |
|--|-----|-------------|
| Pesos | Congelados | Atualizados |
| Custo marginal | Tokens no prompt | Treino + serving do adaptador/modelo |
| Troca de tarefa | Rápida (muda prompt) | Novo treino / adapter |
| Limite | [[Janela-de-Contexto]] | Dados e overfitting |

Na prática: ICL para iterar e tarefas dinâmicas; fine-tuning (ou LoRA) quando o
padrão é estável e o volume justifica.

### Limites

- Exemplos ruins ou enviesados → comportamento ruim
- Sensível a ordem e formato dos shots
- Compete por espaço com histórico, tools e RAG

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "In-Context Learning (zero/few-shot sem update de pesos)"
relations:
  - is_a: "Adaptação de tarefa via prompt sem gradient update"
  - related_to: "[[Engenharia-de-Prompts]]"
  - related_to: "[[Chain-of-Thought]]"
  - related_to: "[[Fine-tuning]]"
  - related_to: "[[Janela-de-Contexto]]"
  - related_to: "[[RAG]]"
  - related_to: "[[Compressao-de-Contexto]]"
rules_of_thumb:
  - "Regra 1: Escolha exemplares representativos e no formato de saída desejado."
  - "Regra 2: Meça se few-shot ganha de zero-shot o suficiente para pagar os tokens."
  - "Regra 3: Se a política de exemplos for estável e crítica, considere fine-tuning."
  - "Regra 4: Documente ordem e seleção dos shots — ICL é sensível a isso."
  - "Exceção: Modelos já instruction-tuned fortes podem bastar com zero-shot bem escrito."
```

---

## 🔗 3. Notas Relacionadas
- [[Engenharia-de-Prompts]]
- [[Chain-of-Thought]]
- [[Fine-tuning]]
- [[Janela-de-Contexto]]
- [[RAG]]
- [[Compressao-de-Contexto]]

## 📚 4. Fontes
- Ver `Fontes/In-Context-Learning.md`.
- Brown et al., arXiv:2005.14165.
