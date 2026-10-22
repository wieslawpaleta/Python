import requests
from database import save_asteroids_to_db
# Importing the database function (Importowanie funkcji bazy danych)

# Defining NASA API URL for Near Earth Objects (Definiowanie adresu IRL API NASA dla obiektów bliskich Ziemi)
# Using DEMO_KEY for testing (Używanie DEMO_KEY do testów)
url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2026-06-01&end_date=2026-06-07&api_key=DEMO_KEY"

# Function to fetch asteroid data from NASA API (Funkcja do pobierania danych o asteroidach z API NASA)
def fetch_neo_data(api_url):
    # Sending GET request to the NASA API (Wysyłanie żądania GET do API NASA)
    response = requests.get(api_url)

    # Checking if the request was successful (Sprawdzanie, czy żądanie zakończyło się sukcesem)
    if response.status_code == 200:
        print("Data fetched successfully! (Dane pobrane pomyślnie!)")
        return response.json()
    else:
        print(f"Error: {response.status_code} (Błąd: {response.status_code})")
        return None

# Testing the function (Testowanie funkcji)
if __name__ == "__main__":
    data = fetch_neo_data(url)
    if data:
        # Printing total elements found (Wypisywanie całkowitej liczby znalezionych elementów)
        print(f"Total elements: {data.get('element_count')} (Całkowita liczba elementów)")

        # Saving the fetched data to SQLite database (Zapisywanie pobranych danych do bazy danych SQLite)
        save_asteroids_to_db(data)