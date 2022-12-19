from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(driver):
  try:
    NOTIFICATION.loop(driver)
    
    dun = driver.find_element(By.ID, 'cooldown_bar_dungeon')
    dun_timer = dun.find_element(By.ID, 'cooldown_bar_text_dungeon')
    dun_btn = dun.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    if dun_timer.text == 'Ir para a Masmorra': #Go to dungeon
      dun_btn.click()
      sleep(3)
      dun = driver.find_element(By.ID, 'cooldown_bar_dungeon')
      dun_pontos = driver.find_elements(By.CLASS_NAME, 'dungeon_header_open')
      if len(dun_pontos) == 0:
        dun_normal = driver.find_elements(By.CLASS_NAME, 'button1')[0]
        dun_normal.click()
        sleep(3)
        dun_pontos = driver.find_elements(By.CLASS_NAME, 'dungeon_header_open')
      dun_btn_atacar =   driver.find_element(By.CSS_SELECTOR, "img[src='//gf3.geo.gfsrv.net/cdne6/643cfe405fb9a1fbd99513f08ca7fe.gif']")
      VERIFICAR.resultado(driver, 'Dungeon!')
      dun_btn_atacar.click()
      sleep(3)
  except:
    pass
