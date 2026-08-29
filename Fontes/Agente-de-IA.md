# Fontes — Agente-de-IA

## [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- Usada para: definição do loop canônico Thought → Action → Observation; evidência de redução de alucinação em HotpotQA/FEVER e ganhos em ALFWorld/WebShop.
- Autores: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao (Princeton + Google Research).
- Data de acesso: 2026-08-29
- Confiabilidade: paper revisado (ICLR 2023); um dos trabalhos mais citados na área de agentes LLM.

## [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- Usada para: demonstração de que um LM pode aprender, de forma auto-supervisionada, *quando* e *como* chamar APIs (calculadora, busca, tradução, etc.) com poucas demonstrações por ferramenta.
- Autores: Timo Schick et al. (Meta AI).
- Data de acesso: 2026-08-29
- Confiabilidade: paper revisado (NeurIPS 2023); referência clássica de tool-use via treino.

## Model Context Protocol e Agentic AI Foundation
- Usada para: contexto de padronização de descoberta e chamada de ferramentas em agentes reais (ligação com a nota [[Model-Context-Protocol]]).
- Fontes primárias:
  - [Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) (Anthropic, 9 dez 2025)
  - [MCP joins the Agentic AI Foundation](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) (blog oficial MCP)
- Data de acesso: 2026-08-29
- Confiabilidade: anúncios oficiais da Anthropic e da fundação sob Linux Foundation.

## Notas de escopo
- A nota de conceito foca no *padrão de controle* (agente como loop de raciocínio + ação) e não tenta catalogar todos os frameworks de produção (LangGraph, AutoGen, CrewAI, etc.), que evoluem rápido.
- "Lost in the middle" e limites de janela de contexto são tratados na nota [[Janela-de-Contexto]]; aqui só se registra a relação de dependência.
