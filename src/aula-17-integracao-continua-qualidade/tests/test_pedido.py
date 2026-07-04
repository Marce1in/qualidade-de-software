import pytest

from localeats_ci.pedido import calcular_total_pedido, validar_cupom


def test_total_simples_sem_desconto():
    resultado = calcular_total_pedido(subtotal=50.0, taxa_entrega=5.0)

    assert resultado == 55.0


def test_total_com_desconto():
    resultado = calcular_total_pedido(
        subtotal=50.0,
        taxa_entrega=5.0,
        desconto=10.0,
    )

    assert resultado == 45.0


def test_entrega_gratuita():
    resultado = calcular_total_pedido(subtotal=30.0, taxa_entrega=0.0)

    assert resultado == 30.0


def test_desconto_maior_que_total_nao_fica_negativo():
    resultado = calcular_total_pedido(
        subtotal=20.0,
        taxa_entrega=5.0,
        desconto=100.0,
    )

    assert resultado == 0.0


def test_valores_negativos_geram_erro():
    with pytest.raises(ValueError):
        calcular_total_pedido(subtotal=-10.0, taxa_entrega=5.0)


def test_validar_cupom_valido():
    cupons = {"BEMVINDO10": 10.0, "FRETE5": 5.0}

    resultado = validar_cupom("bemvindo10", cupons)

    assert resultado == 10.0


def test_validar_cupom_invalido():
    cupons = {"BEMVINDO10": 10.0}

    resultado = validar_cupom("CUPOMFALSO", cupons)

    assert resultado == 0.0
