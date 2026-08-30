---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Grounding", "Atribuição de Evidências", "Attributed Generation", "Ancoragem em Evidência"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.93
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #13; nota sobre grounding e atribuição de evidências (distinto de RAG)"
---

# ⚓ Grounding

> **Resumo para Humanos:**
> Prática de ancorar afirmações da IA em evidências verificáveis (documentos,
> dados, ferramentas) e, quando possível, **atribuir** cada trecho a uma fonte
> específica — sem confundir "ter recuperado contexto" com "ter usado a
> evidência de forma fiel".

---

## 📖 1. Contexto Humano (Narrativa)

**Grounding** não é sinônimo de [[RAG]]. RAG é um *padrão de arquitetura*
(recuperar + gerar). Grounding é o *objetivo de qualidade*: a resposta deve
permanecer ancorada em evidências externas ou observáveis, e o sistema deve
ser capaz de apontar *qual* evidência sustenta *qual* afirmação.

Distinções úteis:

- **Contexto recuperado ≠ evidência usada.** O modelo pode receber trechos
  e ainda inventar detalhes ([[Alucinacao]]) ou ignorar o documento.
- **Atribuição** (citation / attribution) liga frases a passagens ou IDs de
  documento. Citações geradas automaticamente podem ser plausíveis e erradas;
  avaliação humana ou métricas de atribuição (ex.: frameworks de Attributed QA)
  são necessárias.
- **Grounding** também pode vir de ferramentas ([[Tool-Calling]]), bases
  estruturadas ou APIs — não só de texto indexado.

Quando **não há evidência suficiente**, a resposta correta costuma ser recusar,
pedir mais contexto ou declarar incerteza — não preencher o vazio com fluência.
Isso se conecta a [[Avaliacao-de-RAG]] (fidelidade) e [[Proveniencia-de-Dados]]
(cadeia de origem do trecho citado).

Limitações: RAG sozinho não garante grounding; citação automática não garante
correção; evidência desatualizada ou enviesada ainda “ancora” respostas ruins.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Grounding e atribuição de evidências em respostas de LLM"
relations:
  - is_a: "Requisito de qualidade: afirmações ancoradas e atribuíveis a evidência"
  - related_to: "[[RAG]] (mecanismo frequente de obter evidência; não equivalente a grounding)"
  - related_to: "[[Avaliacao-de-RAG]] (fidelidade e relevância medem aderência à evidência)"
  - related_to: "[[Proveniencia-de-Dados]] (metadados e origem do trecho citado)"
  - related_to: "[[Alucinacao]] (falha de grounding / factualidade)"
  - related_to: "[[Tool-Calling]] (ferramentas como fonte de evidência observável)"
rules_of_thumb:
  - "Regra 1: Não trate 'documento no prompt' como prova de que a resposta usou esse documento."
  - "Regra 2: Prefira atribuição a trechos ou IDs específicos a 'segundo as fontes' genérico."
  - "Regra 3: Se a evidência for insuficiente ou conflitante, declare incerteza ou recuse — não invente."
  - "Regra 4: Avalie citações (atribuição) separadamente de fluência; citações automáticas erram."
  - "Regra 5: Grounding pode vir de tools e dados estruturados, não só de RAG textual."
  - "Exceção: Tarefas criativas ou especulativas podem não exigir grounding factual; deixe o contrato explícito."
```

---

## 🔗 3. Notas Relacionadas
- [[RAG]]
- [[Avaliacao-de-RAG]]
- [[Proveniencia-de-Dados]]
- [[Alucinacao]]
- [[Tool-Calling]]

## 📚 4. Fontes
- Ver `Fontes/Grounding.md`.
- Bohnet et al., Attributed Question Answering (arXiv:2212.08037).
- Kenthapadi et al., Grounding and Evaluation for LLMs survey (arXiv:2407.12858).
