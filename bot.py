import requests

# I tuoi dati Telegram aggiornati e definitivi
TOKEN = "8670105719:AAGv3CnQRX7Zg2vQN4dB0PILCQpOvhe-1Ic"
CHAT_ID = "8496958478"
URL_SITO = "https://shop.weeztix.com/6c90b596-eac7-4f34-b20e-eb43350a7c40/tickets"

def controlla_biglietti():
    try:
        # 1. Scarica la pagina del sito
        risposta = requests.get(URL_SITO, timeout=15)
        testo_sito = risposta.text.lower()
        
        # 2. Controlla se i biglietti sono tornati disponibili
        if "sold out" not in testo_sito:
            messaggio_allarme = "🚨 BIGLIETTI DISPONIBILI! Corri su Weeztix: " + URL_SITO
            url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={messaggio_allarme}"
            requests.get(url_telegram)
            print("Biglietti trovati! Messaggio di allarme inviato.")
        else:
            # Ti avvisa comunque ogni 30 minuti sullo stato del bot
            messaggio_stato = "🤖 Bot Attivo: controllo effettuato. Ancora tutto esaurito."
            url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={messaggio_stato}"
            requests.get(url_telegram)
            print("Ancora sold out. Messaggio di stato inviato.")
            
    except Exception as e:
        print(f"Errore durante il controllo: {e}")

if __name__ == "__main__":
    controlla_biglietti()
