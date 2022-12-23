from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Variáveis de inicialização
email = 'lucasf1991@hotmail.com'
senha = 'knov972468'
#email = 'lucasf@unipam.edu.br'
#senha = 'Knov972468'
expedition_monster = 0 #0~3 // 0=monstro mais fraco // 3=boss
expedition_hp = 60
#treinamento
treinar = False
#stat_list = ['str', 'dex', 'agi', 'con', 'car', 'int']
stat = 2
sh = False
mission_text = ['Circus', 'Encontre', 'Vence', 'Campo Viking', 'Soldado Renegado']
mission_text_not = ['seguida', 'promoção', 'consecutiv']


# Iniciar o navegador/browser // start-maximized = assistir bot // headless(+window_size - não necessário) = bot background 
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
#options.add_argument('headless')
#options.add_argument('window-size=1920,1080')
options.add_argument('log-level=3')
driver = webdriver.Chrome(options=options)
driver.get('https://lobby.gladiatus.gameforge.com/pt_BR')

#Imports dos outros arquivos python
LOGIN = __import__('login')
NOTIFICATION = __import__('notification')
EXPEDITION = __import__('expedition')
DUNGEON = __import__('dungeon')
ARENA_MERCENARIO = __import__('arena_mercenario')
TREINAR = __import__('treinar')
VERIFICAR = __import__('verificar')
MISSION = __import__('mission')


#INICIAR BOT
LOGIN.logar(driver, email, senha)
while True:
  while sh == False:
    sh = VERIFICAR.get_sh(driver)
  NOTIFICATION.loop(driver)
  MISSION.loop(driver, sh, mission_text, mission_text_not)
  EXPEDITION.loop(driver, expedition_monster, expedition_hp)
  DUNGEON.loop(driver)
  ARENA_MERCENARIO.loop(driver)
  TREINAR.loop(driver, treinar, stat, sh)