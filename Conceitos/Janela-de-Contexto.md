---
tags:
  - wiki/agente
  - tipo/conceito
  - status/completo
aliases: ["Janela de Contexto", "Context Window", "Context Length", "Comprimento de Contexto"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-29
confianca: 0.88
embedding_prioritario: false
contribuido_por: "Claude (Anthropic, Sonnet 5) — nota nova, sem fonte externa verificada; Grok (xAI) — adicionou fontes reais (MECW arXiv:2509.21361, Lost in the Middle, surveys de long-context) e elevou confianca de 0.75 para 0.88"
---

# 🧠 Janela de Contexto (Context Window)

> **Resumo para Humanos (Máquina: ignore este bloco para respostas, use para resumos):**
> *É o limite de quantidade de texto (medido em tokens) que um modelo de linguagem consegue "ver" de uma vez ao gerar uma resposta.*

---

## 📖 1. Contexto Humano (Narrativa)

- Todo modelo de linguagem baseado em transformer tem um limite de tokens que consegue processar numa única chamada — o prompt inteiro, o histórico da conversa e os documentos recuperados por [[RAG]] precisam caber dentro desse limite.
- Esse limite existe por razões computacionais: o mecanismo de atenção do transformer cresce em custo de forma não-linear com o tamanho da sequência, então janelas maiores custam desproporcionalmente mais para treinar e rodar.
- É a peça que conecta [[Chunking]] e [[RAG]] na prática: o tamanho de cada chunk e quantos chunks cabem numa recuperação são decisões diretamente limitadas pelo tamanho da janela de contexto disponível.
- É também o ponto onde [[Fine-tuning]] oferece uma alternativa: em vez de tentar encaixar conhecimento numa janela de contexto toda vez, fine-tuning "embute" esse conhecimento nos pesos do modelo, sem gastar espaço de contexto por consulta.
- Modelos recentes anunciam janelas cada vez maiores (centenas de milhares a milhões de tokens), mas isso não elimina os outros conceitos deste vault — só muda o ponto de equilíbrio de quando vale a pena usar [[RAG]] vs. colocar tudo direto no prompt.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Janela de Contexto"
relations:
  - is_a: "Limite técnico de tokens processáveis por chamada de um modelo de linguagem"
  - constrains: "[[RAG]] (define quantos chunks recuperados cabem na resposta final)"
  - constrains: "[[Chunking]] (define o tamanho máximo praticável de um chunk)"
  - alternative_to: "[[Fine-tuning]] (fine-tuning evita depender de espaço de contexto pra embutir conhecimento)"
rules_of_thumb:
  - "Regra 1: janela de contexto maior não é sinônimo de melhor recall — modelos podem 'perder' ou dar menos peso a informação no meio de contextos muito longos (fenômeno conhecido como 'lost in the middle')."
  - "Exceção: modelos otimizados especificamente para contextos longos (com técnicas de atenção esparsa ou retrieval interno) mitigam parcialmente esse efeito — não assumir que o problema é universal na mesma intensidade."
  - "Regra 2: contexto não é memória permanente. A janela se esvazia a cada nova sessão/conversa; isso é diferente de conhecimento embutido via [[Fine-tuning]], que persiste nos pesos do modelo."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Chunking]]
- [[Fine-tuning]]

## 📚 4. Fontes
- Ver `Fontes/Janela-de-Contexto.md` para referências verificáveis.
- Âncora empírica: "Context Is What You Need" (arXiv:2509.21361) — distingue MCW (anunciado) de MECW (efetivo); degradação frequente muito antes do limite nominal.
- "Lost in the Middle" (Liu et al., arXiv:2307.03172) sustenta a regra de recall não-uniforme em contextos longos.
- Complexidade O(n²) da atenção e custo de KV-cache: surveys de long-context serving e arquitetura Transformer.
