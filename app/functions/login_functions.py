from .. import driver
from selenium.webdriver.common.by import By


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
        2. MARCAR AULAS COMPARTILHADAS

    """)

    acao = input("Insira o número da ação que deseja realizar: ")
    return int(acao)