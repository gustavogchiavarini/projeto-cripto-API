import requests
import json

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd"

response = requests.get(url) 

if response.status_code == 200:
    dados=response.json()

    taxa_cambio = 5.10

    precos_brl = {
        "bitcoin":dados["bitcoin"]["usd"]* taxa_cambio,
        "ethereum": dados["ethereum"]["usd"] * taxa_cambio,
        "litecoin" : dados["litecoin"]["usd"] * taxa_cambio
        }
    
    with open("cripto_precos.json", "w") as arquivo:
        json.dump(precos_brl,arquivo,indent=4)

    print("Arquivo cripto_precos.json salvo com sucesso.")
else:
    print(f"Erro ao acessar API: {response.status_code}")