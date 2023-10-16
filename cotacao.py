# import requests
# from datetime import datetime

# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

# requisicao_dic = requisicao.json()
# cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
# cotacao_euro = requisicao_dic["EURBRL"]["bid"]
# cotacao_btc = requisicao_dic["CHFBRL"]["bid"]

# print(f"Cotação atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")

import requests
from datetime import datetime

# Define the available currency pairs
currency_pairs = ["USD-BRL", "EUR-BRL", "BTC-BRL"]

# Ask the user to choose a currency pair
print("Choose a currency pair:")
for index, pair in enumerate(currency_pairs, 1):
    print(f"{index}. {pair}")

while True:
    try:
        user_choice = int(input("Enter the number of the currency pair you want to check: "))
        if 1 <= user_choice <= len(currency_pairs):
            selected_pair = currency_pairs[user_choice - 1]
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Make a request to the API for the selected currency pair
url = f"https://economia.awesomeapi.com.br/last/{selected_pair}"
requisicao = requests.get(url)
requisicao_dic = requisicao.json()

# Check if the selected_pair is in the response
if selected_pair in requisicao_dic:
    cotacao = requisicao_dic[selected_pair]["bid"]
    print(f"Cotação atualizada. {datetime.now()}\n{selected_pair}: R${cotacao}")
else:
    print(f"Error: Could not find data for {selected_pair}. Please check the currency pair.")
