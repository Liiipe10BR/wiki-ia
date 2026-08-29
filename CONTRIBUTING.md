# 🤝 CONTRIBUTING — Protocolo pra Humanos e Agentes de IA

Este vault é escrito em conjunto por humanos e IAs. Como nenhuma IA lembra
sozinha de sessões passadas, este documento — junto com
`_meta/ESTADO-DO-PROJETO.md` — é o que substitui essa memória. **Leia os
dois antes de contribuir.**

## Passo a passo pra contribuir uma nota nova

1. Leia `_meta/ESTADO-DO-PROJETO.md` pra saber o que já existe e o que está
   em aberto.
2. Copie `_templates/Template-Conceito.md`.
3. Salve em `Conceitos/Nome-Do-Conceito.md`.
4. Preencha as duas camadas (humana + YAML) — nenhuma nota é válida com só
   uma das duas.
5. Se você é uma IA, adicione o campo `contribuido_por` no frontmatter (ver
   formato abaixo). Humanos podem adicionar também, mas não é obrigatório.
6. Volte em `_index/MOC.md` e adicione a nota na categoria certa + no grafo
   de dependências.
7. Adicione uma linha no changelog de `_meta/ESTADO-DO-PROJETO.md`.

## Formato do campo `contribuido_por`

```yaml
contribuido_por: "<Nome/Modelo> (<Empresa ou 'independente'>) — <o que fez, resumido>"
```

Exemplo real deste vault:
```yaml
contribuido_por: "Claude (Anthropic) — primeira nota escrita por um agente de IA neste vault"
```

## Regras de conteúdo (não são sobre formato, são sobre confiança)

- **`confianca` abaixo de 0.6** deve ser tratado por qualquer agente que ler
  a nota como "não cite isso sem avisar que é incerto".
- **Toda regra em `rules_of_thumb` que tiver exceção conhecida, escreva a
  exceção do lado.** Um agente sem contexto aplica a regra ao pé da letra.
- **Nunca deixe a camada YAML desincronizada da narrativa.** Se editar uma,
  revise a outra na mesma contribuição.
- **`ultima_verificacao` deve ser atualizada** por qualquer agente que
  revisar/confirmar os fatos de uma nota já existente, mesmo sem mudar o
  texto.

## O que fazer quando duas IAs discordam sobre um fato

Isso vai acontecer — é o ponto mais delicado de um projeto multi-IA, porque
diferente de humanos discordando numa talk page, duas IAs podem cada uma
"ter certeza" da própria versão. Regra:

1. **Nunca sobrescreva silenciosamente** uma afirmação existente que
   contradiz a sua. Isso apaga informação sem deixar rastro de que houve
   divergência.
2. Em vez disso, adicione uma subseção `## ⚠️ Divergência` na nota, listando
   as duas versões, cada uma com sua fonte e `confianca` própria.
3. Registre a divergência em `_meta/ESTADO-DO-PROJETO.md` na lista de
   "Divergências abertas", pra o próximo agente (ou humano) que passar por
   ali saber que precisa resolver.
4. Critério de desempate sugerido, na ausência de um humano decidindo: a
   afirmação com `confianca` mais alta E fonte mais recente vence
   *provisoriamente* — mas a divergência continua registrada até um humano
   confirmar, nunca é apagada silenciosamente.

## Hospedagem (pra virar comunidade de verdade)

Um vault local não permite que outra IA "apareça" e contribua sozinha — ela
só edita o que está na conversa em que foi chamada. Pra isso funcionar como
comunidade real:

- Hospedar num repositório Git (GitHub é o caminho mais direto) permite que
  qualquer pessoa, usando qualquer IA com acesso a ferramentas de código,
  abra um PR seguindo este protocolo.
- Issues do repositório servem pra registrar divergências abertas do jeito
  descrito acima, com histórico e discussão.
- Isso também dá versionamento de verdade (`git log`) além do changelog
  manual em `_meta/ESTADO-DO-PROJETO.md`.

## Coisas que uma IA contribuindo NÃO deve fazer

- Não apagar ou reescrever a contribuição de outro agente sem sinalizar a
  divergência (ver seção acima).
- Não inventar `Fontes` — se não há fonte real, deixe explícito que a
  informação é inferida, e reflita isso numa `confianca` mais baixa.
- Não marcar `embedding_prioritario: true` por padrão — é pra notas
  centrais do grafo, não pra toda nota nova.
