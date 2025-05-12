from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')
EXPEDITION = __import__('expedition')
LINKS = __import__('links')
CONFIG = __import__('config')

#Variáveis
stat_price = 0

def loop(driver, stat, sh):
  global stat_price
  try:
    NOTIFICATION.loop(driver)
    if stat_price == 0:
      LINKS.link_tela_treinamento(driver, sh)
      stat_price = int(driver.find_elements(By.CLASS_NAME, 'training_costs')[stat].text.replace('.',''))
      sleep(0.2)
      VERIFICAR.resultado(driver, 'Preço-treinamento: '+str(stat_price))
    else:
      gold = VERIFICAR.verificar_gold(driver)
      sleep(0.1)
      if gold >= stat_price:
        LINKS.link_tela_treinamento(driver, sh)
        realizar_treinamento(driver, stat, sh).click()
        VERIFICAR.resultado(driver, 'Treinando!')
        stat_price = int(driver.find_elements(By.CLASS_NAME, 'training_costs')[stat].text.replace('.',''))
        sleep(0.2)
        VERIFICAR.resultado(driver, 'Preço-treinamento: '+str(stat_price))
        sleep(1)
  except:
    pass

def realizar_treinamento(driver, stat, sh):
  try:
    sleep(0.2)
    #training_box = driver.find_element(By.ID, 'training_box')
    #treino = training_box.find_element(By.XPATH, "//a[@href='index.php?mod=training&submod=train&skillToTrain="+str(1+stat)+"&sh="+str(sh)+"']")
    #treino.click()
    driver.get(CONFIG.login_data['index_url']+'?mod=training&submod=train&skillToTrain='+str(stat+1)+'&sh='+str(sh))
    sleep(3)
  except:
    VERIFICAR.resultado(driver, 'Falha no treinamento!')