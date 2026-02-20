import requests
def check_my_portfolio(api_key):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    # Definiamo cosa possediamo e a che prezzo
    my_wallet = {
        'BTC': {'amount': 0.5, 'buy_price': 30000},
        'ETH': {'amount': 2.0, 'buy_price': 1500}
    }
    parameters = {
        'symbol': 'BTC,ETH',
        'convert': 'EUR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    total_spent = 0
    total_now = 0
    for symbol, info in my_wallet.items():
        current_price = data['data'][symbol]['quote']['EUR']['price']
        initial_value = info['amount'] * info['buy_price']
        current_value = info['amount'] * current_price
        total_spent += initial_value
        total_now += current_value
        status = "PROFITTO" if current_value > initial_value else "PERDITA"
        print(f"--- {symbol} ---")
        print(f"Valore Iniziale: {round(initial_value, 2)} €")
        print(f"Valore Attuale: {round(current_value, 2)} € ({status})")
    print(f"\nRISULTATO FINALE:")
    # Formattazione richiesta: Valore Iniziale + Profitto/Perdita = Valore Totale
    profit_loss = total_now - total_spent
    print(f"**{round(total_spent, 2)} + {round(profit_loss, 2)} = {round(total_now, 2)}**")
# Usa la tua API Key qui
api_key = '17fa5bcd048b4d21a4f96681a1b6a572'
check_my_portfolio(api_key)