from dotenv import load_dotenv
import os
from app.functions.marcar_presenca import marcar_presenca, perguntar_tipo_aula
from app.functions.login_functions import fazer_login, perguntar_acao
from app.functions.agendar_aulas import achar_aulas

load_dotenv()

cpf = os.environ.get("CPF")
nascimento = os.environ.get("DATA_NASCIMENTO")

fazer_login(cpf=cpf, data_nascimento=nascimento)

acao = perguntar_acao()

match acao:
    case 1:
        TOKEN = input("Insira o token do dia de hoje: ")
        tipo_aula = perguntar_tipo_aula()
        marcar_presenca(token=TOKEN, aula_XPATH=tipo_aula)
    
    case 2:
        achar_aulas()
    
    case _:
        print("Ação inválida selecionada...")
