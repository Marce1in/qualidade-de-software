def aplicar_desconto(valor, percentual):
    if valor < 0:
        raise ValueError("Valor invalido")

    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual de desconto invalido")

    valor_final = valor - (valor * percentual / 100)

    return max(valor_final, 0)
