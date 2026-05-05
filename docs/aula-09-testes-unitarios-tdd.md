# Centro Universitário Senac-RS

**ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet**
**Unidade Curricular:** Qualidade de Software
**Prof.:** Luciano Zanuz

---

# 🧩 Atividade PBL – Aula 9

## Testes Unitários Automatizados e TDD – LocalEats

---

## 👥 Integrantes

* Marcelo Oscaberry

---

## 📁 Estrutura do Projeto

```python
.
├── src/
│   ├── pedido.py
│   ├── desconto.py
│   └── entrega.py
└── tests/
    ├── test_pedido.py
    ├── test_desconto.py
    └── test_entrega.py
```

---

## 🔹 1. Funcionalidades escolhidas

### 🍔 Funcionalidade 1 – Cálculo do total do pedido

📌 **Descrição:**
Encarregada de somar os valores dos itens e checar se o pedido alcança o valor mínimo exigido.

📏 **Regras de negócio**

* A soma dos itens determina o total
* Se total < valor mínimo → erro
* Caso contrário → pedido válido

---

### 💸 Funcionalidade 2 – Aplicação de desconto

📌 **Descrição:**
Aplica um desconto percentual sobre o valor total do pedido.

📏 **Regras de negócio**

* Percentual entre 0% e 100%
* Valor final não pode ficar negativo

---

### 🚚 Funcionalidade Complementar – Cálculo de taxa de entrega

📌 **Descrição:**
Calcula a taxa de entrega conforme a distância informada.

📏 **Regras de negócio**

* Até 3 km → taxa fixa
* Acima de 3 km → taxa proporcional
* Distância negativa → erro

---

## 🔹 2. Testes Unitários

### 🧪 Pedido

**Teste: Pedido válido**

* Cenário: soma superior ao valor mínimo
* Dados de entrada: itens com valores positivos
* Resultado esperado: 60

```python
def test_total_valido():
    itens = [
        {"preco": 10},
        {"preco": 20},
        {"preco": 30}
    ]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 60
```

---

**Teste: Valor mínimo não atingido**

* Cenário: pedido inválido
* Dados de entrada: itens com valores baixos
* Resultado esperado: erro

```python
def test_valor_minimo_nao_atingido():
    itens = [
        {"preco": 5},
        {"preco": 5}
    ]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 20)
```

---

**Teste: Valor exatamente no mínimo**

* Cenário: total igual ao valor mínimo
* Dados de entrada: soma igual ao mínimo
* Resultado esperado: 20

```python
def test_total_exatamente_valor_minimo():
    itens = [
        {"preco": 10},
        {"preco": 10}
    ]
    resultado = calcular_total_pedido(itens, 20)
    assert resultado == 20
```

---

**Teste: Preço negativo**

* Cenário: item inválido
* Dados de entrada: item com preço negativo
* Resultado esperado: erro

```python
def test_preco_negativo():
    itens = [
        {"preco": 10},
        {"preco": -5}
    ]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 15)
```

---

### 🧪 Desconto

**Teste: Desconto válido**

* Cenário: aplicação de desconto dentro do limite
* Dados de entrada: valor = 100, percentual = 10
* Resultado esperado: 90

```python
def test_desconto_valido():
    resultado = aplicar_desconto(100, 10)
    assert resultado == 90
```

---

**Teste: Desconto zero**

* Cenário: sem desconto aplicado
* Dados de entrada: valor = 100, percentual = 0
* Resultado esperado: 100

```python
def test_desconto_zero():
    resultado = aplicar_desconto(100, 0)
    assert resultado == 100
```

---

**Teste: Desconto completo**

* Cenário: desconto máximo aplicado
* Dados de entrada: valor = 100, percentual = 100
* Resultado esperado: 0

```python
def test_desconto_completo():
    resultado = aplicar_desconto(100, 100)
    assert resultado == 0
```

---

**Teste: Valor negativo**

* Cenário: entrada inválida
* Dados de entrada: valor negativo
* Resultado esperado: erro

```python
def test_valor_negativo():
    with pytest.raises(ValueError):
        aplicar_desconto(-50, 10)
```

---

