# Fontes — Avaliação de RAG

## [RAGAs: Automated Evaluation of Retrieval Augmented Generation](https://aclanthology.org/2024.eacl-demo.16/)
- Usada para: decomposição da avaliação em qualidade do contexto recuperado,
  fidelidade da geração e relevância da resposta; apresentação de métricas
  reference-free para acelerar ciclos de avaliação de RAG.
- Autores: Shahul Es, Jithin James, Luis Espinosa Anke e Steven Schockaert.
- Publicação: EACL 2024, System Demonstrations, p. 150–158.
- Data de acesso: 2026-08-29.
- Confiabilidade: publicação acadêmica na ACL Anthology; o artigo descreve o
  framework e suas limitações experimentais.

## [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](https://aclanthology.org/2024.naacl-long.20/)
- Usada para: avaliação de relevância do contexto, fidelidade da resposta e
  relevância da resposta; uso de dados sintéticos, avaliadores leves e
  prediction-powered inference com uma pequena amostra de anotações humanas.
- Autores: Jon Saad-Falcon, Omar Khattab, Christopher Potts e Matei Zaharia.
- Publicação: NAACL 2024, Long Papers.
- Data de acesso: 2026-08-29.
- Confiabilidade: publicação acadêmica na ACL Anthology; resultados reportados
  em múltiplas tarefas e com avaliação de mudança de domínio.

## Nota de escopo

Métricas de avaliação não transformam uma resposta em fato verdadeiro por si
sós. O resultado depende do conjunto de testes, da qualidade das referências,
do avaliador escolhido e do domínio. Em aplicações de maior risco, combine
métricas automáticas com evidência rastreável e revisão humana.