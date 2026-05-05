import pytest

from localeats.entrega import calcular_taxa_entrega


def test_taxa_fixa():
    resultado = calcular_taxa_entrega(2)

    assert resultado == 5.0


def test_taxa_variavel():
    resultado = calcular_taxa_entrega(5)

    assert resultado == 9.0


def test_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-1)


def test_distancia_acima_de_10():
    resultado = calcular_taxa_entrega(15)

    assert resultado == 29.0
