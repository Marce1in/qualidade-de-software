import pytest

from localeats.desconto import aplicar_desconto


def test_desconto_valido():
    resultado = aplicar_desconto(100, 10)

    assert resultado == 90


def test_desconto_zero():
    resultado = aplicar_desconto(100, 0)

    assert resultado == 100


def test_desconto_completo():
    resultado = aplicar_desconto(100, 100)

    assert resultado == 0


def test_valor_negativo():
    with pytest.raises(ValueError):
        aplicar_desconto(-50, 10)


def test_percentual_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)
