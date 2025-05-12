from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')

def loop(driver):
  bonus = daily_bonus(driver)
  if bonus != False:
    VERIFICAR.resultado(driver, 'Bónus Diário')
    bonus.click()
    sleep(2)
    driver.refresh()
    sleep(3)

  noti = notification(driver)
  if noti and noti != False:
    VERIFICAR.resultado(driver, 'Notificação!')
    noti.click()
    sleep(2)
    driver.refresh()
    sleep(3)

def daily_bonus(driver):
  try:
    return driver.find_element(By.ID, 'linkLoginBonus')
  except:
    return False

def notification(driver):
  try:
    noti_tarefa = driver.find_element(By.ID, 'header_notification').text
    if 'a' in noti_tarefa or 'e' in noti_tarefa or 'o' in noti_tarefa:
      return driver.find_element(By.ID, 'linknotification')
  except:
    return False