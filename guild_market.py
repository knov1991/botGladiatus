from time import sleep

from selenium.webdriver.common.by import By

VERIFICAR = __import__('verificar')
CONFIG = __import__('config')
LINKS = __import__('links')

def loop(driver, sh):
  LINKS.link_guild_market(driver, sh)
  gold = VERIFICAR.verificar_gold(driver)
  if gold > 5000:
    vender_item(driver, sh)
  if gold > 100000:
    comprar_item(driver, sh)
  pacotes_pegar_item(driver, sh)


def comprar_item(driver, sh):
  try:
    #buyid=494228&qry=&seller=&f=0&fl=0&fq=-1&s=&p=1&buy=Comprar
    market_table = driver.find_element(By.ID, 'market_table')
    tr = market_table.find_elements(By.XPATH, '//tr')
    for i in range(len(tr)):
      market_items = tr[i].find_elements(By.CLASS_NAME, 'item-i-white')
      if len(market_items) > 0:
        nome = tr[i].find_element(By.CSS_SELECTOR, 'span').text
        almas = ['Alma de: Dyroths', 'Alma de: Freedom']
        vinculo_alma = market_items[0].get_attribute('data-tooltip')
        if 'Trisquel' in vinculo_alma and (almas[0] in vinculo_alma or almas[1] in vinculo_alma) and nome != CONFIG.login_data['account_name']:
          item_id = market_items[0].get_attribute('data-item-id')
          VERIFICAR.resultado(driver, 'Guild-Market : item para gold pack encontrado, item_id:', item_id)
          buy_url = CONFIG.login_data['index_url']+'?mod=guildMarket&sh='+str(sh)+''+'&buyid='+str(item_id)+'&buy=Comprar'     
          VERIFICAR.resultado(driver, 'Comprar Item - Guild Market!')
          driver.get(buy_url)
          sleep(5)
          return
  except:
    pass

def vender_item(driver, sh):
  valor = 100000
  try:
    #dauer = tempo de venda // 1=2h // 2=8h // 3=24h
    #&sellid=9283349&preis=100000&dauer=2&sell_mode=0&anbieten=Oferta
    #item_type = item[0].get_attribute('data-content-type')
    inventory = driver.find_element(By.ID, 'inv')
    item = inventory.find_elements(By.CLASS_NAME, 'item-i-white')
    if len(item) > 0:
      item_id = item[0].get_attribute('data-item-id')
      item_info = item[0].get_attribute('data-tooltip')
      if 'Trisquel' in item_info:
        sell_url = CONFIG.login_data['index_url']+'?mod=guildMarket&sh='+str(sh)+''+'&sellid='+str(item_id)+'&preis='+str(valor)+'&dauer=2&sell_mode=0&anbieten=Oferta'
        VERIFICAR.resultado(driver, 'Vender Item - Guild Market!')
        driver.get(sell_url)
        sleep(3)
        return
  except:
    pass


#https://s301-en.gladiatus.gameforge.com/game/ajax.php?mod=inventory&submod=move&from=-12100048&fromX=1&fromY=1&to=513&toX=1&toY=1&amount=1
#mod=inventory&submod=move&from=-12100048&fromX=1&fromY=1&to=513&toX=1&toY=1&amount=1
def pacotes_pegar_item(driver, sh):
  driver.get('https://s301-en.gladiatus.gameforge.com/game/index.php?mod=packages&f=0&fq=-1&qry=trisquel&page=1&sh=94e1eae61b2c542175f216da74e853ef')
  sleep(3)
  try:
    pacotes = driver.find_element(By.ID, 'packages')
    item = pacotes.find_elements(By.XPATH, "//div[@data-gca-soulbound='true']")[0]
    item_location = item.get_attribute('data-container-number')
    #desc_item = item.find_element(By.CSS_SELECTOR, "data-content-type='48'")
    #item_amount = desc_item.get_attribute('data-amount')
    if item_location:
      url_pegar_item = CONFIG.login_data['ajax_url']+'?mod=inventory&submod=move&from='+str(item_location)+'&fromX=1&fromY=1&to=513&toX=1&toY=1&amount=1&sh='+str(sh)
      VERIFICAR.resultado(driver, 'Pegar Item - Guild Gold Pack!')
      driver.get(url_pegar_item)
      sleep(3)
  except:
    pass