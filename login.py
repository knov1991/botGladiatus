from time import sleep

from selenium.webdriver.common.by import By

CONFIG = __import__('config')

def logar(driver):
  logado = False
  while logado == False:
    tela_login(driver)
    logado = tela_servidor(driver)

#Primeira tela ao abrir o site do jogo - realizar login
def tela_login(driver):
  try:
    sleep(3)
    menu_login = driver.find_elements(By.CLASS_NAME, 'tabsList')[0].find_elements(By.TAG_NAME, 'li')[0]
    menu_login.click()
    sleep(0.5)

    user = driver.find_element(By.NAME, 'email')
    user.send_keys(CONFIG.login_data['email'])
    sleep(0.5)

    pasw = driver.find_element(By.NAME, 'password')
    pasw.send_keys(CONFIG.login_data['senha'])
    sleep(0.5)

    btn_login = driver.find_element(By.CSS_SELECTOR, ".button-lg")
    btn_login.click()
    sleep(8)
  except:
    pass

#Após login realizado - a segunda tela ira selecionar o servidor // último server conectado
def tela_servidor(driver):
  try:
    btn_server = driver.find_element(By.CSS_SELECTOR, ".button-default")
    btn_server.click()
    sleep(3)
    
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
    print('login realizado com sucesso!')
    return True
  except:
    print('login falhou!')
    return False