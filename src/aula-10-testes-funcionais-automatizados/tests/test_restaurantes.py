import uuid

from playwright.sync_api import sync_playwright

from pages.restaurantes_page import RestaurantesPage


def test_usuario_visualiza_detalhes_de_restaurante():
    email = f"teste-{uuid.uuid4().hex[:8]}@teste.com"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        restaurantes = RestaurantesPage(page)

        restaurantes.cadastrar_usuario_teste(
            nome="Usuario Teste",
            email=email,
            senha="123456",
        )
        restaurantes.validar_lista_carregada()
        restaurantes.abrir_primeiro_restaurante()
        restaurantes.validar_pagina_de_detalhes()

        browser.close()
