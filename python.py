import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

dadosDaApi = requests.get(url)
response = dadosDaApi.json()

print(response["id"])
print(response["name"])
print(response["base_experience"])
print(response["order"])


