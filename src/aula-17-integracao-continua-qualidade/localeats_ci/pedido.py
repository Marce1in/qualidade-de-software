def calcular_total_pedido(
    subtotal: float,
    taxa_entrega: float = 0.0,
    desconto: float = 0.0,
) -> float:
    """Calcula o valor final de um pedido do LocalEats."""
    if subtotal < 0 or taxa_entrega < 0 or desconto < 0:
        raise ValueError("Valores do pedido nao podem ser negativos.")

    total = subtotal + taxa_entrega - desconto
    return max(round(total, 2), 0.0)


def validar_cupom(codigo: str | None, cupons_validos: dict[str, float]) -> float:
    """Retorna o desconto de um cupom valido ou zero quando ele nao existir."""
    if not codigo:
        return 0.0

    codigo_normalizado = codigo.strip().upper()
    if not codigo_normalizado:
        return 0.0

    return cupons_validos.get(codigo_normalizado, 0.0)
