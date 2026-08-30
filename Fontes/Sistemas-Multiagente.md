# Fontes — Sistemas-Multiagente

## [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)
- Usada para: afirmação de que ganhos de MAS vs. agente único em benchmarks são frequentemente mínimos; taxonomia MAST com 14 modos em 3 categorias (especificação/desenho, desalinhamento entre agentes, verificação/término); kappa 0.88 entre anotadores; existência do dataset de traces.
- Autores: Mert Cemri, Melissa Z. Pan, Shuyi Yang et al. (Berkeley / colaboradores).
- Data de acesso: 2026-08-30
- Confiabilidade: preprint arXiv (2025), estudo empírico com anotação humana; versões do abstract variam em número de traces/frameworks (150 traces iniciais vs. dataset ampliado 1600+). A nota usa as três categorias e a conclusão qualitativa, não um número único de traces como fato rígido.

## [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)
- Usada para: padrão de agentes conversáveis (LLM + humano + tools), group chat e programação do fluxo de conversa como infraestrutura de MAS.
- Autores: Qingyun Wu, Gagan Bansal, Jieyu Zhang et al. (Microsoft / universidades).
- Data de acesso: 2026-08-30
- Confiabilidade: relatório técnico / preprint 2023 amplamente citado; o software evoluiu (AutoGen → AG2 etc.). A nota cita o *padrão conversacional*, não uma versão específica de biblioteca.

## [A2A Protocol](https://a2a-protocol.org/latest/)
- Usada para: distinção MCP (agente→tool) vs. A2A (agente→agente); Agent Cards, tarefas e artefatos; governança atual sob Linux Foundation.
- Complemento: [repositório a2aproject/A2A](https://github.com/a2aproject/A2A).
- Data de acesso: 2026-08-30
- Confiabilidade: documentação oficial do protocolo; versão e bindings (JSON-RPC, gRPC, REST) mudam — não tratar detalhes de wire format como estáveis nesta nota.

## Notas de escopo e divergência menor
- Não se catalogam todos os frameworks (CrewAI, LangGraph, MetaGPT, Magentic-One): a vida útil da nota é o desenho (papéis, canal, parada, verificação), não o vendor.
- Resumos públicos do MAST às vezes rotulam a primeira categoria como "system design" e às vezes "specification issues". São o mesmo bloco (contrato de papéis, tools, orquestração). A nota usa "especificação/desenho" de propósito.
- Definições clássicas de MAS em IA (Wooldridge et al.) são anteriores a LLM agents; esta nota cobre o recorte **LLM multi-agent**, não o campo inteiro de agentes clássicos.
