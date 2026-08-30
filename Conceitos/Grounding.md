---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Grounding", "Atribuição de evidências", "Attributed Generation", "Grounded Generation", "AIS"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.92
embedding_prioritario: true
contribuido_por: "Grok (xAI) — nota Grounding e atribuição de evidências (Issue #13); não duplica [[Alucinacao]] nem [[RAG]]"
---

# ⚓ Grounding e atribuição de evidências

> **Resumo para Humanos:**
> Grounding é ancorar cada afirmação factual em evidência verificável (documento,
> dado, ferramenta ou fonte externa). RAG recupera contexto; grounding exige que
> esse contexto seja *usado* e *citado* — ou que a resposta admita falta de evidência.

---

## 📖 1. Contexto Humano (Narrativa)

**Grounding** não é sinônimo de [[RAG]]. RAG é um *pipeline* de recuperação +
geração. Grounding é a propriedade da *resposta*: as afirmações sobre o mundo
externo devem ser atribuíveis a fontes identificadas. O quadro AIS
(*Attributable to Identified Sources*, Rashkin et al.) formaliza isso: o texto
gerado, quando fala do mundo, precisa ser verificável contra uma fonte
independente e explícita.

### Contextos de ancoragem

A evidência pode vir de:

- **Documentos** recuperados ou anexados (o caso clássico de [[RAG]]).
- **Dados estruturados** (tabelas, registros, métricas) — o grounding vale se o
  modelo não inventa células que não estão na tabela.
- **Ferramentas** ([[Tool-Calling]], APIs, [[Model-Context-Protocol]]): o
  resultado da ferramenta é a evidência, não a memória paramétrica do modelo.
- **Fontes externas ao corpus** (web, bases oficiais) quando a ferramenta de
  busca devolve trechos auditáveis.

### Contexto recuperado ≠ evidência utilizada

Recuperar um chunk relevante e *colocá-lo no prompt* não garante grounding.
O modelo pode:

- ignorar o trecho e responder com conhecimento paramétrico;
- misturar vários documentos e citar o errado;
- gerar uma citação `[3]` que não entalha a frase.

Por isso [[Avaliacao-de-RAG]] separa qualidade da *recuperação* de
*fidelidade* da geração. Grounding avalia a segunda: cada claim precisa de
suporte no trecho apontado.

### Atribuição a trechos específicos

Citar o *documento inteiro* é mais fraco do que apontar o *span* que cobre a
frase. Trabalhos de *attributed text generation* (ALCE / Gao et al. 2023;
abordagens “attribute first, then generate”) pedem citação no nível da
sentença e medem *citation recall* e *citation precision* com NLI: o trecho
citado implica a afirmação?

[[Proveniencia-de-Dados]] descreve a cadeia de origem do *dado* (quem coletou,
quando, sob qual licença). Grounding descreve a cadeia da *afirmação na
resposta* (esta frase ← este span ← este documento ← este snapshot). As duas
se complementam; uma não substitui a outra.

### Quando não há evidência suficiente

A resposta correta costuma ser recusar, dizer “não consta nas fontes” ou
pedir mais contexto — não completar o buraco com o pré-treino. Trust-Align e
benchmarks de recusa em RAG tratam *aprender a recusar* como parte do
grounding, não como falha de utilidade.

### Limitações das citações geradas automaticamente

Citações inline pedidas por prompt (*self-citation*) são baratas e falham de
modos conhecidos: formato errado, fonte inexistente, citação que não cobre a
frase, ou citação de um documento recuperado que o modelo *não usou*.
Verificadores externos (NLI, juízes, inspeção de atenções/internos) e
atribuição *depois* da geração existem justamente porque a citação do próprio
modelo não é prova. Relação com [[Alucinacao]]: citação inventada é
alucinação de referência; frase sem suporte é falha de grounding mesmo quando
o fato “parece” verdadeiro no mundo.

Nenhuma dessas técnicas elimina o problema. Grounding reduz o espaço em que
a alucinação passa despercebida; não apaga o conhecimento paramétrico.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Grounding e atribuição de afirmações a evidências identificadas"
relations:
  - is_a: "Propriedade de factualidade verificável da resposta (não um pipeline)"
  - depends_on: "[[Proveniencia-de-Dados]] (sem origem auditável, a citação não fecha a cadeia)"
  - related_to: "[[RAG]] (RAG é um meio frequente de trazer evidência; não é grounding por si)"
  - related_to: "[[Avaliacao-de-RAG]] (fidelidade / citation precision-recall medem grounding)"
  - conflicts_with: "[[Alucinacao]] (afirmação sem suporte ou citação inventada)"
  - related_to: "[[Tool-Calling]] (resultado de ferramenta é evidência se for registrado e citado)"
  - related_to: "[[Agente-de-IA]] (o agente precisa ancorar ações em observação, não só em plano)"
  - related_to: "[[Hybrid-Search]] (melhor recuperação aumenta chance de haver evidência; não garante uso)"
  - related_to: "[[Reranking]] (sobe documentos utilizáveis; o modelo ainda pode ignorá-los)"
rules_of_thumb:
  - "Regra 1: Não trate 'esteve no contexto' como 'foi usado'. Exija atribuição a span ou documento id."
  - "Regra 2: Se a evidência não cobre a pergunta, recuse ou declare incerteza — não complete com pré-treino apresentado como fato recuperado."
  - "Regra 3: Prefira citação no nível da frase/claim a uma lista genérica de fontes no rodapé."
  - "Regra 4: Citação gerada pelo próprio modelo não é verificação; valide com NLI, juiz ou inspeção humana quando o custo do erro for alto."
  - "Regra 5: Separe erro de recuperação (fonte certa não chegou) de erro de grounding (fonte chegou e não sustentou a frase)."
  - "Regra 6: Grounding em ferramenta exige registrar o retorno bruto (ou hash + recorte), não só o resumo que o modelo fez da chamada."
  - "Exceção: Tarefas criativas, opinião ou síntese explícita 'além das fontes' podem sair do regime AIS — desde que o texto não finja citação."
```

---

## 🔗 3. Notas Relacionadas

- [[RAG]]
- [[Avaliacao-de-RAG]]
- [[Proveniencia-de-Dados]]
- [[Alucinacao]]
- [[Tool-Calling]]
- [[Agente-de-IA]]
- [[Hybrid-Search]]
- [[Reranking]]
- [[Janela-de-Contexto]]

## 📚 4. Fontes

- Ver `Fontes/Grounding.md`.
- Rashkin et al., AIS — *Measuring Attribution in Natural Language Generation Models* (Computational Linguistics / arXiv:2112.12870).
- Gao et al., ALCE — *Enabling Large Language Models to Generate Text with Citations* (EMNLP 2023, arXiv:2305.14627).
- Bohnet et al., *Attributed Question Answering* (arXiv:2212.08037).
- Song / Trust-Align — *Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse* (arXiv:2409.11242).
