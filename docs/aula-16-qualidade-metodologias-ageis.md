# 🧩 Aula 16 – Qualidade em Metodologias Ágeis (LocalEats)

## 👥 Integrantes

- Marcelo Oscaberry

---

# 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
| --- | --- | --- | --- |
| Planejamento iterativo | Sim | As entregas são organizadas por aula e ajustadas conforme a necessidade do projeto. | Pode ser evoluído com ciclos curtos e datas de entrega mais explícitas. |
| Priorização de funcionalidades | Parcial | As demandas principais são escolhidas conforme a atividade e registradas como tarefas no MEIRA. | Criar um backlog priorizado dentro do MEIRA. |
| Entregas incrementais | Sim | O repositório recebe novas documentações, testes e automações por etapa. | Associar cada incremento a uma tarefa e evidência. |
| Feedback frequente | Parcial | Ocorre por validação das entregas e ajustes no próprio repositório. | Registrar feedbacks como comentários ou novas tarefas. |
| Trabalho colaborativo | Parcial | A atividade é individual, mas segue um fluxo que poderia ser usado por um time. | Definir responsáveis e revisores em um cenário com mais integrantes. |
| Controle visual das atividades | Sim | O MEIRA foi usado como ferramenta de organização, com Kanban para visualizar o status das tarefas. | Manter as tarefas sempre atualizadas durante o desenvolvimento. |
| Melhoria contínua | Sim | O processo é ajustado conforme surgem novas aulas, testes e necessidades. | Formalizar retrospectivas ao final de cada ciclo. |

---

## 📌 Conclusão

O processo do LocalEats possui características ágeis importantes, principalmente o uso de entregas incrementais e controle visual por Kanban. O **MEIRA** foi considerado como ferramenta de organização do trabalho, substituindo ferramentas como Trello para acompanhar tarefas, defeitos e status das atividades.

- Site do MEIRA: <https://meira.marce1in.com.br/>
- Repositório do MEIRA: <https://gitlab.com/senac-projetos-de-desenvolvimento/2025-marcelo-oscaberry-dos-santos/meira>

Mesmo assim, existem oportunidades de melhoria. O backlog pode ser mais detalhado, os critérios de aceite podem ser definidos antes da implementação e as revisões podem ser registradas com mais clareza. A adoção de práticas simples de Scrum e Kanban ajudaria a aumentar previsibilidade e controle.

---

# 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
| --- | --- | --- |
| Detalhar melhor as tarefas no MEIRA | Kanban | Maior clareza sobre o que precisa ser entregue |
| Criar ciclos curtos de entrega | Scrum | Mais previsibilidade para planejamento e validação |
| Manter backlog priorizado | Scrum | Melhor decisão sobre o que implementar primeiro |
| Registrar retrospectivas | Scrum / Lean | Aprendizado contínuo após cada etapa |
| Revisar código antes da conclusão | XP | Redução de erros e aumento da qualidade técnica |

---

# 3. Definition of Ready (DoR)

Uma funcionalidade estará pronta para desenvolvimento quando:

- O requisito estiver descrito com clareza
- Os critérios de aceitação estiverem definidos
- A tarefa estiver registrada e priorizada no Kanban do MEIRA
- As dependências forem conhecidas
- O escopo estiver compreendido
- Não houver impedimento técnico relevante

---

# 4. Definition of Done (DoD)

Uma funcionalidade será considerada concluída quando:

- Os critérios de aceitação forem atendidos
- O código estiver implementado
- Os testes necessários forem executados
- Não houver bug crítico conhecido
- A alteração estiver integrada ao projeto
- A documentação estiver atualizada
- A tarefa estiver movida para concluído no Kanban do MEIRA
