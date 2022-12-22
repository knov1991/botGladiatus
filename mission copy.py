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
      print('func - finalizar')
      quests_ativas = driver.find_elements(By.CLASS_NAME, 'contentboard_slot_active')
      finalizar_quest(quests_ativas)
      
    if int(mission_count) < 5:
      quests_inativas = driver.find_elements(By.CLASS_NAME, 'contentboard_slot_inactive')
      iniciar_quest(driver, quests_inativas, mission_text, mission_text_not)
  except:
    pass

def finalizar_quest(quests_ativas):
    for i in range(len(quests_ativas)):
      try:
        finalizar = quests_ativas[i].find_elements(By.CLASS_NAME, 'quest_slot_button quest_slot_button_finish')[0]
        finalizar.click()
        print('Missão Concluída!')
        sleep(2)
      except:
        pass

def iniciar_quest(driver, quests_inativas, mission_text, mission_text_not):
  for n_quest in range(len(quests_inativas)):
    quest_titulo = quests_inativas[n_quest].find_elements(By.CLASS_NAME, 'quest_slot_title')[0].text
    
    #procurar texto valido
    for n_text_valido in range(len(mission_text)):
      if mission_text[n_text_valido] in quest_titulo:
        print('encontrado:', mission_text[n_text_valido])
        validar_text_not = 0
        for n_text_invalido in range(len(mission_text_not)):
          if mission_text_not[n_text_invalido] in quest_titulo:
            validar_text_not += 1
        if validar_text_not == 0:
          print('iniciar quest')
          iniciar = quests_inativas[n_quest].find_elements(By.CLASS_NAME, 'quest_slot_button_accept')[0]
          iniciar.click()
          sleep(1)
          VERIFICAR.resultado(driver, 'Missão Iniciada!')
          return

    
    """ if mission_text in quest_titulo:
      print('missão valida')
      if mission_text_not not in quest_titulo:
        print('missão iniciada por passar nos requisitos')
      else:
        print('missão não permitida')
    else:
      print('missão descartada')
    
      
      try:
        iniciar = quests_inativas[i].find_elements(By.CLASS_NAME, 'quest_slot_button quest_slot_button_accept')[0]
        iniciar.click()
        print('Missão Iniciada!')
        break
      except:
        pass """