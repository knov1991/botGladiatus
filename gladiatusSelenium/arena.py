from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(driver, arena_hp):
  try:
    NOTIFICATION.loop(driver)
    
    arena = driver.find_element(By.ID, 'cooldown_bar_arena')
    arena_timer = arena.find_element(By.ID, 'cooldown_bar_text_arena')
    arena_btn = arena.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    hp_atual = VERIFICAR.verificar_hp(driver)
    if arena_timer.text == 'Ir para a Arena' and hp_atual >= arena_hp: #Go Arena
      arena_btn.click()
      sleep(2)
      arena_atacar = driver.find_elements(By.CLASS_NAME, 'attack')
      VERIFICAR.resultado(driver, 'Arena!')
      arena_atacar[0].click()
      sleep(2)
      ataque_repetido(driver, arena_atacar)
  except:
    pass

def ataque_repetido(driver, arena_atacar):
  try:
    repetido = driver.find_element(By.ID, 'header_bod').text
    i = 1
    while repetido == 'Atacar na mesma?':
      btn_cancel = driver.find_elements(By.XPATH, "//input[@onclick='blackoutDialog(false)']")[1]
      btn_cancel.click()
      sleep(0.2)
      arena_atacar[i].click()
      sleep(2)
      i += 1
      repetido = driver.find_element(By.ID, 'header_bod').text
  except:
    pass