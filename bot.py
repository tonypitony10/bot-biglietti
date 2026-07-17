import requests

TOKEN = "8949964974:AAGIJUUMBrIZixnCd3aTAZX0nCCJM6a2U0Q"
CHAT_ID = "7794109019"
URL_SITO = "https://shop.weeztix.com/6c90b596-eac7-4f34-b20e-eb43350a7c40/tickets"

def controlla_biglietti():
    try:
        risposta = requests.get(URL_SITO, timeout=15)
        testo_sito = risposta.text.lower()
        
        if "sold out" not in testo_sito:
            messaggio_allarme = "🚨 BIGLIETTI DISPONIBILI! Corri su Weeztix: " + URL_SITO
            url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={messaggio_allarme}"
            requests.get(url_telegram)
            print("Biglietti trovati! Messaggio di allarme inviato.")
        else:
            messaggio_stato = "🤖 Bot Attivo: controllo effettuato. Ancora tutto esaurito."
            url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={messaggio_stato}"
            requests.get(url_telegram)
            print("Ancora sold out. Messaggio di stato inviato.")
            
    except Exception as e:
        print(f"Errore durante il controllo: {e}")

if __name__ == "__main__":
    controlla_biglietti()
