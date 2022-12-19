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
    if exp_timer.text == 'Ir em Expedição' and hp_atual>= expedition_hp: #Go to expedition
      exp_btn.click()
      sleep(3)
      exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
      exp_timer = exp.find_element(By.ID, 'cooldown_bar_text_expedition')
      exp_btn_atacar = driver.find_elements(By.CLASS_NAME, 'expedition_button')
      if exp_timer.text == 'Ir em Expedição' and len(exp_btn_atacar) > 0:
        VERIFICAR.resultado(driver, 'Expedição!')
        # posições de 0 a 3, sendo 0 o monstro mais fraco e 3 o boss
        exp_btn_atacar[expedition_monster].click()
        sleep(2)
  except:
    pass

def refresh_expedition(driver):
  try:
    exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
    exp_btn = exp.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    exp_btn.click()
    sleep(3)
  except:
    pass