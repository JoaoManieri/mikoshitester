import requests

# URL da requisição
url = 'http://localhost:8080/auth'

# Dados para enviar no corpo da requisição (substitua pelos seus dados reais)
data = {
    'apiId': 'authvalidate-321',
}

# Realiza a requisição POST
response = requests.post(url, data=data)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    print('Token obtido com sucesso:')
    print(response.json())
else:
    print('Erro ao obter token:')
    print(response.text)
