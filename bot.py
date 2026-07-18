import requests

# I tuoi dati Telegram immutati
TOKEN = "8670105719:AAGv3CnQRX7Zg2vQN4dB0PILCQpOvhe-1Ic"
CHAT_ID = "8496958478"

# URL dell'API interna di Weeztix per questo specifico evento
URL_API = "https://shop.weeztix.com/api/v1/events/6c90b596-eac7-4f34-b20e-eb43350a7c40/tickets"
URL_NEGOZIO = "https://shop.weeztix.com/6c90b596-eac7-4f34-b20e-eb43350a7c40/tickets"

def controlla_biglietti():
    try:
        # Faccia finta di essere un browser normale per evitare blocchi
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        # Interroga l'API del sito
        risposta = requests.get(URL_API, headers=headers, timeout=15)
        
        # Se il sito risponde correttamente
        if risposta.status_code == 200:
            dati = risposta.json()
            
            # Analizza la lista dei biglietti
            biglietti_disponibili = False
            
            # Controlla ogni categoria di biglietto presente nel sistema
            for categoria in dati.get("tickets", []):
                # Controlla se lo stato non è 'sold_out' o se c'è quantità disponibile
                status = categoria.get("status", "").lower()
                quantity = categoria.get("available_quantity", 0)
                
                if "sold" not in status and "esaurito" not in status:
                    biglietti_disponibili = True
                    break
            
            if biglietti_disponibili:
                # Invia l'allarme solo se ha trovato qualcosa di realmente acquistabile
                messaggio = f"🚨 BIGLIETTI DISPONIBILI! Corri a comprare: {URL_NEGOZIO}"
                url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={messaggio}"
                requests.get(url_tg)
                print("Biglietti rilevati! Allarme inviato.")
            else:
                print("Confermato: Tutto ancora sold out. Nessuna notifica inviata.")
        else:
            print(f"Il sito ha risposto con errore codice: {risposta.status_code}")
            
    except Exception as e:
        print(f"Errore tecnico durante la lettura dei dati: {e}")

if __name__ == "__main__":
    controlla_biglietti()
