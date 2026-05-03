# Testes Funcionais vs Estruturais

**Disciplina:** Qualidade de Software  
**Funcionalidade escolhida:** Login/Cadastro  
**Equipe:** Solo dev  
**Integrante:** Marcelo Oscaberry  



---

## 1. Descrição da funcionalidade

A funcionalidade de login/cadastro possibilita que o usuário registre uma conta e acesse o LocalEats por meio de e-mail e senha.

No cadastro, o usuário preenche seus dados básicos (e-mail e senha).  
No login, ele utiliza essas credenciais para entrar na sua conta.

### O que o usuário espera

O usuário espera:

- Criar uma conta sem apresentar falhas;  
- Realizar login com dados válidos;  
- Receber mensagens compreensíveis em caso de erro;  
- Ter segurança (não acessar contas de terceiros);  
- Ter validações adequadas nos campos de entrada.  

---

## 2. Testes Caixa-Preta (Visão do Usuário)

Nos testes caixa-preta, desconsideramos a implementação interna, avaliando apenas o comportamento visível ao usuário.

### Cenários de teste

1. **Login com dados válidos**  
Ao informar e-mail e senha corretos, o sistema deve conceder acesso e direcionar o usuário para a área logada.

2. **Login com senha incorreta**  
Ao informar um e-mail existente e senha errada, o sistema deve apresentar uma mensagem como "Senha incorreta", sem revelar dados sensíveis.

3. **Login com e-mail não cadastrado**  
O sistema deve notificar que o usuário não foi encontrado ou que os dados são inválidos.

4. **Campos vazios**  
O sistema deve bloquear o envio do formulário e sinalizar quais campos são obrigatórios.

5. **Cadastro com dados válidos**  
O sistema deve registrar a conta com sucesso e confirmar ao usuário.

6. **Cadastro com e-mail já existente**  
O sistema deve bloquear o cadastro e avisar que o e-mail já está em uso.

7. **E-mail em formato inválido**  
Exemplo: `marcelo@`  
O sistema deve validar e bloquear o envio.

8. **Senha muito curta ou inválida**  
O sistema deve exigir um tamanho mínimo e exibir mensagem adequada.

9. **Campos com espaços ou caracteres inválidos**  
O sistema deve considerar entradas como `"   "` como inválidas.

10. **Recuperação de senha**  
O usuário deve conseguir solicitar a recuperação de senha de forma intuitiva e segura.

---

### Possíveis erros encontrados

- Login permitindo acesso com senha incorreta  
- Cadastro aceitando e-mails duplicados  
- Ausência de mensagens claras de erro  
- Validações insuficientes nos campos  
- Comportamento inconsistente entre telas diferentes  

---

## 3. Testes Caixa-Branca (Visão do Sistema)

Nos testes caixa-branca, analisamos como a funcionalidade pode estar implementada por dentro.

### Possível lógica do sistema

- Verificação de preenchimento dos campos 
- Normalização do e-mail (ex: converter para minúsculo)  
- Consulta do usuário no banco de dados  
- Comparação entre a senha informada e a armazenada
- Checagem de duplicidade de e-mail no cadastro  

### Estruturas lógicas possíveis

```javascript
if (!email || !senha)
if (!email.includes("@"))
if (senha.length < 6)
if (usuario == null)
if (hash(senha) === senhaBanco)
if (emailJaExiste)
```

### Situações a serem testadas

1. **Validação de campos vazios**  
Certificar que o sistema não avança com dados incompletos.

2. **Verificação de usuário existente**  
Testar o comportamento tanto quando o usuário existe quanto quando não existe.

3. **Comparação de senha**  
Verificar se a comparação está correta e se é segura.

4. **Cadastro com e-mail duplicado**  
Garantir que a checagem de duplicidade está funcionando.

5. **Caminhos alternativos**  
Testar todas as rotas possíveis (sucesso e falha).

---

### Possíveis erros encontrados

- Falhas na checagem de senha  
- Condições implementadas incorretamente  
- Fluxos não testados  
- Problemas na validação de dados  

---

## 4. Comparação entre as abordagens

A diferença fundamental entre as abordagens está na perspectiva de análise do sistema.

- **Caixa-preta:** foca no comportamento visível, simulando o uso real do usuário  
- **Caixa-branca:** foca na lógica interna e nos pontos de decisão do sistema  

### Tipos de problemas identificados

**Caixa-preta:**

- Falhas percebidas pelo usuário  
- Questões de usabilidade  
- Problemas no fluxo principal  

**Caixa-branca:**

- Erros na lógica interna  
- Falhas em condições (if)  
- Caminhos de código não testados  

---

## 5. Reflexão no contexto do LocalEats

O sistema apresenta comportamentos inesperados e inconsistências.

No contexto do login, isso pode significar:

- Usuários sem conseguir acessar suas contas  
- Sistema aceitando credenciais incorretas  
- Falhas na validação de dados  

A abordagem caixa-preta permite enxergar esses problemas pela perspectiva do usuário.

Já a caixa-branca possibilita compreender a causa raiz, analisando a lógica do sistema.

### Conclusão

Nenhuma abordagem isolada é suficiente.

- A caixa-preta revela os erros  
- A caixa-branca auxilia na correção da causa  

Por isso, combinar ambas é fundamental para assegurar que o sistema funcione de forma correta e confiável.
