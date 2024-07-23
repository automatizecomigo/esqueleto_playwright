from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page
from credenciais import login, senha

scenarios('../features/login_sucess.features')


# a funcao faz abrir uma nova pagina e acessar o site
@given('que o usuário acessa a página de login do saucedemo')
def pagina_de_login(browser: Page):
    browser.goto('https://www.saucedemo.com/')


# a funcao preenche os campos de login e senha e clica no botao de entrar
@when('o usuário preenche o campo de usuário com "standard_user" e senha com "secret_sauce"')
def preenche_campos(browser: Page):
    browser.locator('[placeholder="Username"]').fill(login)
    browser.locator('[placeholder="Password"]').fill(senha)
    browser.locator('[type="submit"]').click()


# a funcao verifica se o usuário foi redirecionado para a página de produtos
@then("o usuário é redirecionado para a página de produtos")
def verifica_redirecionamento(browser: Page):
    expect(browser.get_by_text('Products')).to_be_visible()
