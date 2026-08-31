---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Memória de Agentes", "Agent Memory", "Memória de agente", "Memória episódica", "Memória de longo prazo"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #25 / nota sobre memória de agentes de IA (persistência, hierarquia, write–manage–read)"
---

# 🧠 Memória de agentes

> **Resumo para Humanos:**
> Como um agente de IA **persiste, organiza e recupera** informação além da
> janela de contexto — para não recomeçar do zero a cada turno ou sessão.

---

## 📖 1. Contexto Humano (Narrativa)

Um [[Agente-de-IA]] sem memória é, na prática, um gerador de texto com tools:
cada chamada depende só do que cabe na [[Janela-de-Contexto]]. Em tarefas
longas, multi-sessão ou multiagente, isso estoura rápido. **Memória de
agentes** é o conjunto de mecanismos que gravam o que aconteceu, o que foi
aprendido e o que não deve se repetir — e que devolvem isso de forma seletiva
quando a decisão precisa.

Isso **não é o mesmo** que [[RAG]] sobre um corpus fixo de documentos. RAG
recupera conhecimento externo (manuais, tickets, papers). Memória de agente
recupera (e escreve) **estado da trajetória**: preferências do usuário,
resultados de tools, falhas já vistas, skills consolidadas, resumos de
sessões anteriores. Os dois podem compartilhar a mesma infraestrutura
(vetorial, híbrida, grafo), mas o *ciclo de escrita* e a política de
esquecimento são o diferencial.

Surveys recentes formalizam memória como um loop **write → manage → read**,
acopado a percepção e ação (Du, arXiv:2603.07670). Outra linha (Huang et al.,
arXiv:2602.06052, TMLR) organiza o campo em três eixos: *substrato*
(paramétrico interno vs. store externo), *mecanismo cognitivo* (working,
episódica, semântica, procedural) e *sujeito* (personalização do usuário vs.
experiência do próprio agente).

### Hierarquia prática (inspirada em SO / MemGPT)

**MemGPT** (Packer et al., arXiv:2310.08560) popularizou a analogia com
sistema operacional: a janela de contexto é “RAM”; o resto é “disco” paginado
com tools de leitura/escrita. A arquitetura de produção derivada (Letta)
distingue de forma útil:

1. **Memória in-context (core)** — blocos editáveis que *sempre* entram no
   prompt (persona, fatos do usuário, estado da tarefa).
2. **Recall / histórico** — mensagens antigas ejetadas da janela, buscáveis.
3. **Archival / longa duração** — store semântico ou estruturado para fatos e
   experiências que sobrevivem a muitas sessões.

O ponto crítico não é só *armazenar*: é **quem decide** o que entra, o que
sai e o que se consolida. Em designs *self-editing*, o próprio modelo chama
tools (`memory_insert`, `memory_replace`, busca archival). Em outros, um
orquestrador externo comprime, filtra e injeta. Os dois coexistam; nenhum
elimina alucinação de memória nem contradição entre fatos gravados.

### Famílias de mecanismo (visão unificada)

Sem eleger um produto:

- **Compressão residente no contexto** — sumários, sliding window, “lost in
  the middle” como risco (ligado a [[Janela-de-Contexto]] e [[Engenharia-de-Prompts]]).
- **Stores com retrieval** — vetorial / hybrid / grafo; overlap com [[RAG]],
  mas com políticas de escrita contínua.
- **Reflexão e consolidação** — transformar trajetórias em lições (ex.:
  reflexion-style); risco de “lição” falsa se a avaliação for fraca.
- **Contexto virtual hierárquico** — paging estilo MemGPT entre tiers.
- **Políticas aprendidas** — roteamento e write-path como objeto de treino
  (ainda emergente; não tratar como padrão estável de produção).

Em [[Sistemas-Multiagente]], memória compartilhável vira coordenação e também
risco: um agente pode poluir o store comum com estado errado. Em qualquer
desenho, [[Observabilidade-de-IA]] (o que foi lido/escrito, com qual
confiança) e [[Guardrails]] (o que *pode* ser memorizado — PII, segredos)
deixam de ser opcionais.

Limitações honestas: benchmarks de *recall* estático não medem bem utilidade
em tarefas multi-sessão; consolidação contínua e *forgetting* confiável
continuam abertos nos surveys de 2026; memória multimodal e embodied é
fronteira, não commodity.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Memória de agentes de IA — persistência e recuperação além da janela de contexto"
relations:
  - is_a: "Mecanismo de estado de longo prazo para agentes baseados em LLM"
  - depends_on: "[[Agente-de-IA]]"
  - depends_on: "[[Janela-de-Contexto]]"
  - related_to: "[[RAG]]"
  - related_to: "[[Embeddings]]"
  - related_to: "[[Banco-de-Dados-Vetorial]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Sistemas-Multiagente]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Proveniencia-de-Dados]]"
  - related_to: "[[Engenharia-de-Prompts]]"
rules_of_thumb:
  - "Regra 1: Separe memória de trajetória (o que o agente e o usuário fizeram) de corpus RAG (documentação externa). Políticas de escrita, TTL e acesso diferem."
  - "Regra 2: Trate memória como write–manage–read: gravar sem política de consolidação/esquecimento vira lixo recuperável e contradição."
  - "Regra 3: O que precisa estar sempre disponível vai para blocos in-context (core); o resto é buscável sob demanda — não encha a janela."
  - "Regra 4: Memória self-editing via tools exige validação (schema, tamanho, PII) igual a qualquer Tool-Calling; o modelo pode gravar fato falso com alta confiança."
  - "Regra 5: Em multiagente, defina store compartilhado vs. privado; sem isso, um agente contamina o estado dos outros."
  - "Regra 6: Avalie memória em tarefas multi-sessão e de decisão, não só em recall de frases; regresse custo e latência do retrieval de memória."
  - "Exceção: Chat de uma sessão, sem personalização e sem tools de efeito no mundo, pode viver só com histórico na janela + sumário leve."
```

---

## 🔗 3. Notas Relacionadas
- [[Agente-de-IA]]
- [[Janela-de-Contexto]]
- [[RAG]]
- [[Embeddings]]
- [[Banco-de-Dados-Vetorial]]
- [[Tool-Calling]]
- [[Sistemas-Multiagente]]
- [[Observabilidade-de-IA]]
- [[Guardrails]]
- [[Proveniencia-de-Dados]]
- [[Engenharia-de-Prompts]]

## 📚 4. Fontes
- Ver `Fontes/Memoria-de-Agentes.md`.
- Packer et al., MemGPT, arXiv:2310.08560.
- Du, *Memory for Autonomous LLM Agents*, arXiv:2603.07670 (2026).
- Huang et al., *A Survey of Agent Memory in the Second Half*, arXiv:2602.06052 (TMLR).
- Documentação Letta (arquitetura MemGPT / core vs archival).
