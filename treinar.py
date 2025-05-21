from time import sleep
from playwright.sync_api import Page

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')
EXPEDITION = __import__('expedition')
LINKS = __import__('links')
CONFIG = __import__('config')

# Variáveis
stat_price = 0

def loop(page: Page, stat, sh):
    global stat_price
    try:
        NOTIFICATION.loop(page)
        
        gold = VERIFICAR.verificar_gold(page)
        sleep(0.1)
        
        if gold >= stat_price:
            realizar_treinamento(page, stat, sh)
            stat_price = obter_preco_treinamento(page, stat)

    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro no treinamento: {e}")
        pass

def obter_preco_treinamento(page: Page, stat):
    try:
        training_costs = page.locator('.training_costs').all_text_contents()
        stat_price_text = training_costs[stat].replace('.', '')
        stat_price = int(stat_price_text)
        sleep(0.2)
        VERIFICAR.resultado(page, f'Preço-proximo-treinamento: {stat_price}')
        return stat_price
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao obter preço de treinamento: {e}")
        return False

def realizar_treinamento(page: Page, stat, sh):
    try:
        sleep(0.2)
        # Tenta treinar, sucesso caso tenha gold suficiente
        url = f"{CONFIG.login_data['index_url']}?mod=training&submod=train&skillToTrain={stat+1}&sh={sh}"
        page.goto(url)
        sleep(3)
    except Exception as e:
        VERIFICAR.resultado(page, 'Falha no treinamento!')
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao realizar treinamento: {e}")
        return False