import requests
import json
from datetime import datetime

def atualizar_precos():
    print("Iniciando a atualização de preços...")  # Mensagem de depuração
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Conexão com a API bem-sucedida.")  # Mensagem de depuração

        dados = response.json()

        taxa_cambio = 5.10

        precos_brl = {
            "bitcoin": dados["bitcoin"]["usd"] * taxa_cambio,
            "ethereum": dados["ethereum"]["usd"] * taxa_cambio,
            "litecoin": dados["litecoin"]["usd"] * taxa_cambio,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Data e hora da consulta
        }

        print(f"Dados processados: {precos_brl}")  # Mensagem de depuração

        import os
        os.makedirs("data", exist_ok=True)

        with open("data/cripto_precos.json", "w") as arquivo:
            json.dump(precos_brl, arquivo, indent=4)

        print("Arquivo cripto_precos.json salvo com sucesso.")  # Mensagem de sucesso
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    except KeyError as e:
        print(f"Dado esperado não encontrado na resposta da API: {e}")

if __name__ == "__main__":
    atualizar_precos()