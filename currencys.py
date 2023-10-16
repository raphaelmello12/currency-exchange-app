import requests

def get_currency_list():
    api_url = "https://economia.awesomeapi.com.br/json/available"  # Replace with the actual API URL
    response = requests.get(api_url)

    if response.status_code == 200:
        currency_list = response.json()
        return currency_list
    else:
        return []

if __name__ == "__main__":
    available_currencies = get_currency_list()
    print(available_currencies)
