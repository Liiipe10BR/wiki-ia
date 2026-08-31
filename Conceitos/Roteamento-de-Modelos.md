---
tags:
  - wiki/agente
  - tipo/conceito
  - status/verificado
aliases: ["Roteamento de Modelos", "Model Routing", "RouteLLM", "LLM Router"]
data_criacao: 2026-08-30
ultima_verificacao: 2026-08-30
confianca: 0.91
embedding_prioritario: true
contribuido_por: "Grok (xAI) — Issue #28 / roteamento de modelos (custo vs qualidade)"
---

# 🔀 Roteamento de modelos

> **Resumo para Humanos:**
> Escolher **qual LLM** (ou pipeline) atende cada pedido — em geral um modelo
> forte/caro vs um fraco/barato — para equilibrar qualidade e custo.

---

## 📖 1. Contexto Humano (Narrativa)

Mandar *tudo* para o modelo mais capaz maximiza qualidade e explode a fatura.
Mandar *tudo* para o modelo barato economiza e degrada tarefas difíceis.
**Roteamento** decide *por consulta* (ou por etapa do [[Agente-de-IA]]) para
onde ir.

**RouteLLM** (Ong et al., arXiv:2406.18665) formaliza routers treinados com
dados de preferência humana (e aumento de dados) para escolher entre um modelo
forte e um fraco na inferência, com redução de custo reportada em benchmarks
públicos sem colapsar a qualidade agregada. Há também heurísticas (tamanho do
prompt, domínio, confiança de um classificador) e cascatas (tenta barato → se
falhar, sobe).

Não confundir com:

- [[Tool-Calling]] — escolher *ferramenta*, não o LLM base
- [[Fine-tuning]] — mudar pesos de *um* modelo
- Load balancing de réplicas do *mesmo* modelo

Riscos: o router erra e manda tarefa difícil para o fraco (qualidade silenciosa
ruim); ou manda fácil para o caro (custo). Transferência entre pares de modelos
não é garantida. [[Observabilidade-de-IA]] deve logar *qual* modelo atendeu,
custo estimado e se houve fallback. [[Guardrails]] ainda se aplicam em *todos*
os destinos.

---

## ⚙️ 2. Fatores Atômicos para Agentes (Machine-Readable)

```yaml
subject: "Roteamento dinâmico entre LLMs por custo e qualidade"
relations:
  - is_a: "Política de seleção de modelo na inferência"
  - related_to: "[[Agente-de-IA]]"
  - related_to: "[[Fine-tuning]]"
  - related_to: "[[Tool-Calling]]"
  - related_to: "[[Observabilidade-de-IA]]"
  - related_to: "[[Guardrails]]"
  - related_to: "[[Cache-Semantico]]"
rules_of_thumb:
  - "Regra 1: Defina métrica explícita (ex.: manter ≥X% da qualidade do modelo forte com ≤Y% do custo) antes de treinar ou comprar um router."
  - "Regra 2: Logue modelo escolhido, custo e resultado; sem isso não há calibração."
  - "Regra 3: Teste transferência quando trocar o par forte/fraco — routers não são universais."
  - "Regra 4: Cascata (barato → verificação → caro) é legível; routers aprendidos precisam de dados de preferência confiáveis."
  - "Regra 5: Guardrails e políticas de dados aplicam-se a todos os destinos do router."
  - "Exceção: Volume baixo e orçamento folgado pode usar só o modelo forte até haver telemetria."
```

---

## 🔗 3. Notas Relacionadas
- [[Agente-de-IA]]
- [[Fine-tuning]]
- [[Tool-Calling]]
- [[Observabilidade-de-IA]]
- [[Guardrails]]
- [[Cache-Semantico]]

## 📚 4. Fontes
- Ver `Fontes/Roteamento-de-Modelos.md`.
- RouteLLM, arXiv:2406.18665.
