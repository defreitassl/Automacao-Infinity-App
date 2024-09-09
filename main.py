from credenciais import CPF, DATA_NASCIMENTO
from functions import fazer_login, perguntar_acao, marcar_presenca, perguntar_tipo_aula

fazer_login(cpf=CPF, data_nascimento=DATA_NASCIMENTO)

acao = perguntar_acao()

match acao:
    case 1:
        TOKEN = input("Insira o token do dia de hoje: ")
        tipo_aula = perguntar_tipo_aula()
        marcar_presenca(token=TOKEN, aula_XPATH=tipo_aula)
    
    case 2:
        print("Nao está pronto ainda")
    
    case 3:
        print("Nao está pronto ainda")
    
    case _:
        print("Ação inválida selecionada...")
