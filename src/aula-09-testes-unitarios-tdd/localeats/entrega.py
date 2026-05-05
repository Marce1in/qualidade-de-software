def calcular_taxa_entrega(distancia_km):
    if distancia_km < 0:
        raise ValueError("Distancia invalida")

    taxa_fixa = 5.0

    if distancia_km <= 3:
        return taxa_fixa

    km_excedente = distancia_km - 3
    return taxa_fixa + (km_excedente * 2.0)
