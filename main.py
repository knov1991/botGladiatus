from bot import BrowserGameBot
import os
from time import sleep
from datetime import datetime, timedelta


# Variáveis de inicialização
expedition_monster = 1 #0 a 3 // boss = 3
expedition_hp = 50
arena_hp = 95
hp_usar_food = 50
stat = 1 #0=str, 1=dex, 2=agi, 3=con, 4=car, 5=int
sh = False
dungeon_rank = 0 #0 = normal, 1 = avançado
mission_text = ['Circus', 'Encontre', 'Vence', 'Elefante Demon']
mission_text_not = ['seguida', 'promoção', 'consecutiv']
mission_text_combo = ['Mesoai-Oasi', 'sua escolha']

# Imports dos módulos personalizados
LOGIN = __import__('login')
NOTIFICATION = __import__('notification')
EXPEDITION = __import__('expedition')
DUNGEON = __import__('dungeon')
ARENA = __import__('arena')
ARENA_MERCENARIO = __import__('arena_mercenario')
TREINAR = __import__('treinar')
VERIFICAR = __import__('verificar')
# MISSION = __import__('mission')
CONFIG = __import__('config')
# GUILD_MARKET = __import__('guild_market')
# FOOD = __import__('food')


# Caminho onde os dados da sessão ficarão salvos (cookies, localStorage, etc.)
USER_DATA = os.path.abspath(f"./gladiatus_playwright_session/{CONFIG.login_data['account_name']}-{CONFIG.login_data['server_country']}-{CONFIG.login_data['server_number']}")


# Refresh
start_time = datetime.now()
refresh_time = timedelta(minutes=10)
def refresh_page(page):
    global start_time
    if datetime.now() - start_time > refresh_time:
        page.reload()
        start_time = datetime.now()


def main():
    """Função principal que executa o fluxo do bot"""
    # Inicializa o bot
    bot = BrowserGameBot(url=CONFIG.login_data['url'], username=CONFIG.login_data['email'], password=CONFIG.login_data['senha'])
    
    try:
        # Inicia o navegador
        page = bot.iniciar(browser_session=USER_DATA)
        
        LOGIN.fazer_login(page)

        # Fecha paginas anteriores
        pages = page.context.pages
        if len(pages) > 1:
            [page.close() for page in pages[:-1]]
            page = pages[-1]
        page.bring_to_front()
        sleep(3)

        # Esperar SH
        sh = False
        while not sh:
            sh = VERIFICAR.get_sh(page)

        CONFIG.login_data['index_url'] = f"https://s{CONFIG.login_data['server_number']}-{CONFIG.login_data['server_country']}.gladiatus.gameforge.com/game/index.php"
        CONFIG.login_data['ajax_url'] = f"https://s{CONFIG.login_data['server_number']}-{CONFIG.login_data['server_country']}.gladiatus.gameforge.com/game/ajax.php"

        print("Iniciando BOT...")
        while True:
            # Refresh caso internet caia e evitar bugs
            refresh_page(page)

            NOTIFICATION.loop(page)
            # MISSION.loop(driver, sh, mission_text, mission_text_not, mission_text_combo)
            ARENA_MERCENARIO.loop(page)
            EXPEDITION.loop(page, expedition_monster, expedition_hp)
            DUNGEON.loop(page, dungeon_rank)
            ARENA.loop(page, arena_hp)
            TREINAR.loop(page, stat, sh)
            # GUILD_MARKET.loop(driver, sh)
            # FOOD.loop(driver, sh, hp_usar_food)
            sleep(5)
            
        
        # Mantém o navegador aberto até que o usuário decida encerrar
        # input("\nBot em execução. Pressione Enter para encerrar...\n")
        
    except Exception as e:
        print(f"Erro durante a execução do bot: {e}")
    finally:
        # Garante que os recursos são liberados adequadamente
        bot.finalizar()


if __name__ == "__main__":
    main()