**Teste: Percentual inválido**

* Cenário: percentual acima do permitido
* Dados de entrada: percentual = 150
* Resultado esperado: erro

```python
def test_percentual_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)
```

---

### 🧪 Entrega

**Teste: Taxa fixa**

* Cenário: distância até 3 km
* Dados de entrada: 2 km
* Resultado esperado: 5.0

```python
def test_taxa_fixa():
    resultado = calcular_taxa_entrega(2)
    assert resultado == 5.0
```

---

**Teste: Taxa variável**

* Cenário: distância acima de 3 km
* Dados de entrada: 5 km
* Resultado esperado: 9.0

```python
def test_taxa_variavel():
    resultado = calcular_taxa_entrega(5)
    assert resultado == 9.0
```

---

**Teste: Distância negativa**

* Cenário: valor inválido
* Dados de entrada: -1
* Resultado esperado: erro

```python
def test_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-1)
```

---

**Teste: Distância acima de 10 km**

* Cenário: distância elevada
* Dados de entrada: 15 km
* Resultado esperado: 29.0

```python
def test_distancia_acima_de_10():
    resultado = calcular_taxa_entrega(15)
    assert resultado == 29.0
```

---

## 🔹 3. Aplicação do TDD

### 🔴 Red

O teste `test_total_valido` foi escrito antes da implementação da função, seguindo a prática de TDD.

```python
def test_total_valido():
    itens = [
        {"preco": 10},
        {"preco": 20},
        {"preco": 30}
    ]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 60
```
👉 Resultado: o teste falharia caso a função ainda não houvesse sido implementada.

### 🟢 Green

Uma versão simplificada da função foi criada para fazer o teste passar.


```python
def calcular_total_pedido(itens, valor_minimo):
    total = 0

    for item in itens:
        total += item["preco"]

    return total
```

👉 Resultado: o teste passa, mas ainda não cobre todas as regras de negócio.

### 🔵 Refactor

O código foi aprimorado com validações e reorganização da lógica, mantendo todos os testes passando.

```python
def calcular_total_pedido(itens, valor_minimo):
    if not itens:
        raise ValueError("O pedido deve ter pelo menos um item")

    total = 0

    for item in itens:
        if "preco" not in item:
            raise ValueError("Item sem preço")

        if item["preco"] < 0:
            raise ValueError("Preço inválido")

        total += item["preco"]

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total
```

👉 Resultado: código mais robusto, validando todas as regras de negócio e mantendo os testes passando.

---

## 🔹 4. Refatoração

Ao longo do desenvolvimento, o código passou por melhorias com foco em qualidade e manutenibilidade:

- **Validação de entradas**  
  Foi incluída checagem para itens vazios, preços negativos e ausência da chave `"preco"`.

- **Melhoria na legibilidade**  
  Nomes claros como `total`, `itens` e `valor_minimo` facilitam a compreensão do código.

- **Organização da lógica**  
  Separação entre:
  - validações (erros)
  - cálculo do total  

- **Tratamento de erros explícito**  
  Uso de `ValueError` para assegurar a integridade dos dados.

- **Código mais robusto**  
  O sistema passou a tratar cenários inválidos que não eram cobertos antes.

---

## 🔹 5. Execução dos Testes

📊 Resultado:

```
13 passed in 0.09s
```
Os testes foram executados com pytest no ambiente local.

* Total de testes: 13
* Aprovados: 13
* Reprovados: 0

---

## 🔹 6. Reflexão

**Foi difícil escrever testes antes do código?**
Sim, porque exige pensar na lógica antes mesmo de implementar.

**O TDD foi útil?**
Sim, contribuiu para organizar melhor o código e prevenir falhas.

**Os testes trouxeram mais confiança?**
Sim, pois garantem que alterações futuras não quebrem o que já funciona.

**O que poderia ser melhor?**
Incluir mais testes para cenários extremos.

**Como isso contribui para o projeto?**
Torna o desenvolvimento mais seguro e profissional.

---

## 🎯 Conclusão

A utilização de testes automatizados e TDD possibilitou validar regras de negócio de maneira contínua, diminuindo erros e elevando a confiabilidade do sistema.
