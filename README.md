# Guida all'Installazione ed Esecuzione

Questa guida spiega come configurare l'ambiente Python ed eseguire lo script principale del progetto.

## Prerequisiti
- Python installato (versione 3.x raccomandata).

## 1. Creazione del Virtual Environment (venv)

Apri il terminale (PowerShell o CMD) nella cartella del progetto ed esegui:

```powershell
python -m venv .venv
```
Questo creerà una cartella `.venv` con l'ambiente virtuale.

## 2. Attivazione dell'Ambiente

Prima di eseguire lo script o installare pacchetti, devi attivare l'ambiente.

**Su Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```
*(Se ricevi un errore sui permessi, esegui prima: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

**Su Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

Quando attivato, vedrai `(.venv)` all'inizio della riga di comando.

## 3. Installazione delle Dipendenze

Se il progetto richiede librerie esterne (e hai un file `requirements.txt`), installale con:

```powershell
pip install -r requirements.txt
```

*(Se non hai dipendenze esterne, puoi saltare questo passaggio).*

Installa la dipendenza:
```powershell
pip install requests
```

## 4. Esecuzione dello Script

Con l'ambiente attivo, esegui l'applicazione con:

```powershell
python five-coin.py
```

## Disattivazione
Per uscire dall'ambiente virtuale una volta finito, scrivi semplicemente:
```powershell
deactivate
```

## NOTA IMPORTANTE

**Ottenere la Chiave API**\
- Per prima cosa, devi registrarti sul CoinMarketCap Developer Portal, [qui](https://pro.coinmarketcap.com/account). 
- Una volta loggato, troverai la tua API Key nella dashboard. Il piano gratuito ("Basic") ti permette di fare fino a 10.000 richieste al mese, il che è perfetto per test e piccoli progetti personali.
- Incollala nel codice