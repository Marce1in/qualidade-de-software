# Aula 15 – Modelos de Maturidade

## Introdução

Este documento apresenta uma análise da maturidade do processo de desenvolvimento utilizado no projeto LocalEats. A avaliação considera organização, padronização, acompanhamento das tarefas, testes e melhoria contínua.

O objetivo é identificar o nível atual de maturidade, apontar lacunas e propor ações que ajudem a tornar o processo mais previsível e alinhado com práticas de qualidade.

## 1. Diagnóstico de Maturidade

### Avaliação do Processo

| Critério | Avaliação |
| --- | --- |
| Os requisitos são documentados? | Sim |
| Existe controle de mudanças? | Sim |
| Há atividades de teste definidas? | Sim |
| Os defeitos são registrados? | Parcial |
| O processo de desenvolvimento é conhecido? | Sim |
| As tarefas são planejadas e acompanhadas regularmente? | Sim |
| Existe padronização para implementação de funcionalidades? | Sim |
| Os testes são executados antes da entrega? | Sim |
| Há revisão de código ou validação por outra pessoa? | Parcial |
| A equipe utiliza ferramentas para gerenciamento das atividades? | Sim |
| Os artefatos do projeto são organizados e versionados? | Sim |
| Existe rastreabilidade entre requisitos e funcionalidades? | Parcial |
| Há momentos de retrospectiva ou melhoria do processo? | Parcial |
| Existem indicadores para acompanhar a qualidade? | Não |

### Classificação do Processo

**Nível de Maturidade: Definido**

### Justificativa

O processo pode ser classificado como **Definido** porque possui fluxo padronizado, organização no MEIRA, versionamento no Git e separação das entregas por aula. O MEIRA funciona como ferramenta de gestão visual do trabalho, com Kanban e acompanhamento de tarefas. Também há uso de testes automatizados em módulos específicos, principalmente nas aulas com implementação Python.

- Site do MEIRA: <https://meira.marce1in.com.br/>
- Repositório do MEIRA: <https://gitlab.com/senac-projetos-de-desenvolvimento/2025-marcelo-oscaberry-dos-santos/meira>

Ainda existem pontos de melhoria, como formalizar revisões, registrar defeitos de maneira mais completa e criar indicadores de qualidade. Mesmo assim, o processo já apresenta documentação e repetição suficientes para não depender apenas de improviso.

## 2. Identificação de Lacunas

| Lacuna | Impacto |
| --- | --- |
| Métricas de qualidade ainda não definidas | Dificulta medir evolução e comparar resultados entre entregas. |
| Revisão de código pouco formalizada | Aumenta a chance de erros passarem sem uma segunda validação. |
| Registro de defeitos ainda simples | Limita a análise de causa e recorrência dos problemas. |
| Rastreabilidade parcial | Nem toda regra possui ligação direta entre tarefa, teste e documentação. |

## 3. Propostas de Melhoria

| Melhoria | Benefício |
| --- | --- |
| Criar checklist de revisão para cada entrega | Reduz falhas por esquecimento e melhora a consistência. |
| Acompanhar métricas como testes executados e defeitos encontrados | Permite avaliar a qualidade com dados objetivos. |
| Padronizar registro de bugs em tarefas do MEIRA | Facilita priorização, correção e histórico. |
| Relacionar critérios de aceite aos testes implementados | Melhora a rastreabilidade entre requisito e validação. |

## Conclusão

O processo atual apresenta boa organização para uma atividade acadêmica e já possui características compatíveis com o nível **Definido**. A evolução mais importante está em transformar práticas existentes em registros mais formais, principalmente métricas, defeitos e revisões.
