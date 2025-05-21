from time import sleep
from playwright.sync_api import Page

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(page: Page, expedition_monster, expedition_hp):
    try:
        NOTIFICATION.loop(page)
        
        # Encontra o elemento de expedição
        exp = page.locator('#cooldown_bar_expedition')
        exp_timer = exp.locator('#cooldown_bar_text_expedition')
        exp_btn = exp.locator('.cooldown_bar_link').first
        
        # Verifica o HP atual
        hp_atual = VERIFICAR.verificar_hp(page)
        
        # Verifica se o cooldown para expedição já terminou
        if exp_timer.text_content() == 'Ir em Expedição' and hp_atual >= expedition_hp:
            exp_btn.click()
            sleep(2)
            
            # Atualiza os elementos após o clique
            exp = page.locator('#cooldown_bar_expedition')
            exp_timer = exp.locator('#cooldown_bar_text_expedition')
            exp_btn_atacar = page.locator('.expedition_button').all()
            
            # Verifica se ainda está na página de expedição e se há botões para atacar
            if exp_timer.text_content() == 'Ir em Expedição' and len(exp_btn_atacar) > 0:
                exp_btn_atacar[expedition_monster].click()  # Clica no monstro escolhido no main.py
                sleep(2)
                VERIFICAR.resultado(page, 'Expedição!')
    except Exception as e:
        # Opcionalmente, você pode adicionar um log de erro aqui
        print(f"Erro na expedição: {e}")
        pass