from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By


def verificar_hp(driver):
  sleep(1)
  try: 
    return int(driver.find_element(By.ID, 'header_values_hp_percent').text[:-1])
  except:
    return 0

def verificar_gold(driver):
  sleep(0.5)
  try:
    gold_string = str(driver.find_element(By.ID, 'sstat_gold_val').text)
    return int(gold_string.replace('.',''))
  except:
    return -1

def verificar_ruby(driver):
  sleep(0.5)
  try:
    ruby_string = str(driver.find_element(By.ID, 'sstat_ruby_val').text)
    return int(ruby_string.replace('.',''))
  except:
    return -1

#Mensagem de resultado
def resultado(driver, mensagem):
  try:
    sleep(0.1)
    print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'gold:', verificar_gold(driver), 'ruby:', verificar_ruby(driver), '-', mensagem)
    sleep(0.1)
  except:
    return -1

#Pegar SH da ULR, usado para encontrar rota href no treinamento
def get_sh(driver):
  try:
    sleep(0.3)
    url = driver.current_url
    sh = url.split('sh=')[1]
    print('sh:', sh)
    return sh
  except:
    print('falha no sh!')
    return False