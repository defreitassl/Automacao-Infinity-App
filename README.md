# Automacao Infinity App

Uma automação básica feita no Infinity App especialmente para os alunos da Infinity School, para facilitar a marcação de presenças e agendamento de aulas extras. Desenvolvido 
totalmente por mim e feita para aprimorar meus conhecimentos lógicos e técnicos sobre automações web.

---

### Tecnologias utilizadas

 - __Selenium__: Um Framework python específico para automações web e webscrapping. Foi o componente principal da aplicação.

---

### Como utilizar

1. Clone ou instale os arquivos do repositório na sua máquina
2. Crie e ative seu Ambiente Virtual (venv):
   
   ```python
   python -m venv venv

   # Linux:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   ```
3. Instale as dependências necessárias:

   ```python
   pip install selenium
   ```
   ```python
   pip install webdriver-manager
   ```
4. Crie um arquivo .env (dotenv) e crie as variáveis de ambiente que serão utilizadas para fazer o login:

   ! As variáveis devem estar exatamente no seguinte formato...
   ```python
   CPF = "12345678911"
   DATA_NASCIMENTO = "10102005"
   ```
---

## Pronto

Agora você já deve estar com o sistema totalmente funcional na sua máquina! Sinta-se a vontade para comentar possíveis erros e fazer pull requests. 

Obrigado!
