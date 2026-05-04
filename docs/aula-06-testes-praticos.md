# Planejamento e Execução de Testes – LocalEats

Integrante:
Marcelo Oscaberry

---

## Plano de Testes

### 1.1 Objetivo

O propósito deste plano de testes é verificar o correto funcionamento das funcionalidades principais do LocalEats, assegurando que os usuários consigam buscar restaurantes, ver informações e fazer pedidos sem problemas.

Os testes visam detectar:

* Falhas de funcionamento
* Comportamentos fora do esperado
* Problemas de interface
* Erros em situações específicas

Dessa forma, busca-se entregar um sistema mais confiável e com maior qualidade.

---

### 1.2 Escopo

**Funcionalidades que serão testadas**

* Login de usuário
* Busca de restaurantes
* Visualização de restaurantes
* Realização de pedidos
* Avaliação de restaurantes

**Funcionalidades fora do escopo**

* Testes de performance
* Testes de segurança
* Testes automatizados
* Integrações externas

---

### 1.3 Funcionalidades Selecionadas

As funcionalidades selecionadas são consideradas vitais para o funcionamento do sistema:

* Autenticação de usuário (login)
* Busca de restaurantes
* Visualização de detalhes de restaurante
* Realização de pedidos
* Avaliação de restaurantes

---

### 1.4 Estratégia de Testes

Os seguintes tipos de teste serão aplicados:

**Testes Funcionais**

Verificam se as funcionalidades operam conforme o esperado.

**Testes de Caixa Preta**

Serão conduzidos sob a perspectiva do usuário, sem analisar o código interno.

**Testes Manuais**

Serão realizados manualmente pela interface do sistema.

---

### 1.5 Abordagem de Testes

A abordagem será baseada em cenários reais de uso, englobando:

* Cenários de sucesso (happy path)
* Cenários de erro
* Verificação de mensagens e comportamentos

Os testes serão executados diretamente no sistema disponibilizado para a atividade.

---

### 1.6 Responsáveis

| Atividade                    | Responsável |
| ---------------------------- | ----------- |
| Planejamento dos testes      | Marcelo      |
| Definição dos casos de teste | Marcelo      |
| Execução dos testes          | Marcelo      |
| Análise dos resultados       | Marcelo      |

---

## 2. Casos de Teste

### CT01 – Login com sucesso

**Pré-condição**

Usuário possui conta ativa no sistema.

**Passos**

* Acessar a página de login
* Inserir email válido
* Inserir senha correta
* Clicar no botão "Login"

**Dados de entrada**

* Email: [marcelo.desenvolvedor.contato@gmail.com](mailto:marcelo.desenvolvedor.contato@gmail.com)
* Senha: senhasecreta

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de login
E que informei um email válido
E que informei a senha correta
Quando eu clicar em Login
Então o sistema deve redirecionar para a página inicial
```

**Resultado esperado**

Usuário consegue acessar o sistema com sucesso.

---

### CT02 – Login com senha incorreta

**Pré-condição**

Usuário possui conta cadastrada.

**Passos**

* Acessar página de login
* Inserir email válido
* Inserir senha incorreta
* Clicar em Login

**Dados de entrada**

* Email: [marcelo.desenvolvedor.contato@email.com](mailto:marcelo.desenvolvedor.contato@email.com)
* Senha: senhaErrada

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de login
E que informei um email válido
E que informei uma senha incorreta
Quando eu clicar em Login
Então o sistema deve apresentar uma mensagem de erro
```

**Resultado esperado**

Sistema notifica que o login é inválido.

---

### CT03 – Buscar restaurante por nome

**Pré-condição**

Usuário está na página principal.

**Passos**

* Acessar página principal
* Digitar o nome de um restaurante na busca
* Clicar em buscar

**Dados de entrada**

* Busca: Japonesa

**Cenário (Gherkin)**

```gherkin
Dado que estou na página principal
Quando eu pesquisar por "Japonesa"
Então o sistema deve exibir restaurantes relacionados
```

