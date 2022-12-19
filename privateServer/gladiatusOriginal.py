from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from imgToText import imgtotext
from printAntiBot import printantibot
from cortarPrint import cortarprint
from PIL import Image

#Variáveis de inicialização
usuario = 'knov1991'
email = 'lucasf1991@hotmail.com'
senha = 'knov972468'
expMonstro = 0 #0~3 // 0=monstro mais fraco // 3=boss


# Iniciar o navegador do 0
options = webdriver.ChromeOptions()
#options.add_argument('start-maximized')
options.add_argument('headless')
options.add_argument('window-size=1920,1080')
options.add_argument('log-level=3')
driver = webdriver.Chrome(options=options)
driver.get('https://lobby.gladiatus.gameforge.com/pt_BR')

#LOGIN
def telaLogin():
  try:
    sleep(3)
    menuLogin = driver.find_elements(By.CLASS_NAME, 'tabsList')[0].find_elements(By.TAG_NAME, 'li')[0]
    print(menuLogin)
    menuLogin.click()
    sleep(0.5)
    user = driver.find_element(By.NAME, 'email')
    user.send_keys(email)
    sleep(0.5)
    pasw = driver.find_element(By.NAME, 'password')
    pasw.send_keys(senha)
    sleep(0.5)
    btnLogin = driver.find_element(By.CSS_SELECTOR, ".button-lg")
    btnLogin.click()
    sleep(8)
    driver.get_screenshot_as_file('screenshots/login.png')

    btnServer = driver.find_element(By.CSS_SELECTOR, ".button-default")
    btnServer.click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
  except:
    print('login falhou!')


#EXPEDITION
def expedition():
  try:
    exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
    expTimer = exp.find_element(By.ID, 'cooldown_bar_text_expedition')
    expBtn = exp.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    if expTimer.text == 'Ir em Expedição': #Go to expedition
      expBtn.click()
      sleep(3)
    # TODO - else: retornar erro caso expedição esteja em CD, pra n gastar GEMAS sem querer!!!
    exp = driver.find_element(By.ID, 'cooldown_bar_expedition')
    expTimer = exp.find_element(By.ID, 'cooldown_bar_text_expedition')
    expBtnAtacar = driver.find_elements(By.CLASS_NAME, 'expedition_button')
    if expTimer.text == 'Ir em Expedição' and len(expBtnAtacar) > 0:
      print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Expedição!')
      # posições de 0 a 3, sendo 0 o monstro mais fraco e 3 o boss
      expBtnAtacar[expMonstro].click()
      sleep(2)
      driver.save_screenshot('screenshots/expedition.png')
  except:
    pass

#DUNGEON
#dif1 by.name[0] - inicia dun modo normal
def dungeon():
  try:
    dun = driver.find_element(By.ID, 'cooldown_bar_dungeon')
    dunTimer = dun.find_element(By.ID, 'cooldown_bar_text_dungeon')
    dunBtn = dun.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    if dunTimer.text == 'Ir para a Masmorra': #Go to dungeon
      dunBtn.click()
      sleep(3)
    # TODO - esle: retornar erro caso dungeon esteja em CD, pra n gastar GEMAS sem querer!!!
    dun = driver.find_element(By.ID, 'cooldown_bar_dungeon')
    dunPontos = driver.find_elements(By.CLASS_NAME, 'dungeon_header_open')
    if len(dunPontos) == 0:
      dunNormal = driver.find_elements(By.CLASS_NAME, 'button1')[0]
      dunNormal.click()
      sleep(3)
      dunPontos = driver.find_elements(By.CLASS_NAME, 'dungeon_header_open')
    if len(dunPontos) > 0:
      btnDunAtacar = driver.find_elements(By.CLASS_NAME, 'map_label')[0]
      print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Dungeon!')
      btnDunAtacar.click()
      sleep(2)
      driver.save_screenshot('screenshots/dungeon.png')
  except:
    pass

#ARENA
def arena(): 
  try:
    arena = driver.find_element(By.ID, 'cooldown_bar_arena')
    arenaTimer = arena.find_element(By.ID, 'cooldown_bar_text_arena')
    arenaBtn = arena.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    if arenaTimer.text == 'Ir para a Arena': #Go Arena
      arenaBtn.click()
      sleep(3)
      arenaAtacar = driver.find_elements(By.CLASS_NAME, 'attack')[0]
      print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Arena!')
      arenaAtacar.click()
      sleep(3)
      driver.save_screenshot('screenshots/arena.png')
  except:
    pass

#ARENA MERCENARIOS
def arenaMercenario():
  try:
    arenaMerc = driver.find_element(By.ID, 'cooldown_bar_ct')
    arenaMercTimer = arenaMerc.find_element(By.ID, 'cooldown_bar_text_ct')
    arenaMercBtn = arenaMerc.find_elements(By.CLASS_NAME, 'cooldown_bar_link')[0]
    if arenaMercTimer.text == 'Para o Circus Turma': #Go Arena Mercenario
      arenaMercBtn.click()
      sleep(3)
      arenaMercAtacar = driver.find_elements(By.CLASS_NAME, 'attack')[0]
      print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), '- Arena Mercenario!')
      arenaMercAtacar.click()
      sleep(3)
      driver.save_screenshot('screenshots/arenaMerc.png')
  except:
    pass

def notification():
  try:
    #lvlup
    noti = driver.find_element(By.ID, 'blackoutDialognotification')
    if noti:
      notiBtn = noti.find_element(By.CSS_SELECTOR, '.awesome-button')
      notiBtn.click()
      sleep(2)
  except:
    pass
  


sleep(2)
print('iniciando')
telaLogin()
#Iniciar Bot
while True:
  driver.save_screenshot('screenshots/verificaTimers.png')
  notification()
  sleep(1)
  
  expedition()
  sleep(1)
  
  dungeon()
  sleep(1)
  
  arenaMercenario()
  sleep(1)
  
  #arena()
  #sleep(1)
  
