import requests

# URL da requisição
url = 'http://localhost:8080/validation'

# Dados para enviar no corpo da requisição (substitua pelos seus dados reais)
data = {
    "email": "jvmanieri@tecnomotor.com.br",
    "nome": "João Victor Ponce Manieri",
    "serialNumber": "129030",
    "senha": "va5uu8eSM8",
}

# Realiza a requisição POST
response = requests.post(url, json=data)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
