from .. import driver
from selenium.webdriver.common.by import By


def achar_aulas():
    
    while True:
        driver.find_element(By.XPATH, '//*[@id="geral_home"]/div[2]/div[2]/details[1]').click()

        driver.find_element(By.XPATH, '//*[@id="geral_home"]/div[2]/div[2]/details[1]/div/form[2]/button').click()

        form_aulas_disponiveis = driver.find_element(By.XPATH, '//*[@id="geral_home"]/form[1]')
        print(form_aulas_disponiveis.get_attribute("action"))

        if form_aulas_disponiveis.get_attribute("action") == "https://infinityschool.app/resposta_workshop":
            aulas = form_aulas_disponiveis.find_elements(By.CLASS_NAME, "aulas_compartilhadas")

        else:
            form_aulas_disponiveis = driver.find_element(By.XPATH, '//*[@id="geral_home"]/form[2]')
            aulas = form_aulas_disponiveis.find_elements(By.CLASS_NAME, "aulas_compartilhadas")

        try:

            if len(aulas) > 0:
                print("OK")
                botao_inscrever = aulas[0].find_element(By.CLASS_NAME, "button2")
                botao_inscrever.click()

                driver.find_element(By.XPATH, '//*[@id="geral_home"]/form/button').click()
            
            else:
                print("Não existem mais aulas compartilhadas disponíveis.")
                break

        except Exception as e:
            print(f"Erro ao achar as aulas: {e}")
