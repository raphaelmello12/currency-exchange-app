# import requests
# from datetime import datetime

# # requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

# url = input("Qual Par de moedas?")
# requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{url}")

# requisicao_dic = requisicao.json()
# # cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
# # cotacao_euro = requisicao_dic["EURBRL"]["bid"]
# # cotacao_btc = requisicao_dic["CHFBRL"]["bid"]

# # print(f"Cotação atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")
# print(f"Cotação atualizada. {datetime.now()}\nR$:{requisicao}")


import requests
from datetime import datetime

# Define the currency pair you want to check
currency_pair = "USD-BRL"  # You can change this to any other valid currency pair

# Define the format (e.g., json)
format = "json"

# Construct the API endpoint URL
url = f"https://economia.awesomeapi.com.br/{format}/{currency_pair}"

# Make a request to the specific API endpoint for the currency pair
requisicao = requests.get(url)

# Check if the request was successful
if requisicao.status_code == 200:
    requisicao_data = requisicao.json()
    if "bid" in requisicao_data:
        cotacao = requisicao_data["bid"]
        print(f"Cotação atualizada. {datetime.now()}\n{currency_pair}: R${cotacao}")
    else:
        print(f"Error: Could not find bid data for {currency_pair}.")
else:
    print(f"Error: Failed to retrieve data from the API. Status code: {requisicao.status_code}")
