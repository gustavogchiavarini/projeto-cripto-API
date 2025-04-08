import requests
import json

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd"

try:
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()

    taxa_cambio = 5.10

    precos_brl = {
        "bitcoin": dados["bitcoin"]["usd"] * taxa_cambio,
        "ethereum": dados["ethereum"]["usd"] * taxa_cambio,
        "litecoin": dados["litecoin"]["usd"] * taxa_cambio
    }

    with open("data/cripto_precos.json", "w") as arquivo:
        json.dump(precos_brl, arquivo, indent=4)

    print("Arquivo cripto_precos.json salvo com sucesso.")
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API: {e}")
except KeyError as e:
    print(f"Dado esperado não encontrado na resposta da API: {e}")
