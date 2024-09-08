from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from credenciais import CPF, NASCIMENTO, CODIGO_PRESENCA


driver_path = os.path.join(os.getcwd(), 'chromedriver-linux64', 'chromedriver')

service = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=service)

driver.get('https://infinityschool.app')
botao_area_aluno = driver.find_element(By.XPATH, '//*[@id="geral_home"]/a[1]/button')
botao_area_aluno.click()

campo_cpf = driver.find_element(By.XPATH, '//*[@id="geral_home"]/form/input[1]')
campo_nascimento = driver.find_element(By.XPATH, '//*[@id="data_nascimento"]')

campo_cpf.send_keys(CPF)
campo_nascimento.send_keys(NASCIMENTO)

botao_entrar = driver.find_element(By.XPATH, '//*[@id="geral_home"]/form/button')
botao_entrar.click()

botao_marcar_presenca = driver.find_element(By.XPATH, '//*[@id="geral_home"]/div[2]/form[1]/button')
botao_marcar_presenca.click()

botao_aula_super_modulo = driver.find_element(By.XPATH, '//*[@id="geral_home"]/form[4]/button')
botao_aula_super_modulo.click()

input_codigo = driver.find_element(By.XPATH, '//*[@id="token"]')
input_codigo.send_keys(CODIGO_PRESENCA)

botao_concluir_presenca = driver.find_element(By.XPATH, '//*[@id="submit-button"]')
botao_concluir_presenca.click()

time.sleep(5)