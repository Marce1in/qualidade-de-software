import re
import uuid
from pathlib import Path

import pytest
from playwright.sync_api import expect, sync_playwright
from pytest_bdd import given, parsers, scenarios, then, when


BASE_URL = "https://local-eats-unisenac.vercel.app/static"
FEATURES_DIR = Path(__file__).parent.parent / "features"

scenarios(str(FEATURES_DIR / "busca_restaurantes.feature"))


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


@given("que o usuario autenticado esta na pagina de exploracao")
def usuario_autenticado_na_exploracao(page):
    email = f"bdd-{uuid.uuid4().hex[:8]}@teste.com"

    page.goto(f"{BASE_URL}/login.html")
    page.get_by_role("button", name="Criar Conta").click()
    page.locator("#regName").fill("Usuario BDD")
    page.locator("#regEmail").fill(email)
    page.locator("#regPassword").fill("123456")
    page.get_by_role("button", name="Registrar").click()

    expect(page).to_have_url(re.compile(r".*/index\.html"))
    expect(page.locator("#restaurantGrid .rest-card").first).to_be_visible()


@when(parsers.parse('pesquisar por "{termo}"'))
def pesquisar_por_termo(page, termo):
    page.locator("#searchInput").fill(termo)
    page.locator("#searchBtn").click()


@then("o sistema deve exibir restaurantes encontrados")
def validar_resultados_encontrados(page):
    grid = page.locator("#restaurantGrid")
    primeiro_card = grid.locator(".rest-card").first

    expect(primeiro_card).to_be_visible()
    expect(grid).to_contain_text("Centro")


@then("o sistema deve informar que nenhum restaurante foi encontrado")
def validar_resultado_vazio(page):
    expect(page.locator("#restaurantGrid")).to_contain_text(
        "Nenhum restaurante encontrado."
    )
