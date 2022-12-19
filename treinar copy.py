from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')
EXPEDITION = __import__('expedition')

#Variáveis
stat_price = 0

def loop(driver, treinar, stat, sh):
  global stat_price
  try:
    NOTIFICATION.loop(driver)
    
    if treinar == True:
      if stat_price == 0:
        tela_treinar(driver, sh)
        stat_price = int(driver.find_elements(By.CLASS_NAME, 'training_costs')[stat].text.replace('.',''))
        sleep(0.2)
        print('preço-treinamento:', stat_price)
      else:
        gold = int(VERIFICAR.verificar_gold(driver).replace('.',''))
        sleep(0.1)
        if gold >= stat_price:
          tela_treinar(driver, sh)
          realizar_treinamento(driver, stat, sh).click()
          VERIFICAR.resultado(driver, 'Treinando!')
          stat_price = int(driver.find_elements(By.CLASS_NAME, 'training_costs')[stat].text.replace('.',''))
          print('preço-treinamento:', stat_price)
          sleep(1)
  except:
    pass

def refresh_treinamento(driver):
  try:
    submenu = driver.find_element(By.ID, 'submenu1')
    menu_items = submenu.find_elements(By.CLASS_NAME, 'menuitem')
    for i in range(len(menu_items)):
      if menu_items[i].text == 'Treino':
        menu_items[i].click()
        sleep(3)
  except:
    pass

def tela_treinar(driver, sh):
  try:
    """ sleep(0.3)
    driver.execute_script("document.getElementById('submenuhead2').style.cssText = 'display: none;'")
    driver.execute_script("document.getElementById('submenuhead1').style.cssText = 'display: block;'")
    sleep(0.5)
    menu = driver.find_element(By.ID, 'submenuhead1')
    sleep(0.2)
    menu_city = menu.find_elements(By.CLASS_NAME, 'menutab_city')[0]
    sleep(0.2)
    menu_city_btn = menu_city.find_elements(By.CLASS_NAME, 'submenuswitch')[0]
    sleep(0.2)
    menu_city_btn.click() """
    driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=training&sh='+str(sh)+'')
    sleep(3)
  except:
    pass

def realizar_treinamento(driver, stat, sh):
  try:
    sleep(0.2)
    training_box = driver.find_element(By.ID, 'training_box')
    treino = training_box.find_element(By.XPATH, "//a[@href='index.php?mod=training&submod=train&skillToTrain="+str(1+stat)+"&sh="+str(sh)+"']")
    treino.click()
    sleep(3)
  except:
    print('não achou botão de treinamento!')