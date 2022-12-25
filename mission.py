from time import sleep

from selenium.webdriver.common.by import By

LINKS = __import__('links')
VERIFICAR = __import__('verificar')
NOTIFICATION = __import__('notification')

def loop(driver, sh, mission_text, mission_text_not):
  try:
    NOTIFICATION.loop(driver)
    LINKS.link_tela_mission(driver, sh)
    mission_count = driver.find_element(By.ID, 'quest_header_accepted').text[-5]
    if int(mission_count) > 0:
      quests_ativas = driver.find_elements(By.CLASS_NAME, 'contentboard_slot_active')
      link_terminar_quest = finalizar_quest(driver, quests_ativas)
      if link_terminar_quest != False:
        print('terminando quest:', link_terminar_quest)
        driver.get(link_terminar_quest)
        sleep(2)
      
    if int(mission_count) < 5:
      quests_inativas = driver.find_elements(By.CLASS_NAME, 'contentboard_slot_inactive')
      link_ativar_quest = iniciar_quest(driver, quests_inativas, mission_text, mission_text_not)
      if link_ativar_quest != False:
        print('ativando quest:', link_ativar_quest)
        driver.get(link_ativar_quest)
        sleep(2)

    refresh_mission(driver, sh)
  except:
    pass

def finalizar_quest(driver, quests_ativas):
    for i in range(len(quests_ativas)):
      finalizar = quests_ativas[i].find_elements(By.CLASS_NAME, 'quest_slot_button_finish')
      if len(finalizar) > 0:
        link_finalizar_quest = finalizar[0].get_attribute("href")
        return link_finalizar_quest
    #se não encontrar nenhuma quest para finalizar, retorna falso
    return False

def iniciar_quest(driver, quests_inativas, mission_text, mission_text_not):
  try:
    verifica_cooldown = driver.find_element(By.ID, 'quest_header_cooldown')
    if verifica_cooldown:
      #print('esta em CD!')
      return False
  except:
    print('missão não esta em CD')
    for n_quest in range(len(quests_inativas)):
      quest_titulo = quests_inativas[n_quest].find_elements(By.CLASS_NAME, 'quest_slot_title')[0].text

      #procurar texto valido
      for n_text_valido in range(len(mission_text)):
        if mission_text[n_text_valido] in quest_titulo:
          #print('encontrado:', mission_text[n_text_valido])
          validar_text_not = 0
          for n_text_invalido in range(len(mission_text_not)):
            if mission_text_not[n_text_invalido] in quest_titulo:
              validar_text_not += 1
          if validar_text_not == 0:
            verifica_limite_tempo = quests_inativas[n_quest].find_elements(By.CLASS_NAME, 'quest_slot_time')
            if not verifica_limite_tempo:
              #print('iniciar quest', mission_text[n_text_valido])
              iniciar = quests_inativas[n_quest].find_elements(By.CLASS_NAME, 'quest_slot_button_accept')[0]
              link_iniciar_quest = iniciar.get_attribute("href")
              #VERIFICAR.resultado(driver, 'Missão Iniciada! -', mission_text[n_text_valido])
              #driver.get(link_iniciar_quest)
              #sleep(2)
              return link_iniciar_quest
    return False

def refresh_mission(driver, sh):  
  #print('function refresh')
  try:
    verifica_cooldown = driver.find_element(By.ID, 'quest_header_cooldown')
    if verifica_cooldown:
      return
  except:
    LINKS.link_refresh_treinamento(driver, sh)
    print('refresh missões')