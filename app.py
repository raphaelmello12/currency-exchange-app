from flask import Flask, render_template, request, url_for
import requests



app = Flask(__name__)

# List of currencies you provided
currencies = ['Chose a currency','USD', 'BRL', 'CAD', 'EUR', 'GBP', 'ARS', 'BTC', 'LTC', 'JPY', 'CHF', 'AUD', 'CNY', 'ILS', 'ETH', 'XRP']

@app.route('/')
def index():
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = request.form['amount']

    # Get the exchange rate from the API
    url = f'http://economia.awesomeapi.com.br/json/{from_currency}-{to_currency}/1'
    response = requests.get(url)

    # Check if the API request was successful
    if response.status_code != 200:
        return render_template('index.html', currencies=currencies, error_message='Failed to fetch exchange rate. Please try again later.')

    data = response.json()

    # Check if the API response contains rate information
    if 'bid' in data[0]:
        rate = data[0]['bid']

        # Perform the currency conversion
        try:
            result = float(amount) * float(rate)
            return render_template('index.html', currencies=currencies, result=f'Result: {amount} {from_currency} is equivalent to {result:.2f} {to_currency}')
        except ValueError:
            return render_template('index.html', currencies=currencies, error_message='Invalid amount. Please enter a valid number.')

    return render_template('index.html', currencies=currencies, error_message='Invalid currency pair. Please select a valid pair.')

if __name__ == '__main__':
    app.run()
