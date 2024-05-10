import jwt
import requests
from getKey import getKey

# URL da requisição
url = 'http://localhost:8080/register'

# Dados para enviar no corpo da requisição (substitua pelos seus dados reais)

token = jwt.encode({"pass": "tecnopass"}, getKey(), algorithm="RS256")

data = {
    "email": "jvmanieri@tecnomotor.com.br",
    "nome": "João Victor Ponce Manieri",
    "serialNumber": "129030",
    "token": token
}

# Realiza a requisição POST
response = requests.post(url, json=data)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
