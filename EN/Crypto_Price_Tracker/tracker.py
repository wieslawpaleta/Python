import requests  # Import the requests library so Python can make internet HTTP requests (Zaimportuj bibliotekę requests, aby Python mógł wysyłać żądania HTTP do internetu)

def fetch_crypto_price(symbol):  # Define a custom function named fetch_crypto_price that takes a text symbol parameter like 'BTCUSDT' (Zdefiniuj funkcję niestandardową o nazwie fetch_crypto_price, która przyjmuje tekstowy parametr symbol, np. 'BTCUSDT')
    url = f"tu adres api"  # Create the target web address string by inserting the variable symbol into the Binance API URL string (Stwórz ciąg znaków docelowego adresu internetowego, wstawiając zmienną symbol do adresu URL API Binance)
    
    try:  # Start a try block to safely catch runtime errors if the internet or API goes down (Rozpocznij blok try, aby bezpiecznie łapać błędy wykonania, jeśli internet lub API przestanie działać)
        response = requests.get(url)  # Send an HTTP GET request to the Binance server and save the entire server response object into a variable (Wyślij żądanie HTTP GET do serwera Binance i zapisz cały obiekt odpowiedzi serwera w zmiennej)
        response.raise_for_status()  # Check if the HTTP status code indicates success (200); if it is an error code like 404 or 500, automatically throw an exception (Sprawdź, czy kod statusu HTTP wskazuje sukces - 200; jeśli jest to kod błędu, np. 404 lub 500, automatycznie rzuć wyjątek)
        
        data = response.json()  # Convert the raw JSON text response from the server into a native Python dictionary object (Konwertuj surową odpowiedź tekstową JSON z serwera na wbudowany obiekt słownika Pythona)
        price = float(data['price'])  # Extract the value stored under the 'price' key from the dictionary and convert it from a text string into a decimal float number (Wyciągnij wartość zapisaną pod kluczem 'price' ze słownika i skonwertuj ją z tekstu na liczbę zmiennoprzecinkową typu float)
        
        return price  # Send the final numeric price back out of the function to wherever it was called (Zwróć ostateczną cenę numeryczną na zewnątrz funkcji tam, gdzie została wywołana)
        
    except requests.exceptions.RequestException as e:  # Catch any network errors or connection issues and store the error message inside variable e (Złap wszelkie błędy sieciowe lub problemy z połączeniem i zapisz komunikat o błędzie w zmiennej e)
        print(f"Error fetching data for {symbol}: {e}")  # Print a friendly error message to the console explaining which symbol failed and why (Wypisz przyjazny komunikat o błędzie na konsoli, wyjaśniający, który symbol zawiódł i dlaczego)
        return None  # Return the special value None because fetching failed completely (Zwróć specjalną wartość None, ponieważ pobieranie całkowicie się nie powiodło)

if __name__ == "__main__":  # Check if this Python script is being executed directly as the main program (Sprawdź, czy ten skrypt Pythona jest uruchamiany bezpośrednio jako program główny)
    print("Fetching live crypto prices from Binance...")  # Print a starting status message to the console screen (Wypisz początkowy komunikat o statusie na ekranie konsoli)
    
    btc_price = fetch_crypto_price("BTCUSDT")  # Call our function with 'BTCUSDT' to fetch Bitcoin's price and store the result in btc_price (Wywołaj naszą funkcję z argumentem 'BTCUSDT', aby pobrać cenę Bitcoina i zapisać wynik w btc_price)
    eth_price = fetch_crypto_price("ETHUSDT")  # Call our function with 'ETHUSDT' to fetch Ethereum's price and store the result in eth_price (Wywołaj naszą funkcję z argumentem 'ETHUSDT', aby pobrać cenę Ethereum i zapisać wynik w eth_price)
    
    if btc_price is not None:  # Check if the returned Bitcoin price is not None (meaning it was successfully retrieved) (Sprawdź, czy zwrócona cena Bitcoina nie jest wartością None - co oznacza, że została pomyślnie pobrana)
        print(f"Bitcoin Price: ${btc_price:,.2f}")  # Print the formatted Bitcoin price with a dollar symbol, thousands separator commas, and exactly two decimal places (Wypisz sformatowaną cenę Bitcoina z symbolem dolara, przecinkami oddzielającymi tysiące i dokładnie dwoma miejscami po przecinku)
        
    if eth_price is not None:  # Check if the returned Ethereum price is not None (meaning it was successfully retrieved) (Sprawdź, czy zwrócona cena Ethereum nie jest wartością None - co oznacza, że została pomyślnie pobrana)
        print(f"Ethereum Price: ${eth_price:,.2f}")  # Print the formatted Ethereum price with a dollar symbol, thousands separator commas, and exactly two decimal places (Wypisz sformatowaną cenę Ethereum z symbolem dolara, przecinkami oddzielającymi tysiące i dokładnie dwoma miejscami po przecinku)