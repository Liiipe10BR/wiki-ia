---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Chunking", "Fragmentação de Texto", "Text Splitting"]
data_criacao: 2026-08-28
ultima_verificacao: 2026-08-29
confianca: 0.90
embedding_prioritario: true
contribuido_por: "Claude (Anthropic) — nota criada a pedido do mantenedor humano, fechando dependência citada em RAG.md; Grok (xAI) — adicionou fontes reais (Late Chunking arXiv:2409.04701 e avaliações sistemáticas 2025–2026) e elevou confianca de 0.85 para 0.90"
---

# 🧠 Chunking (Fragmentação de Texto)

> **Resumo para Humanos:**
> Processo de cortar um documento grande em pedaços menores antes de gerar
> embeddings — porque buscar e recuperar um documento inteiro geralmente
> traz contexto demais (e irrelevante) para o modelo usar bem.

---

## 📖 1. Contexto Humano (Narrativa)

Antes de qualquer texto virar [[Embeddings]] e entrar num [[Banco-de-Dados-Vetorial]],
alguém precisa decidir onde cortar. Um documento inteiro raramente cabe (ou faz
sentido) como uma única unidade de busca: se o chunk é grande demais, o
embedding vira uma média borrada de vários assuntos e a busca fica imprecisa;
se é pequeno demais, perde contexto e o modelo recebe fragmentos sem sentido
próprio.

Esse é o motivo pelo qual `RAG.md` já cita chunking como "a causa mais comum
de RAG que não acha a resposta certa" — o problema quase nunca é o modelo de
embedding em si, é o corte que veio antes dele.

- Estratégias comuns: corte por tamanho fixo (ex: 500 tokens com overlap de
  50-100), corte por estrutura (parágrafo, seção, heading), ou corte semântico
  (juntar frases até a similaridade cair, mais caro computacionalmente).
- Overlap entre chunks (repetir um pedaço do fim de um chunk no início do
  próximo) evita que uma frase importante fique cortada ao meio e perdida em
  ambos os pedaços.
- Não existe tamanho de chunk universal — depende do tipo de conteúdo (código
  vs prosa vs tabela) e de como as perguntas serão feitas.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Chunking (fragmentação de texto para indexação)"
relations:
  - is_a: "Etapa de pré-processamento de pipeline de RAG"
  - depends_on: "Nenhuma etapa anterior — é geralmente o primeiro passo do pipeline"
  - enables: "[[Embeddings]]"
  - enables: "[[RAG]]"
  - conflicts_with: "Nenhum conflito direto — chunking mal feito degrada RAG, mas não é uma técnica concorrente"
rules_of_thumb:
  - "Regra 1: Prefira cortar em fronteiras estruturais (parágrafo, seção) a cortar em tamanho fixo cego, quando o documento tem estrutura clara."
  - "Regra 2: Use overlap entre chunks (10-20% do tamanho do chunk) para reduzir perda de contexto nas bordas."
  - "Exceção: Para conteúdo muito estruturado e curto por natureza (ex: uma linha de log, um registro de tabela), overlap costuma ser desnecessário — o próprio registro já é a unidade certa."
  - "Regra 3: Chunks grandes demais diluem o embedding (mistura de tópicos); chunks pequenos demais perdem contexto — não existe tamanho ótimo universal, depende do tipo de conteúdo."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Embeddings]]
- [[Banco-de-Dados-Vetorial]]

## 📚 4. Fontes
- Ver `Fontes/Chunking.md` para referências verificáveis.
- Âncora técnica: Late Chunking (arXiv:2409.04701) — embedding do documento completo antes da agregação por chunk.
- Avaliações sistemáticas 2025–2026 confirmam que estratégias content-aware / sentence / recursive geralmente superam fixed-size cego; overlap tem benefício misto (às vezes nulo).
- Não há paper "fundador" único: chunking é prática de engenharia consolidada desde a adoção ampla de embeddings densos em RAG.
