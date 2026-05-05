def calcular_total_pedido(itens, valor_minimo):
    if not itens:
        raise ValueError("O pedido deve ter pelo menos um item")

    if valor_minimo < 0:
        raise ValueError("Valor minimo invalido")

    total = 0

    for item in itens:
        if "preco" not in item:
            raise ValueError("Item sem preco")

        preco = item["preco"]
        if preco < 0:
            raise ValueError("Preco invalido")

        total += preco

    if total < valor_minimo:
        raise ValueError("Valor minimo do pedido nao atingido")

    return total
