import requests
import csv
from datetime import datetime
import os
def save_to_csv(total_spent, profit, total_now):
    file_name = 'andamento_portfolio.csv'
    # Verifichiamo se il file esiste già per scrivere l'intestazione solo la prima volta
    file_exists = os.path.isfile(file_name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Data', 'Investimento Iniziale', 'Profitto_Perdita', 'Valore Totale'])
        # Salviamo i dati
        writer.writerow([timestamp, total_spent, profit, total_now])
def monitor_and_save(api_key):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    my_wallet = {'BTC': {'amount': 0.1, 'buy_price': 30000}}
    headers = {'X-CMC_PRO_API_KEY': api_key}
    parameters = {'symbol': 'BTC', 'convert': 'EUR'}
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()
        current_price = data['data']['BTC']['quote']['EUR']['price']
        total_spent = my_wallet['BTC']['amount'] * my_wallet['BTC']['buy_price']
        current_now = my_wallet['BTC']['amount'] * current_price
        profit = current_now - total_spent
        # Salvataggio su file
        save_to_csv(total_spent, profit, current_now)
        # Formattazione richiesta: Valore Iniziale + Profitto = Totale
        print(f"Dati salvati: **{round(total_spent, 2)} + {round(profit, 2)} = {round(current_now, 2)}**")
    except Exception as e:
        print(f"Errore durante l'aggiornamento: {e}")
# Esecuzione
api_key = '17fa5bcd048b4d21a4f96681a1b6a572'
monitor_and_save(api_key)