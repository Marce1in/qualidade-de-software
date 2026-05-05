import pytest

from localeats.pedido import calcular_total_pedido


def test_total_valido():
    itens = [
        {"preco": 10},
        {"preco": 20},
        {"preco": 30},
    ]

    resultado = calcular_total_pedido(itens, 15)

    assert resultado == 60


def test_valor_minimo_nao_atingido():
    itens = [
        {"preco": 5},
        {"preco": 5},
    ]

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 20)


def test_total_exatamente_valor_minimo():
    itens = [
        {"preco": 10},
        {"preco": 10},
    ]

    resultado = calcular_total_pedido(itens, 20)

    assert resultado == 20


def test_preco_negativo():
    itens = [
        {"preco": 10},
        {"preco": -5},
    ]

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 15)
