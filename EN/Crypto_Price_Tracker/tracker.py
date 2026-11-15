import csv  # Import the built-in csv module to handle writing data rows into comma-separated value files (Zaimportuj wbudowany moduł csv do obsługi zapisywania wierszy danych do plików wartości rozdzielanych przecinkami)
from datetime import datetime  # Import the datetime class to capture current dates and times (Zaimportuj klasę datetime do rejestrowania aktualnych dat i godzin)
import time  # Import the time module so we can pause execution between loop runs using sleep (Zaimportuj moduł time, abyśmy mogli wstrzymywać wykonywanie programu pomiędzy kolejnymi obiegami pętli za pomocą funkcji sleep)
import requests  # Import the requests library to make HTTP network calls to Binance (Zaimportuj bibliotekę requests do wykonywania sieciowych żądań HTTP do Binance)

def fetch_crypto_price(symbol):  # Define a function named fetch_crypto_price that accepts a string symbol argument like 'BTCUSDT' (Zdefiniuj funkcję o nazwie fetch_crypto_price, która przyjmuje argument w postaci ciągu znaków symbolu, np. 'BTCUSDT')
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"  # Construct the target API URL string by inserting the symbol parameter (Skonstruuj ciąg docelowego adresu URL API, wstawiając parametr symbolu)
    
    try:  # Start a try block to handle any network or internet errors safely (Rozpocznij blok try, aby bezpiecznie obsłużyć wszelkie błędy sieciowe lub internetowe)
        response = requests.get(url)  # Send an HTTP GET request to Binance server and store the response object (Wyślij żądanie HTTP GET do serwera Binance i zapisz obiekt odpowiedzi)
        response.raise_for_status()  # Check if the HTTP status code is 200 OK; raise an exception if it is an error code (Sprawdź, czy kod statusu HTTP to 200 OK; wyrzuć wyjątek, jeśli jest to kod błędu)
        
        data = response.json()  # Parse the raw JSON response text from the server into a Python dictionary object (Przeanalizuj surowy tekst odpowiedzi JSON z serwera na obiekt słownika Pythona)
        price = float(data['price'])  # Extract the price value string from the dictionary and convert it to a decimal float number (Wyciągnij ciąg wartości ceny ze słownika i skonwertuj go na liczbę zmiennoprzecinkową typu float)
        
        return price  # Return the numerical price value out of the function (Zwróć numeryczną wartość ceny z funkcji)
        
    except requests.exceptions.RequestException as e:  # Catch any network exception or request failure and store error in variable e (Złap dowolny wyjątek sieciowy lub błąd żądania i zapisz błąd w zmiennej e)
        print(f"Error fetching data for {symbol}: {e}")  # Print a descriptive error message to the console screen (Wypisz opisowy komunikat o błędzie na ekranie konsoli)
        return None  # Return None since the fetching operation failed completely (Zwróć None, ponieważ operacja pobierania całkowicie się nie powiodła)

def save_to_csv(filename, data_row):  # Define a function to append a new row of data into a target CSV file (Zdefiniuj funkcję do dopisywania nowego wiersza danych do docelowego pliku CSV)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:  # Open the target file in append mode ('a') safely using a context manager with UTF-8 encoding (Otwórz docelowy plik w trybie dopisywania ('a') bezpiecznie za pomocą menedżera kontekstu z kodowaniem UTF-8)
        writer = csv.writer(file)  # Create a CSV writer helper object to format rows correctly (Utwórz obiekt pomocniczy zapisujący CSV do poprawnego formatowania wierszy)
        writer.writerow(data_row)  # Write the list of data values as a brand new row at the end of the file (Zapisz listę wartości danych jako zupełnie nowy wiersz na końcu pliku)

if __name__ == "__main__":  # Check if this script is being executed directly as the main program (Sprawdź, czy ten skrypt jest wykonywany bezpośrednio jako program główny)
    csv_filename = "crypto_prices.csv"  # Define the string variable holding our CSV file name (Zdefiniuj zmienną ciągową przechowującą nazwę naszego pliku CSV)
    print("Starting continuous crypto price tracker... Press Ctrl+C to stop.")  # Print a starting notification message to the console (Wypisz początkowy komunikat powiadomienia na konsoli)
    
    try:  # Start a try block to catch KeyboardInterrupt when user stops the script with Ctrl+C (Rozpocznij blok try, aby złapać KeyboardInterrupt, gdy użytkownik zatrzyma skrypt za pomocą skrótu Ctrl+C)
        while True:  # Start an infinite loop so the code repeats continuously forever (Rozpocznij nieskończoną pętlę, aby kod powtarzał się w nieskończoność)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Capture the current timestamp formatted nicely as a readable string (Zarejestruj bieżący znacznik czasu sformatowany ładnie jako czytelny ciąg znaków)
            
            btc_price = fetch_crypto_price("BTCUSDT")  # Call function to fetch the live Bitcoin price from Binance (Wywołaj funkcję, aby pobrać cenę Bitcoina na żywo z Binance)
            eth_price = fetch_crypto_price("ETHUSDT")  # Call function to fetch the live Ethereum price from Binance (Wywołaj funkcję, aby pobrać cenę Ethereum na żywo z Binance)
            
            if btc_price is not None:  # Check if the Bitcoin price was successfully returned (Sprawdź, czy cena Bitcoina została pomyślnie zwrócona)
                btc_row = [timestamp, "BTCUSDT", btc_price]  # Create a list representing the CSV row for Bitcoin (Utwórz listę reprezentującą wiersz CSV dla Bitcoina)
                save_to_csv(csv_filename, btc_row)  # Call helper function to append Bitcoin data into the CSV file (Wywołaj funkcję pomocniczą, aby dopisać dane Bitcoina do pliku CSV)
                print(f"Saved: {btc_row}")  # Print confirmation message to the console screen (Wypisz komunikat potwierdzenia na ekranie konsoli)
                
            if eth_price is not None:  # Check if the Ethereum price was successfully returned (Sprawdź, czy cena Ethereum została pomyślnie zwrócona)
                eth_row = [timestamp, "ETHUSDT", eth_price]  # Create a list representing the CSV row for Ethereum (Utwórz listę reprezentującą wiersz CSV dla Ethereum)
                save_to_csv(csv_filename, eth_row)  # Call helper function to append Ethereum data into the CSV file (Wywołaj funkcję pomocniczą, aby dopisać dane Ethereum do pliku CSV)
                print(f"Saved: {eth_row}")  # Print confirmation message to the console screen (Wypisz komunikat potwierdzenia na ekranie konsoli)
                
            print("Waiting 10 seconds before next fetch...\n")  # Print a status message indicating a pause period (Wypisz komunikat o statusie wskazujący okres pauzy)
            time.sleep(10)  # Pause script execution for 10 seconds before looping again (Wstrzymaj wykonywanie skryptu na 10 sekund przed ponownym rozpoczęciem pętli)
            
    except KeyboardInterrupt:  # Catch the exception triggered when the user presses Ctrl+C in the terminal (Złap wyjątek wywołany, gdy użytkownik naciśnie Ctrl+C w terminalu)
        print("\nTracker stopped gracefully by user. Good job!")  # Print a friendly goodbye message when exiting (Wypisz przyjazny komunikat pożegnalny przy wychodzeniu z programu)