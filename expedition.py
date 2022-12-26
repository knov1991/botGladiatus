from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(driver, expedition_monster, expedition_hp):
  try:
    NOTIFICATION.loop(driver)
    
    exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
    exp_timer = exp.find_element(By.ID, 'cooldown_bar_text_expedition')
    exp_btn = exp.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    hp_atual = VERIFICAR.verificar_hp(driver)
    if exp_timer.text == 'Ir em Expedição' and hp_atual>= expedition_hp: #Verifica se o cooldown para expedição já terminou
      exp_btn.click()
      sleep(2)
      exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
      exp_timer = exp.find_element(By.ID, 'cooldown_bar_text_expedition')
      exp_btn_atacar = driver.find_elements(By.CLASS_NAME, 'expedition_button')
      if exp_timer.text == 'Ir em Expedição' and len(exp_btn_atacar) > 0:
        VERIFICAR.resultado(driver, 'Expedição!')
        exp_btn_atacar[expedition_monster].click()  #Clica no monstro - escolher no main.py
        sleep(2)
  except:
    pass