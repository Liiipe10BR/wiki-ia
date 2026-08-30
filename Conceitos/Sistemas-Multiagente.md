---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Sistemas multiagente", "Multi-Agent", "MAS", "Multi-Agent LLM Systems", "Orquestração de agentes"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #15; nota nova sobre sistemas multiagente, com MAST (arXiv:2503.13657), AutoGen (arXiv:2308.08155) e protocolo A2A"
---

# 🧠 Sistemas Multiagente (MAS)

> **Resumo para Humanos:**
> Vários [[Agente-de-IA]] cooperam (ou competem) para um objetivo: um orquestra, um pesquisa, outro escreve, outro critica. Útil quando a tarefa tem papéis distintos; caro e frágil quando um único agente com ferramentas já resolveria.

---

## 📖 1. Contexto Humano (Narrativa)

Um [[Agente-de-IA]] é um loop Thought → Action → Observation. Um **sistema multiagente** é um conjunto desses loops com **papéis**, **canal de comunicação** e **regra de parada**. O ganho não vem de "mais LLMs", e sim de especialização (quem busca não é quem aprova) e de isolamento de contexto: cada agente vê só o recorte que cabe na [[Janela-de-Contexto]].

Isso **não** é automaticamente melhor que um agente só. O estudo MAST (Cemri et al., 2025) documentou que ganhos de MAS em benchmarks populares são frequentemente mínimos frente a um agente único bem desenhado. As falhas se agrupam em três famílias: especificação/desenho do sistema, desalinhamento entre agentes, e verificação/término da tarefa.

### Quando usar vários agentes (e quando não)

Use multiagente quando:
- a tarefa tem **papéis incompatíveis no mesmo prompt** (ex.: autor vs. revisor com critérios opostos);
- o trabalho precisa **partir contexto** (pesquisa longa + síntese + código) sem estourar a janela;
- há **ferramentas com permissões diferentes** (um agente lê a web, outro só escreve no repo, um terceiro só aprova);
- o caminho até a solução é **não linear** e falhas parciais devem ser isoladas.

Não use quando:
- um agente com [[Tool-Calling]] + [[RAG]] + orçamento de passos resolve o mesmo job;
- você não tem critério de "feito" nem observabilidade — MAS multiplica loops e custo sem um juiz;
- o único motivo é "parece mais inteligente". Custo, latência e [[Alucinacao]] compostos sobem juntos.

### Padrões de coordenação

- **Centralizado (orquestrador):** um agente raiz decompõe, despacha e agrega. Mais fácil de limitar, auditar e abortar. Gargalo e ponto único de falha.
- **Hierárquico:** orquestrador + suborquestradores por subtarefa (comum em pesquisa + redação + crítica). Combina isolamento com controle.
- **Descentralizado / conversacional:** agentes falam entre si (padrão AutoGen: agentes *conversable* com políticas de auto-reply e group chat). Flexível; mais sujeito a loops, deriva de objetivo e "conversa sem término".

Na prática de produção o desenho dominante é **orquestrador + especialistas**, não um bando simétrico.

### Papéis, comunicação e contexto

Papéis precisam de **contrato**: objetivo, entradas, saídas, ferramentas permitidas, o que *não* fazer. Sobreposição de papel é um modo de falha MAST (especificação).

Comunicação típica:
- mensagens em linguagem natural (barato de implementar, ambíguo);
- artefatos estruturados (JSON, patches, relatórios) — preferíveis na fronteira entre agentes;
- memória compartilhada (store, board, arquivos) — exige trava e proveniência, senão dois agentes reescrevem o mesmo estado;
- protocolos entre sistemas opacos: **A2A** (Agent2Agent, Linux Foundation; origem Google) padroniza descoberta (Agent Card), tarefas e artefatos. **MCP** continua sendo agente→ferramenta; A2A é agente→agente. Não são substitutos.

Contexto não deve ser "tudo para todos". Repassar o histórico inteiro explode custo e dilui o sinal (lost in the middle). Passe o *brief*, o artefato e a restrição; recupere o resto via [[RAG]] ou memória endereçável.

### Conflitos, erros e loops

Desalinhamento entre agentes: um entende "pronto" como rascunho, o outro como publicado; um inventa evidência e o próximo trata como fato. [[Alucinacao]] **propaga** se não houver verificação independente (ferramenta, teste, juiz com evidência — ver [[Avaliacao-de-RAG]] no caso de respostas fundamentadas).

