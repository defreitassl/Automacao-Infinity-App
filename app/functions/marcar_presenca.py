from selenium.webdriver.common.by import By
from app import driver
import time


def perguntar_tipo_aula():
    tipos_de_aulas = {
        'SUPERMODULO': '//*[@id="geral_home"]/form[4]/button',
        'COMPARTILHADA': '//*[@id="geral_home"]/form[2]/button',
        'REPOSICAO': '//*[@id="geral_home"]/form[3]/button',
        'OFICIAL': '//*[@id="geral_home"]/form[1]/button',
        'ESTUDIO':'//*[@id="geral_home"]/form[5]/button'
    }
    print("""
        MARCAR PRESENÇA:
          
          . SUPERMODULO
          . COMPARTILHADA
          . REPOSICAO
          . OFICIAL
          . ESTUDIO

    """)
    aula_escolhida = input("Digite o nome do tipo da aula de acordo com o menu acima: ")
    return tipos_de_aulas[aula_escolhida.upper()]


def marcar_presenca(token: str, aula_XPATH: str):
    
    botao_marcar_presenca = driver.find_element(By.XPATH, '//*[@id="geral_home"]/div[2]/form[1]/button')
    botao_marcar_presenca.click()

    botao_aula = driver.find_element(By.XPATH, aula_XPATH)
    botao_aula.click()

    input_codigo = driver.find_element(By.XPATH, '//*[@id="token"]')
    input_codigo.send_keys(token)

    botao_concluir_presenca = driver.find_element(By.XPATH, '//*[@id="submit-button"]')
    botao_concluir_presenca.click()

    time.sleep(5)
