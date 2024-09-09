from selenium.webdriver.common.by import By
from configs import driver
import time


def fazer_login(cpf: str, data_nascimento: str) -> None:
    
    driver.get('https://infinityschool.app')

    botao_area_aluno = driver.find_element(By.XPATH, '//*[@id="geral_home"]/a[1]/button')
    botao_area_aluno.click()

    campo_cpf = driver.find_element(By.XPATH, '//*[@id="geral_home"]/form/input[1]')
    campo_nascimento = driver.find_element(By.XPATH, '//*[@id="data_nascimento"]')

    campo_cpf.send_keys(cpf)
    campo_nascimento.send_keys(data_nascimento)

    botao_entrar = driver.find_element(By.XPATH, '//*[@id="geral_home"]/form/button')
    botao_entrar.click()


def perguntar_acao():
    
    print("""
        AÇÕES:

        1. MARCAR PRESENÇA
        2. VERIFICAR SUPER MÓDULOS
        3. MARCAR AULAS COMPARTILHADAS

    """)

    acao = input("Insira o número da ação que deseja realizar: ")
    return int(acao)


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