from datetime import datetime
from time import sleep
from playwright.sync_api import Page, expect

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(page: Page, arena_hp):
    try:
        NOTIFICATION.loop(page)
        
        # Encontra os elementos da arena
        arena = page.locator('#cooldown_bar_arena')
        arena_timer = arena.locator('#cooldown_bar_text_arena')
        arena_btn = arena.locator('.cooldown_bar_link').first
        
        # Verifica o HP atual
        hp_atual = VERIFICAR.verificar_hp(page)
        
        # Verifica se o timer da arena está pronto e se tem HP suficiente
        if arena_timer.text_content() == 'Ir para a Arena' and hp_atual >= arena_hp:
            arena_btn.click()
            sleep(2)
            
            # Encontra os botões de ataque
            arena_atacar = page.locator('.attack').all()
            
            if len(arena_atacar) > 0:
                VERIFICAR.resultado(page, 'Arena!')
                arena_atacar[0].click()
                sleep(2)
                
                # Verifica se houve ataque repetido
                ataque_repetido(page, arena_atacar)
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        # print(f"Erro na arena: {e}")
        pass

def ataque_repetido(page: Page, arena_atacar):
    try:
        # Verifica se apareceu o diálogo de ataque repetido
        header_text = page.locator('#header_bod').text_content()
        i = 1
        
        # Enquanto o diálogo de ataque repetido estiver visível
        while header_text == 'Atacar na mesma?':
            # Encontra o botão de cancelar e clica nele
            # Usando o segundo botão que possui o onclick="blackoutDialog(false)"
            btn_cancel = page.locator("input[onclick='blackoutDialog(false)']").nth(1)
            btn_cancel.click()
            sleep(0.2)
            
            # Tenta clicar no próximo oponente se houver
            if i < len(arena_atacar):
                arena_atacar[i].click()
                sleep(2)
                i += 1
                
                # Verifica novamente o texto do cabeçalho
                try:
                    header_text = page.locator('#header_bod').text_content()
                except:
                    # Se não conseguir obter o texto, assume que o diálogo foi fechado
                    break
            else:
                # Sai do loop se não houver mais oponentes para atacar
                break
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        # print(f"Erro ao verificar ataque repetido: {e}")
        pass