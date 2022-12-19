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
      sleep(3)
      arena_mercenario_atacar = driver.find_elements(By.CLASS_NAME, 'attack')[0]
      VERIFICAR.resultado(driver, 'Arena Mercenario!')
      arena_mercenario_atacar.click()
      sleep(3)
  except:
    pass