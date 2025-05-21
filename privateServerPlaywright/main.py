from playwright.sync_api import sync_playwright
import time
from datetime import datetime, timedelta
from imgToText import imgtotext

stat = 3 #1=str, 2=dex, 3=agi, 4=con, 5=car, 6=int


# Refresh
tempo_atual = datetime.now()
tempo_refresh = timedelta(minutes=10)
def refresh_page(page):
    global tempo_atual
    if datetime.now() - tempo_atual > tempo_refresh:
        try:
            page.reload()
            tempo_atual = datetime.now()
        except Exception as e:
            print(f"Erro ao fazer refresh: {e}")

def main():
    with sync_playwright() as p:
        # Iniciar o navegador
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()
        
        # Navegar para o site
        page.goto('https://s16.gladiatuspvp.com/index.php')
        
        print('Iniciando bot')
        
        try:
            while True:
                # Tentar fazer login se necessário
                tela_login(page)
                time.sleep(1)
                
                # Verificar e executar expedição
                executar_expedicao(page)
                
                # Verificar e executar dungeon
                executar_dungeon(page)
                
                # Refresh
                refresh_page(page)
                
                # Treinar
                treinar(page)
                
                # Esperar antes do próximo ciclo
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("Bot interrompido manualmente")
        finally:
            browser.close()

def tela_login(page):
    """Função que realiza o login caso necessário"""
    try:
        # Verifica se elementos de login estão presentes
        if page.locator('#login_username').is_visible():
            # Username
            page.locator('#login_username').fill('knov1991')
            time.sleep(0.1)
            
            # Password
            page.locator('#login_password').fill('knov972468')
            time.sleep(0.1)
            
            # Clicar no botão de login
            page.locator('#loginsubmit').click()
            time.sleep(0.5)
    except Exception as e:
        print(f"Erro ao fazer login: {e}")

def verifica_bot(page):
    """Função que verifica e resolve o captcha anti-bot"""
    try:
        # Verificar se o anti-bot está presente
        if page.locator('input[name="nobot"]').is_visible():
            # Tirar screenshot para o EasyOCR
            printantibot(page)
            time.sleep(2)
            
            # Obter texto da imagem e preencher
            captcha_text = imgtotext()
            page.locator('input[name="nobot"]').fill(captcha_text)
            time.sleep(0.5)
            
            # Clicar no botão de verificação
            page.locator('input[name="verifyme"]').click()
            print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'AntiBot resolvido')
            time.sleep(0.5)
            return True
    except Exception as e:
        print(f"Erro ao verificar anti-bot: {e}")
    return False

def executar_expedicao(page):
    """Função que executa expedições"""
    try:
        # Verificar botão de expedição
        btn_expedition = page.locator('#zegar3')
        
        # Verificar texto do botão (se disponível para expedição)
        if btn_expedition.is_visible():
            expedition_text = btn_expedition.text_content()
            
            # Se estiver disponível para expedição, clicar
            if expedition_text == 'Keşif seferine geç':  # Go to expedition
                btn_expedition.click()
                time.sleep(1)
                
                # Verificar anti-bot
                verifica_bot(page)
                
                # Obter botão de expedição novamente após possível anti-bot
                expedition_text = page.locator('#zegar3').text_content()
                
                # Verificar se há botões de ataque
                attack_buttons = page.locator('.expedition_button')
                if expedition_text == 'Keşif seferine geç' and attack_buttons.count() > 0:
                    print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Expedição!')
                    # Atacar o monstro mais fraco (posição 0)
                    attack_buttons.nth(0).click()
                    return True
    except Exception as e:
        print(f"Erro na expedição: {e}")
    return False

def executar_dungeon(page):
    """Função que executa dungeons"""
    try:
        # Verificar botão de dungeon
        btn_dungeon = page.locator('#zegar4')
        
        # Verificar texto do botão (se disponível para dungeon)
        if btn_dungeon.is_visible():
            dungeon_text = btn_dungeon.text_content()
            
            # Se estiver disponível para dungeon, clicar
            if dungeon_text == 'Zindana geç':  # Go to dungeon
                btn_dungeon.click()
                time.sleep(1)
                
                # Verificar anti-bot
                verifica_bot(page)
                
                # Obter botão de dungeon novamente após possível anti-bot
                dungeon_text = page.locator('#zegar4').text_content()
                
                # Verificar se há botões de ataque
                attack_buttons = page.locator('.expedition_button')
                if dungeon_text == 'Zindana geç' and attack_buttons.count() > 0:
                    print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Dungeon!')
                    # Atacar o último monstro (boss)
                    attack_buttons.nth(attack_buttons.count() - 1).click()
                    return True
    except Exception as e:
        print(f"Erro no dungeon: {e}")
    return False


def treinar(page):
    try:
        page.goto('https://s16.gladiatuspvp.com/egitim.php')
        page.wait_for_timeout(2000)
        if page.locator("#coklue").is_visible():
            set_stat1 = page.locator("#coklue")
            set_stat_qtd = page.locator("#gmiktar")
            buy_stat = page.locator(".buttonegitim")

            set_stat1.select_option(str(stat))
            page.wait_for_timeout(100)
            set_stat_qtd.fill('1000')
            page.wait_for_timeout(100)
            buy_stat.nth(0).click()
            page.wait_for_timeout(2000)
    except Exception as e:
        print(f"Erro ao treinar: {e}")

def printantibot(page):
    page.screenshot(
        path='screenshots/bot.jpg',
        clip={"x": 460, "y": 300, "width": 80, "height": 80}
    )
    time.sleep(2)

if __name__ == "__main__":
    main()