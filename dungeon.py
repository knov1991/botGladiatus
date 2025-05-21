from time import sleep
from playwright.sync_api import Page

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')
CONFIG = __import__('config')

def loop(page: Page, dungeon_rank):
    try:
        NOTIFICATION.loop(page)
        
        # Encontra o elemento de dungeon
        dun = page.locator('#cooldown_bar_dungeon')
        dun_timer = dun.locator('#cooldown_bar_text_dungeon')
        dun_btn = dun.locator('.cooldown_bar_link').first
        
        # Verifica se o cooldown para dungeon já terminou
        if dun_timer.text_content() == 'Ir para a Masmorra':
            dun_btn.click()
            sleep(3)
            
            # Atualiza o elemento após o clique
            dun = page.locator('#cooldown_bar_dungeon')
            
            # Verifica se a masmorra está aberta verificando os pontos de dungeon
            dun_pontos = page.locator('.dungeon_header_open').all()
            
            if len(dun_pontos) == 0:
                # Seleciona a dificuldade da masmorra baseado no dungeon_rank
                if dungeon_rank == 0:
                    # Seleciona masmorra normal
                    dun_normal = page.locator('input[name="dif1"]').first
                    dun_normal.click()
                else:
                    # Seleciona masmorra avançada
                    dun_advanced = page.locator('input[name="dif2"]').first
                    dun_advanced.click()
                    
                sleep(3)
                
                # Verifica novamente os pontos de dungeon após selecionar a dificuldade
                dun_pontos = page.locator('.dungeon_header_open').all()
            
            # Encontra o botão de ataque na masmorra usando o seletor da imagem
            # dun_btn_atacar = page.locator("img[src='//gf3.geo.gfsrv.net/cdne6/643cfe405fb9a1fbd99513f08ca7fe.gif']")
            dun_btn_atacar = page.locator(f"img[src='//s{CONFIG.login_data['server_number']}-{CONFIG.login_data['server_country']}.gladiatus.gameforge.com/cdn/img/combatloc.gif?v=1745305460']").last
            dun_btn_atacar.click()
            VERIFICAR.resultado(page, 'Dungeon!')
            sleep(3)
            
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro na dungeon: {e}")
        pass