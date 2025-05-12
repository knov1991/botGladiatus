from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from seleniumrequests import Firefox, Chrome

#Variáveis de inicialização
expedition_monster = 3 #0~3 // 0=monstro mais fraco // 3=boss
expedition_hp = 40
arena_hp = 50
hp_usar_food = 40

#treinar
#stat_list = ['str', 'dex', 'agi', 'con', 'car', 'int']
stat = 2 #0~5

sh = False
dungeon_rank = 1 # 0 = normal // 1 = avançado
#mission_text = ['Circus', 'Encontre', 'Vence', 'Guarda da Caravana']
mission_text = ['Circus', 'Encontre', 'Vence', 'Elefante Demon']
mission_text_not = ['seguida', 'promoção', 'consecutiv']
mission_text_combo = ['Mesoai-Oasi', 'sua escolha']


# Iniciar o navegador/browser // start-maximized = assistir bot // headless(+window_size - não necessário) = bot background 
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')

#options.add_experimental_option('debuggerAddress', 'localhost:10001')
#adicionar essa linha no atralho do chrome
#--remote-debugging-port="10001" --user-data-dir="D:\Developer\Meus Projetos\Python\botGladiatus\Chrome-Gladiatus-MadKoala"

#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_argument('headless')
#options.add_argument('window-size=1920,1080')
options.add_argument('log-level=3')
#driver = webdriver.Chrome(options=options)

#Imports dos outros arquivos python
LOGIN = __import__('login')
NOTIFICATION = __import__('notification')
EXPEDITION = __import__('expedition')
DUNGEON = __import__('dungeon')
ARENA = __import__('arena')
ARENA_MERCENARIO = __import__('arena_mercenario')
TREINAR = __import__('treinar')
VERIFICAR = __import__('verificar')
MISSION = __import__('mission')
CONFIG = __import__('config')
GUILD_MARKET = __import__('guild_market')
FOOD = __import__('food')





#INICIAR BOT
with Chrome(options=options) as driver:
  #LOGIN
  driver.get('https://lobby.gladiatus.gameforge.com/pt_BR')
  LOGIN.logar(driver)
  

  while sh == False:
      sh = VERIFICAR.get_sh(driver)
  CONFIG.login_data['index_url'] = f"https://s{CONFIG.login_data['server_number']}-{CONFIG.login_data['server_country']}.gladiatus.gameforge.com/game/index.php"
  CONFIG.login_data['ajax_url'] = f"https://s{CONFIG.login_data['server_number']}-{CONFIG.login_data['server_country']}.gladiatus.gameforge.com/game/ajax.php"

  while True:  
    """ NOTIFICATION.loop(driver)
    MISSION.loop(driver, sh, mission_text, mission_text_not, mission_text_combo)
    ARENA_MERCENARIO.loop(driver)
    EXPEDITION.loop(driver, expedition_monster, expedition_hp)
    DUNGEON.loop(driver, dungeon_rank)
    ARENA.loop(driver, arena_hp)
    TREINAR.loop(driver, stat, sh)
    GUILD_MARKET.loop(driver, sh)
    FOOD.loop(driver, sh, hp_usar_food) """


    #treinar em evento
    #driver.get(CONFIG.login_data['index_url'] + f"?mod=training&submod=train&skillToTrain=2&sh={str(sh)}") #dex
    #sleep(0.1)
    #driver.get(CONFIG.login_data['index_url'] + f"?mod=training&submod=train&skillToTrain=3&sh={str(sh)}") #agi
    #sleep(0.1)
    
    res = driver.request('GET', CONFIG.login_data['index_url']+'?mod=packages&f=7&fq=-1&qry=&page=1&sh='+str(sh))
    print('res:', res)
    soup = BeautifulSoup(res.text, 'lxml')
    print('soup:', soup)
    supa = soup.find('input', attrs={'name' : 'packages[]'})['value']
    print('supa:', supa)

    print('fim')
    sleep(10)