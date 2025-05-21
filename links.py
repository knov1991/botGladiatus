from time import sleep
from playwright.sync_api import Page

CONFIG = __import__('config')

def link_tela_treinamento(page: Page, sh):
    try:
        page.goto(f'https://s{CONFIG.login_data["server_number"]}-{CONFIG.login_data["server_country"]}.gladiatus.gameforge.com/game/index.php?mod=training&sh={sh}')
        sleep(3)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao acessar tela de treinamento: {e}")
        pass

def link_tela_mission(page: Page, sh):
    try:
        page.goto(f'https://s{CONFIG.login_data["server_number"]}-{CONFIG.login_data["server_country"]}.gladiatus.gameforge.com/game/index.php?mod=quests&sh={sh}')
        sleep(3)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao acessar tela de missões: {e}")
        pass

def link_tela_mercado(page: Page, sh):
    try:
        page.goto(f'https://s{CONFIG.login_data["server_number"]}-{CONFIG.login_data["server_country"]}.gladiatus.gameforge.com/game/index.php?mod=market&sh={sh}')
        sleep(3)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao acessar tela de mercado: {e}")
        pass

def link_refresh_treinamento(page: Page, sh):
    try:
        page.goto(f'https://s{CONFIG.login_data["server_number"]}-{CONFIG.login_data["server_country"]}.gladiatus.gameforge.com/game/index.php?mod=quests&submod=resetQuests&sh={sh}')
        sleep(3)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao atualizar treinamento: {e}")
        pass

def link_guild_market(page: Page, sh):
    try:
        page.goto(f'https://s{CONFIG.login_data["server_number"]}-{CONFIG.login_data["server_country"]}.gladiatus.gameforge.com/game/index.php?mod=guildMarket&sh={sh}')
        sleep(3)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao acessar mercado da guilda: {e}")
        pass

def link_storage_forge_items(page: Page, sh):
    try:
        # https://s58-br.gladiatus.gameforge.com/game/ajax.php?mod=forge&submod=storageIn
        page.goto(f'{CONFIG.login_data["ajax_url"]}?mod=forge&submod=storageIn&sh={sh}')
        sleep(3)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro ao guardar itens de forja: {e}")
        pass