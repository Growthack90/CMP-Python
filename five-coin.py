import requests
import json
def get_crypto_prices(api_key):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5',
        'convert': 'EUR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = json.loads(response.text)
        for crypto in data['data']:
            name = crypto['name']
            price = crypto['quote']['EUR']['price']
            print(f"{name}: {round(price, 2)} €")
    except Exception as e:
        print(f"Errore: {e}")
# Sostituisci 'LA_TUA_API_KEY' con il codice ottenuto dal portale
api_key = 'LA_TUA_API_KEY'
get_crypto_prices(api_key)
