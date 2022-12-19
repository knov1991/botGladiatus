from time import sleep


def tela_treinamento(driver, sh):
  try:
    driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=training&sh='+str(sh)+'')
    sleep(3)
  except:
    pass

def tela_mercado(driver, sh):
  try:
    driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=market&sh='+str(sh)+'')
    sleep(3)
  except:
    pass