from time import sleep
from playwright.sync_api import Page

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(page: Page):
    try:
        NOTIFICATION.loop(page)
        
        # Encontra os elementos da arena de mercenários
        arena_mercenario = page.locator('#cooldown_bar_ct')
        arena_mercenario_timer = arena_mercenario.locator('#cooldown_bar_text_ct')
        arena_mercenario_btn = arena_mercenario.locator('.cooldown_bar_link').first
        
        # Verifica se o timer da arena está pronto
        if arena_mercenario_timer.text_content() == 'Para o Circus Turma':  # Go Arena Mercenario
            arena_mercenario_btn.click()
            sleep(2)
            
            # Encontra os botões de ataque e clica no primeiro
            arena_mercenario_atacar = page.locator('.attack').all()
            if len(arena_mercenario_atacar) > 0:
                arena_mercenario_atacar[0].click()
                
                # Verifica se houve ataques duplicados e tenta outros oponentes
                verificar_multi_attack(page, arena_mercenario_atacar)
                
                VERIFICAR.resultado(page, 'Arena Mercenario!')
                sleep(2)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        # print(f"Erro na arena de mercenários: {e}")
        pass

def verificar_multi_attack(page: Page, arena_mercenario_atacar):
    sleep(2)
    try:
        i = 1
        
        # Verifica se apareceu o diálogo de ataque repetido
        atk_repetido = page.locator('#blackoutDialogbod')
        
        # Enquanto o diálogo estiver visível, tenta atacar outro oponente
        while atk_repetido.is_visible():
            # Encontra o botão de cancelar e clica nele
            btn_cancelar = atk_repetido.locator('.ar').first
            btn_cancelar.click()
            sleep(0.5)
            
            print('tentando atacar merc', i)
            
            # Tenta clicar no próximo oponente se houver
            if i < len(arena_mercenario_atacar):
                arena_mercenario_atacar[i].click()
                sleep(2)
                i += 1
                
                # Verifica novamente se o diálogo apareceu
                sleep(0.5)
            else:
                # Sai do loop se não houver mais oponentes para atacar
                break
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        # print(f"Erro ao verificar multi-attack: {e}")
        pass