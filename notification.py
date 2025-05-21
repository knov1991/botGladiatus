from time import sleep
from playwright.sync_api import Page

VERIFICAR = __import__('verificar')

def loop(page: Page):
    daily_bonus(page)

    notification(page)

    loot = loot_bonus(page)
    if loot:
        VERIFICAR.resultado(page, 'Loot!')
        loot.click()
        sleep(2)
        page.reload()
        sleep(3)

    loot_link_notification(page)

def daily_bonus(page: Page):
    try:
        # Usando o método wait_for_selector para garantir que o elemento esteja visível
        bonus_element = page.wait_for_selector('#linkLoginBonus', timeout=1000)
        VERIFICAR.resultado(page, 'Bónus Diário')
        bonus_element.click()
        sleep(2)
        page.reload()
        sleep(3)
    except:
        pass

def notification(page: Page):
    try:
        # Obtém o texto da notificação
        noti_tarefa = page.locator('#header_notification').text_content()
        if 'a' in noti_tarefa or 'e' in noti_tarefa or 'o' in noti_tarefa:
            # Retorna o elemento linknotification
            link_not = page.locator('#linknotification')
            VERIFICAR.resultado(page, 'Notificação!')
            link_not.click()
            sleep(2)
            page.reload()
            sleep(3)
    except:
        pass

def loot_bonus(page: Page):
    try:
        # Usando o método wait_for_selector para garantir que o elemento esteja visível
        bonus_elements = page.locator('.loot-button').all()
        if len(bonus_elements) > 0:
            VERIFICAR.resultado(page, 'Loot!')
            bonus_elements[-1].click()
            sleep(2)
            page.reload()
            sleep(3)
    except:
        pass

def loot_link_notification(page: Page):
    try:
        noti_tarefa = page.locator('#linknotification')
        if noti_tarefa.is_visible():
            page.reload()
            sleep(3)
    except:
        pass