Loops: debate sem critério de parada, retry cego, ping-pong de crítica. Sempre: teto de turnos **global** e **por agente**, timeout, circuit breaker, e um estado explícito `done | blocked | failed`.

Custo e latência são o produto de (agentes × turnos × tokens de contexto compartilhado). Paralelizar especialistas ajuda latência de relógio, não a conta de tokens.

### Limites, memória e observabilidade

Um MAS sem esses três vira caixa-preta cara:
- **limites:** ferramentas por papel, orçamento, o que pode mutar o mundo;
- **memória:** o que persiste entre turnos e quem pode escrever (e com [[Proveniencia-de-Dados]]);
- **observabilidade:** trace por agente (prompt, tools, mensagens, decisor de roteamento). Sem trace, MAST não é diagnosticável em produção.

Frameworks (AutoGen/AG2, CrewAI, LangGraph, Magentic-One, MetaGPT) mudam rápido; o que permanece é o desenho: papéis + canal + parada + verificação.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Sistemas multiagente (coordenação de vários agentes de IA)"
relations:
  - is_a: "Arquitetura de controle com dois ou mais [[Agente-de-IA]] e protocolo de coordenação"
  - depends_on: "[[Agente-de-IA]]"
  - depends_on: "[[Tool-Calling]]"
  - depends_on: "[[Janela-de-Contexto]]"
  - related_to: "[[Model-Context-Protocol]] (agente→ferramenta; complementar a A2A agente→agente)"
  - related_to: "[[Alucinacao]] (propaga entre agentes sem verificação)"
  - related_to: "[[Avaliacao-de-RAG]] (juiz e fidelidade quando há recuperação)"
  - related_to: "[[Proveniencia-de-Dados]] (quem produziu qual artefato)"
rules_of_thumb:
  - "Regra 1: Comece com um único agente + ferramentas. Só adicione um segundo agente quando houver papel, permissão ou contexto que não cabem no mesmo loop."
  - "Exceção: Autor vs. crítico com incentivos opostos é um caso em que dois papéis no mesmo prompt tendem a colapsar; aí a separação é o ponto."
  - "Regra 2: Prefira orquestrador central + especialistas a group chat simétrico em produção. É mais fácil impor teto de turnos, permissões e abort."
  - "Exceção: Exploração / brainstorm em ambiente sem efeito colateral pode usar conversa livre, ainda com teto global."
  - "Regra 3: Todo papel tem contrato escrito: objetivo, I/O, tools permitidas, critério de 'feito'. Sobreposição de papel é falha de especificação (MAST)."
  - "Regra 4: Não compartilhe o histórico inteiro. Passe brief + artefato + restrição; recupere o resto com [[RAG]] ou memória endereçável."
  - "Regra 5: Trate saída de outro agente como não confiável até verificação independente (teste, tool, juiz com evidência). Alucinação propaga."
  - "Regra 6: Defina teto de turnos global e por agente, timeout e estado terminal (done/blocked/failed). Sem isso o custo explode em loop."
  - "Regra 7: MCP não substitui protocolo agente–agente. Use MCP para tools; use A2A (ou um barramento interno) quando os agentes são sistemas opacos distintos."
  - "Regra 8: Sem trace por agente (mensagens, tools, roteamento) não dá para depurar MAS. Observabilidade é requisito, não extra."
```

---

## 🔗 3. Notas Relacionadas
- [[Agente-de-IA]]
- [[Tool-Calling]]
- [[Janela-de-Contexto]]
- [[Model-Context-Protocol]]
- [[Alucinacao]]
- [[Avaliacao-de-RAG]]
- [[RAG]]
- [[Proveniencia-de-Dados]]

## 📚 4. Fontes
- Ver `Fontes/Sistemas-Multiagente.md`.
- MAST / falhas de MAS: Cemri et al., "Why Do Multi-Agent LLM Systems Fail?", arXiv:2503.13657 (2025).
- Framework conversacional multiagente: Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", arXiv:2308.08155 (2023).
- Protocolo agente–agente: A2A (Agent2Agent), especificação e docs em https://a2a-protocol.org/ (Linux Foundation; iniciativa original Google).