**Resultado esperado**

Lista de restaurantes exibida de forma correta.

---

### CT04 – Buscar restaurante inexistente

**Pré-condição**

Usuário está na página de busca.

**Passos**

* Acessar campo de busca
* Digitar restaurante inexistente
* Executar busca

**Dados de entrada**

* Busca: RestauranteAvenida

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de busca
Quando eu pesquisar por um restaurante inexistente
Então o sistema deve informar que nenhum resultado foi encontrado
```

**Resultado esperado**

Mensagem informando que não há resultados.

---

### CT05 – Realizar pedido

**Pré-condição**

Usuário está visualizando um restaurante.

**Passos**

* Abrir página de um restaurante
* Selecionar item do menu
* Clicar em realizar pedido

**Dados de entrada**

* Item: Pizza

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de um restaurante
E que selecionei um item do menu
Quando eu clicar em realizar pedido
Então o sistema deve registrar o pedido
```

**Resultado esperado**

Pedido criado com sucesso no sistema.

---

### CT06 – Pagamento de pedido

**Pré-condição**

Usuário possui pedido pendente.

**Passos**

* Acessar página de pedidos
* Selecionar pedido pendente
* Clicar em pagar pedido

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de pedidos
E que possuo um pedido pendente
Quando eu clicar em pagar pedido
Então o sistema deve permitir concluir o pagamento
```

**Resultado esperado**

Pagamento finalizado com sucesso.

---

### CT07 – Avaliar restaurante

**Pré-condição**

Usuário está logado e na página do restaurante.

**Passos**

* Acessar página do restaurante
* Clicar em avaliações
* Inserir avaliação
* Enviar avaliação

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de um restaurante
Quando eu clicar em avaliações
Então o sistema deve permitir enviar uma avaliação
```

**Resultado esperado**

Avaliação registrada com sucesso.

---

## Execução dos Testes

| ID   | Caso de Teste                  | Resultado | Evidência                                          |
| ---- | ------------------------------ | --------- | -------------------------------------------------- |
| CT01 | Login com sucesso              | Passou    | Usuário foi redirecionado para a página inicial    |
| CT02 | Login com senha incorreta      | Passou    | Sistema exibiu mensagem de erro                    |
| CT03 | Buscar restaurante             | Falhou    | Busca por nome ou culinária não retorna resultados |
| CT04 | Buscar restaurante inexistente | Passou    | Sistema exibiu mensagem de nenhum resultado        |
| CT05 | Realizar pedido                | Passou    | Pedido foi registrado no sistema                   |
| CT06 | Pagamento de pedido            | Falhou    | Sistema não permite concluir pagamento             |
| CT07 | Avaliar restaurante            | Falhou    | Não foi possível enviar avaliação                  |

---

## Análise dos Resultados

Total de testes executados: 7

Testes que passaram: 4

Testes que falharam: 3

**Principais problemas encontrados**

* A busca por tipo de culinária ou nome não exibe resultados corretamente.
* O processo de pagamento não permite concluir a compra.
* O módulo de avaliação de restaurantes não funciona como deveria.

Esses problemas afetam diretamente a experiência do usuário e revelam falhas relevantes nos fluxos do sistema.

---

## Reflexão no contexto do LocalEats

**O plano de testes contribuiu para uma melhor organização?**

Sim. O plano possibilitou estruturar os cenários de verificação de forma organizada, assegurando que as funcionalidades principais fossem avaliadas de maneira sistemática.

---

**Algum problema só foi notado durante a execução?**

Sim. Ao executar os testes, ficou evidente que o sistema tem falhas no fluxo de pedidos e avaliações, além de problemas na funcionalidade de busca.

---

**O que poderia ser aprimorado no processo de testes?**

* Elaborar mais casos de teste
* Incluir testes de usabilidade
* Implementar testes automatizados
* Testar mais cenários de erro
