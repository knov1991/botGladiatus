from time import sleep
from selenium.webdriver.common.by import By
#ajax
#mod=inventory&submod=move&from=513&fromX=2&fromY=2&to=8&toX=1&toY=1&amount=1&doll=1

VERIFICAR = __import__('verificar')
CONFIG = __import__('config')

def loop(driver, sh, hp_usar_food):
  try:
    driver.get(CONFIG.login_data['index_url']+'?mod=overview&sh='+str(sh))
    sleep(3)
    hp_atual = VERIFICAR.verificar_hp(driver)
    if hp_atual < hp_usar_food and hp_atual > 0:
      coord_food = procurar_food(driver)
      if len(coord_food) > 0:
        #usar food
        usar_food_url = driver.get(CONFIG.login_data['ajax_url']+'?mod=inventory&submod=move&from='+str(coord_food[0])+'&fromX='+str(coord_food[1])+'&fromY='+str(coord_food[2])+'&to=8&toX=1&toY=1&amount=1&doll=1&sh='+str(sh))
        VERIFICAR.resultado(driver, 'Usar Food!')
        driver.get(usar_food_url)
        sleep(3)
  except:
    pass

def procurar_food(driver):
  try:
    food_list = driver.find_elements(By.XPATH, "//div[@data-content-type='64']")
    if len(food_list) > 0:
      food_container = food_list[0].get_attribute('data-container-number')
      food_x = food_list[0].get_attribute('data-position-x')
      food_y = food_list[0].get_attribute('data-position-y')
      return food_container, food_x, food_y
  except:
    return []