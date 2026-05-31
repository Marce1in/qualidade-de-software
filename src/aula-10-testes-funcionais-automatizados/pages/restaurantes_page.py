import re

from playwright.sync_api import expect


class RestaurantesPage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://local-eats-unisenac.vercel.app/static"
        self.grid_restaurantes = page.locator("#restaurantGrid")
        self.cards_restaurantes = page.locator("#restaurantGrid .rest-card")
        self.nome_restaurante = page.locator("#restName")
        self.itens_cardapio = page.locator("#menuList .menu-item")

    def cadastrar_usuario_teste(self, nome, email, senha):
        self.page.goto(f"{self.base_url}/login.html")
        self.page.get_by_role("button", name="Criar Conta").click()
        self.page.locator("#regName").fill(nome)
        self.page.locator("#regEmail").fill(email)
        self.page.locator("#regPassword").fill(senha)
        self.page.get_by_role("button", name="Registrar").click()
        expect(self.page).to_have_url(re.compile(r".*/index\.html"))

    def validar_lista_carregada(self):
        expect(self.grid_restaurantes).to_be_visible()
        expect(self.cards_restaurantes.first).to_be_visible()

    def abrir_primeiro_restaurante(self):
        self.cards_restaurantes.first.click()

    def validar_pagina_de_detalhes(self):
        expect(self.page).to_have_url(re.compile(r".*/restaurant\.html\?id=\d+"))
        expect(self.nome_restaurante).to_be_visible()
        expect(self.itens_cardapio.first).to_be_visible()
