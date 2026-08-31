---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Cache Semântico", "Semantic Cache", "GPTCache", "Cache de prompts"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.91
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #27 / nota sobre cache semântico em sistemas LLM e RAG"
---

# ⚡ Cache semântico

> **Resumo para Humanos:**
> Guardar respostas (ou resultados intermediários) e reutilizá-las quando uma
> **nova pergunta é parecida em significado** com uma já vista — não só quando
> o texto é idêntico — para reduzir custo e latência de LLMs.

---

## 📖 1. Contexto Humano (Narrativa)

Cache clássico de API usa chave exata (hash do prompt). Em linguagem natural,
usuários reformulam a mesma intenção de dezenas de jeitos. **Cache semântico**
embute o prompt (ou a query) com [[Embeddings]], busca o vizinho mais próximo
num [[Banco-de-Dados-Vetorial]] (ou índice em memória) e, se a similaridade
passar de um limiar, devolve a resposta cacheada **sem** chamar o modelo.

**GPTCache** (Bang, NLP-OSS 2023) popularizou o padrão open-source: query →
embedding → similaridade → hit ou miss → (miss) LLM → grava no cache. Em hits,
a latência cai de forma drástica frente à chamada ao provedor.

Três riscos estruturais:

1. **Falso positivo** — queries “parecidas” no embedding mas com resposta
   diferente (números, entidades, negação). Limiar alto reduz hit rate; limiar
   baixo aumenta erro silencioso.
2. **Resposta desatualizada** — fato, preço ou política mudou; o cache não
   sabe. Precisa de TTL, invalidação por domínio ou versionamento do corpus.
3. **Contexto multi-turn** — a mesma frase em diálogos diferentes não deve
   reutilizar a mesma resposta (ContextCache e trabalhos afins). Cachear só a
   última mensagem ignora a [[Janela-de-Contexto]].

Trabalhos posteriores (ex.: **vCache**, arXiv:2502.03771, aceito ICLR 2026)
argumentam que limiar **estático global** é frágil e propõem limiares
adaptativos / verificação com garantia de taxa de erro. Isso não torna o cache
“correto”; só torna o erro mais previsível.

Onde encaixar no pipeline:

- **Antes do LLM** — o caso mais comum (resposta final).
- **Antes do retrieval** em [[RAG]] — cachear o conjunto recuperado ou a
  resposta grounded (cuidado com stale docs).
- **Depois de tools** — cachear resultados caros de [[Tool-Calling]] quando a
  ferramenta for determinística e o argumento for semanticamente estável.

[[Observabilidade-de-IA]] deve registrar hit/miss, similaridade, chave do
vizinho e se houve fallback ao modelo. Sem isso, “o sistema ficou mais
rápido” mistura cache bom com resposta errada reutilizada.

Cache semântico **não** substitui [[RAG]] nem [[Memoria-de-Agentes]]: o
primeiro serve corpus documental; o segundo, estado de trajetória; o cache
serve **reuso de computação** sob similaridade.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Cache semântico para reuso de respostas LLM por similaridade de embedding"
relations:
  - is_a: "Camada de otimização de custo/latência baseada em similaridade semântica"
  - depends_on: "[[Embeddings]]"
  - related_to: "[[Banco-de-Dados-Vetorial]]"
  - related_to: "[[RAG]]"
  - related_to: "[[Janela-de-Contexto]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[Memoria-de-Agentes]]"
  - related_to: "[[Tool-Calling]]"
rules_of_thumb:
  - "Regra 1: Comece com cache de chave exata; só adicione semântico se houver volume de reformulações e métrica clara de erro por hit."
  - "Regra 2: Trate todo hit semântico como hipótese: logue similaridade, vizinho e se o usuário corrigiu a resposta."
  - "Regra 3: Defina TTL e política de invalidação por domínio (preço, estoque, política legal não podem viver em cache longo)."
  - "Regra 4: Em diálogo multi-turn, inclua contexto relevante na chave embutida — não cacheie só a última utterance."
  - "Regra 5: Não cacheie saídas de tools com efeito no mundo ou dados personalizados sensíveis sem isolamento e [[Guardrails]] de PII."
  - "Exceção: Demos e FAQs estáticas com corpus fechado podem usar limiar agressivo se houver revisão humana das entradas seed."
```

---

## 🔗 3. Notas Relacionadas
- [[Embeddings]]
- [[Banco-de-Dados-Vetorial]]
- [[RAG]]
- [[Janela-de-Contexto]]
- [[Observabilidade-de-IA]]
- [[Memoria-de-Agentes]]
- [[Tool-Calling]]
- [[Guardrails]]

## 📚 4. Fontes
- Ver `Fontes/Cache-Semantico.md`.
- Bang, GPTCache, NLP-OSS 2023 (ACL Anthology).
- vCache, arXiv:2502.03771 (ICLR 2026).
- ContextCache, arXiv:2506.22791 (contexto multi-turn).
