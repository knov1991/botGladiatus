import config
from playwright.sync_api import Page

def fazer_login(page: Page):
    logado = False
    while not logado:
        tela_login(page)
        logado = tela_servidor(page)
    return logado

def tela_login(page: Page):
    try:
        page.wait_for_selector('.tabsList >> li', state='visible', timeout=10000)
        page.wait_for_timeout(1000)
        menu_login = (page.locator('.tabsList >> li').all())[0]
        menu_login.click()
        page.wait_for_timeout(500)

        page.fill('input[name="email"]', config.login_data['email'])
        page.wait_for_timeout(500)

        page.fill('input[name="password"]', config.login_data['senha'])
        page.wait_for_timeout(500)

        page.click('.button-lg')
        page.wait_for_timeout(8000)
    except Exception as e:
        print(f"Erro na tela de login: {e}")

def tela_servidor(page: Page):
    try:
        page.click('.button-default')
        page.wait_for_timeout(3000)

        pages = page.context.pages
        if len(pages) > 1:
            print('login realizado com sucesso!')
            return True
        else:
            print('login falhou! Nenhuma nova aba detectada.')
            return False
    except Exception as e:
        print(f"Erro ao selecionar servidor: {e}")
        return False
