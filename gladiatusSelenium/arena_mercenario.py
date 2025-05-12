from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(driver):
  try:
    NOTIFICATION.loop(driver)
    
    arena_mercenario = driver.find_element(By.ID, 'cooldown_bar_ct')
    arena_mercenario_timer = arena_mercenario.find_element(By.ID, 'cooldown_bar_text_ct')
    arena_mercenario_btn = arena_mercenario.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    if arena_mercenario_timer.text == 'Para o Circus Turma': #Go Arena Mercenario
      arena_mercenario_btn.click()
      sleep(2)
      arena_mercenario_atacar = driver.find_elements(By.CLASS_NAME, 'attack')
      arena_mercenario_atacar[0].click()
      verificar_multi_attack(driver, arena_mercenario_atacar)
      VERIFICAR.resultado(driver, 'Arena Mercenario!')
      sleep(2)
  except:
    pass

def verificar_multi_attack(driver, arena_mercenario_atacar):
  sleep(2)
  try:
    i = 1
    atk_repetido = driver.find_element(By.ID, 'blackoutDialogbod')
    while atk_repetido:
      btn_cancelar = atk_repetido.find_elements(By.CLASS_NAME, 'ar')[0]
      btn_cancelar.click()
      sleep(0.5)
      print('tentando atacar merc', i)
      arena_mercenario_atacar[i].click()
      sleep(2)
      i+=1
      atk_repetido = driver.find_element(By.ID, 'blackoutDialogbod')
      sleep(0.5)
  except:
    pass