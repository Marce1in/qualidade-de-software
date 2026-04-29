# Diagnóstico de Qualidade – Startup Local Eats

Disciplina: Qualidade de Software  
Aula 3 – Papéis, Responsabilidades e Práticas de QA  
Equipe: Solo dev.  
Integrante: Marcelo Oscaberry.

---

## 1. Diagnóstico da Situação Atual

### 1.1 Papéis atuais identificados
Desenvolvedores;  
Gerente de Produto (ou quem decide prioridades de produto);  
Possivelmente um Analista de Sistemas (sem formalização).

### 1.2 Quem é responsável pela qualidade hoje?
Hoje a qualidade vem sendo conduzida de maneira informal, concentrada nas mãos dos próprios desenvolvedores. Não existe um cargo dedicado a QA nem um processo estruturado de validação antes das entregas.

### 1.3 Problemas identificados
Falta de clareza sobre quem responde pela qualidade;  
Inexistência de testes organizados antes da liberação;  
Sem controle ou registro de defeitos;  
Comunicação ineficiente entre equipe e parceiros;  
Entregas recorrentes com falhas.

### 1.4 Impactos desses problemas
Essas questões provocam defeitos como pedidos duplicados e falhas no checkout, prejudicando a experiência do usuário. Isso resulta em perda de confiança dos clientes e restaurantes, retrabalho constante e aumento dos custos de manutenção.

### 1.5 A qualidade é responsabilidade de quem?
A qualidade precisa ser compromisso de todos. Mesmo havendo um papel específico de QA, cada membro (desenvolvedores, analistas e produto) deve contribuir para entregar software de qualidade.

---

## 2. Papéis da Equipe Propostos

### 2.1 Lista de papéis
Desenvolvedor;  
QA / Analista de Qualidade;  
Analista de Sistemas;  
DevOps.

### 2.2 Descrição dos papéis

| Papel | Responsabilidades principais | Relação com a qualidade |
|------|----------------------------|-------------------------|
| Desenvolvedor | Construir funcionalidades, corrigir defeitos, revisar código | Deve produzir código limpo e testável, resolvendo problemas com agilidade |
| QA / Analista de Qualidade | Planejar e rodar testes, detectar bugs | Encarregado de validar o sistema antes de cada entrega |
| Analista de Sistemas | Levantar e documentar requisitos | Assegura que o sistema atenda às necessidades levantadas |
| DevOps | Administrar deploy e infraestrutura | Mantém a estabilidade do sistema em produção |

---

## 3. Práticas de QA Sugeridas

### 3.1 Lista de práticas
Testes manuais nas funcionalidades essenciais;  
Registro e monitoramento de bugs;  
Testes exploratórios;  
Revisão de código (code review);  
Validação pré-deploy.

### 3.2 Explicação das práticas

**Prática 1:**  
Executar testes manuais nas funcionalidades críticas (ex: finalização de pedidos) antes de liberar para produção.

**Prática 2:**  
Adotar ferramentas de gestão de bugs (ex: Jira, Trello) para rastrear e acompanhar defeitos.

**Prática 3:**  
Testes exploratórios para descobrir problemas que passam despercebidos nos testes planejados.

**Prática 4:**  
Revisão de código entre pares para prevenir erros e elevar a qualidade do código.

**Prática 5:**  
Checar todas as funcionalidades antes do deploy para confirmar que estão operando corretamente.

---

## 4. Anúncios de Contratação

### 4.1 Vaga 1 – Analista de Qualidade de Software (QA)

**Descrição da vaga**  
A Local Eats procura um(a) Analista de Qualidade para assegurar a entrega de funcionalidades com alto padrão, trabalhando em conjunto com desenvolvedores e analistas na validação do sistema.

**Responsabilidades**  
Planejar e executar testes  
Identificar e documentar bugs  
Validar funcionalidades antes da liberação  

**Requisitos obrigatórios**  
Conhecimento fundamental em testes de software  
Habilidade para identificar e registrar defeitos  
Boa comunicação  

**Requisitos desejáveis**  
Experiência com testes web  
Conhecimento em ferramentas de bug tracking  
Noções de automação de testes  

**Certificações desejáveis**  
ISTQB – CTFL (Certified Tester Foundation Level);  
ISTQB CTAL (Certified Tester Advanced Level);  
Agile Testing.

---

### 4.2 Vaga 2 – Desenvolvedor Full Stack

**Descrição da vaga**  
A Local Eats está recrutando Desenvolvedor Full Stack para atuar na construção e manutenção da plataforma de pedidos online.

**Responsabilidades**  
Desenvolver novas funcionalidades  
Corrigir defeitos reportados  
Participar de revisões de código  

**Requisitos obrigatórios**  
Conhecimento em desenvolvimento web  
Experiência com JavaScript/TypeScript  
Noções de banco de dados  

**Requisitos desejáveis**  
Experiência com APIs REST  
Conhecimento em Git  
Noções de testes automatizados  

**Certificações desejáveis**  
AWS Certified Developer – Associate;  
IBM Full-Stack JavaScript Developer Professional Certificate (Coursera);  
Formação em ADS, Ciência da Computação ou áreas afins.

---

## 5. Conclusão da Equipe

Compreendeu-se a relevância de estruturar a qualidade dentro do ciclo de desenvolvimento. A maior dificuldade foi definir com clareza os papéis e responsabilidades. Como proposta de melhoria, sugerimos estabelecer papéis bem definidos, adotar práticas de QA e organizar melhor o processo de desenvolvimento, buscando reduzir falhas e aumentar a confiabilidade.

---

## Observações:

Este trabalho evidencia que a qualidade deve ser tratada como responsabilidade coletiva e que processos simples podem gerar melhorias significativas no produto final.
