from datetime import datetime
from time import sleep
from playwright.sync_api import Page

def verificar_hp(page: Page):
    sleep(1)
    try:
        hp_text = page.locator('#header_values_hp_percent').inner_text()
        return int(hp_text.strip()[:-1])  # Remove o '%' no final
    except:
        return -1


def verificar_gold(page: Page):
    sleep(0.5)
    try:
        gold_text = page.locator('#sstat_gold_val').inner_text()
        return int(gold_text.replace('.', ''))
    except:
        return -1


def verificar_ruby(page: Page):
    sleep(0.5)
    try:
        ruby_text = page.locator('#sstat_ruby_val').inner_text()
        return int(ruby_text.replace('.', ''))
    except:
        return -1


def resultado(page: Page, mensagem):
    try:
        sleep(0.1)
        gold = verificar_gold(page)
        ruby = verificar_ruby(page)
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'gold:', gold, 'ruby:', ruby, '-', mensagem)
        sleep(0.1)
    except:
        return -1


def get_sh(page: Page):
    try:
        sleep(0.3)
        url = page.url
        sh = url.split('sh=')[1]
        print('sh:', sh)
        return sh
    except:
        print('falha no sh!')
        sleep(3)
        return False
