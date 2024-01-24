from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from imgToText import imgtotext
from printAntiBot import printantibot

# conectar ao navegador
""" options = Options()
options.add_experimental_option('debuggerAddress', 'localhost:10001')
driver = webdriver.Chrome(options=options) """


# Iniciar o navegador do 0
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('start-maximized')
options.add_argument('log-level=3')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://s16.gladiatuspvp.com/index.php')


#login_username
#login_password
#loginsubmit
#zegar3 = btnExpedition
#zegar4 = btnDungeon

def telalogin():
    try:
        user = driver.find_element(By.ID, 'login_username')
        sleep(0.1)
        # Username
        user.send_keys('')
        sleep(0.1)
        user = driver.find_element(By.ID, 'login_password')
        sleep(0.1)
        # Password
        user.send_keys('')
        sleep(0.1)
        btnLogin = driver.find_element(By.ID, 'loginsubmit')
        btnLogin.click()
        return btnLogin
    except:
        pass

def verificabot():
  try:
    driver.get_screenshot_as_file('screenshot.png')
    sleep(1)
    atb = driver.find_element(By.NAME, 'nobot')
    printantibot()
    sleep(2)
    atb.send_keys(str(imgtotext()))
    sleep(0.5)
    btnAntiBot = driver.find_element(By.NAME, 'verifyme')
    sleep(0.1)
    print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'AntiBot')
    btnAntiBot.click()
    sleep(0.5)
  except:
    pass

print('iniciando')
#Iniciar Bot
while True:
  telalogin()
  sleep(1)
  btnExpedition = 0
  btnExpAtacar = 0
  btnDungeon = 0
  btnDunAtacar = 0

  #EXPEDITION
  try:
    btnExpedition = driver.find_element(By.ID, 'zegar3')
    if btnExpedition.text == 'Keşif seferine geç': #Go to expedition
      btnExpedition.click()
      sleep(1)
      verificabot()
    # TODO - esle: retornar erro caso expedição esteja em CD, pra n gastar GEMAS sem querer!!!
    btnExpedition = driver.find_element(By.ID, 'zegar3')
    btnExpAtacar = driver.find_elements(By.CLASS_NAME, 'expedition_button')
    if btnExpedition.text == 'Keşif seferine geç' and len(btnExpAtacar) > 0:
      print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Expedição!')
      # posições de 0 a 3, sendo 0 o monstro mais fraco e 3 o boss
      btnExpAtacar[0].click()
  except:
    pass

  #DUNGEON
  try:
    btnDungeon = driver.find_element(By.ID, 'zegar4')
    if btnDungeon.text == 'Zindana geç': #Go to dungeon
      btnDungeon.click()
      sleep(1)
      verificabot()
    # TODO - esle: retornar erro caso dungeon esteja em CD, pra n gastar GEMAS sem querer!!!
    btnDungeon = driver.find_element(By.ID, 'zegar4')
    btnDunAtacar = driver.find_elements(By.CLASS_NAME, 'expedition_button')
    if btnDungeon.text == 'Zindana geç' and len(btnDunAtacar) > 0:
      print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Dungeon!')
      btnDunAtacar[len(btnDunAtacar)-1].click()
  except:
    pass

  #Tempo de Espera para loop do bot
  sleep(1)