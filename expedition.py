from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(driver, expedition_monster, expedition_hp):
  try:
    NOTIFICATION.loop(driver)
    
    hp_atual = VERIFICAR.verificar_hp(driver)
    #Verifica se o cooldown para expedição já terminou // verifica hp para atacar
    if expedition_timer(driver) == 'Ir em Expedição' and hp_atual>= expedition_hp:
      expedition_button.click()
      sleep(3)
      exp_btn_atacar = driver.find_elements(By.CLASS_NAME, 'expedition_button')
      if expedition_timer(driver) == 'Ir em Expedição' and len(exp_btn_atacar) > 0:
        VERIFICAR.resultado(driver, 'Expedição!')
        exp_btn_atacar[expedition_monster].click()  #Clica no monstro - escolher em main.py
        sleep(2)
  except:
    pass

def expedition_timer(driver):
  try:
    exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
    return exp.find_element(By.ID, 'cooldown_bar_text_expedition').text
  except:
    pass

def expedition_button(driver):
  try:
    exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
    return exp.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
  except:
    pass