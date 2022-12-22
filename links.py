from time import sleep


def link_tela_treinamento(driver, sh):
  try:
    driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=training&sh='+str(sh)+'')
    sleep(3)
  except:
    pass

def link_tela_mission(driver, sh):
  try:
    driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=quests&sh='+str(sh)+'')
    sleep(3)
  except:
    pass

def link_tela_mercado(driver, sh):
  try:
    driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=market&sh='+str(sh)+'')
    sleep(3)
  except:
    pass

def link_refresh_treinamento(driver, sh):
  try:
    driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=quests&submod=resetQuests&sh='+str(sh)+'')
    sleep(3)
  except:
    pass