import json  # Import the built-in json module to read and write JSON data (Importuje wbudowany moduł json do czytania i zapisywania danych JSON)
import folium  # Import folium to build an interactive HTML map with markers and lines (Importuje folium do tworzenia interaktywnej mapy HTML z pinezkami i liniami)
import numpy as np  # Import NumPy as np for fast math on lists of numbers (Importuje NumPy jako np do szybkiej matematyki na listach liczb)
import requests  # Import requests to download data from web APIs over HTTP (Importuje requests do pobierania danych ze stron i API przez internet)
from scipy.spatial import cKDTree  # Import cKDTree from SciPy to fast-search nearest points in space (Importuje cKDTree z SciPy do szybkiego szukania najbliższych punktów w przestrzeni)

API_URL = "https://volcanoes.usgs.gov/vsc/api/volcanoApi/"  # Store the USGS volcano API address in a text variable (Zapisuje adres API wulkanów USGS w zmiennej tekstowej)
OUTPUT_MAP_FILE = "volcano_map.html"  # Define the filename where the generated map will be saved (Określa nazwę pliku, pod którą zapisze się wygenerowana mapa)
WORLD_GEOJSON_URL = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"  # Store a public world countries GeoJSON URL in a variable (Zapisuje adres publicznego pliku GeoJSON z granicami państw w zmiennej)

FALLBACK_VOLCANOES = [  # Create a backup list of volcanoes in case the internet or API fails (Tworzy zapasową listę wulkanów na wypadek braku internetu lub błędu API)
    {"name": "Kilauea", "lat": 19.4069, "lon": -155.2834, "alert_level": 3},  # Dictionary for Kilauea with name, latitude, longitude, and alert score (Słownik dla Kilauea z nazwą, szerokością, długością i poziomem alertu)
    {"name": "Mauna Loa", "lat": 19.4756, "lon": -155.6054, "alert_level": 2},  # Dictionary for Mauna Loa volcano data (Słownik z danymi wulkanu Mauna Loa)
    {"name": "Mount St. Helens", "lat": 46.1914, "lon": -122.1956, "alert_level": 2},  # Dictionary for Mount St. Helens data (Słownik z danymi wulkanu Mount St. Helens)
    {"name": "Mount Rainier", "lat": 46.8523, "lon": -121.7603, "alert_level": 2},  # Dictionary for Mount Rainier data (Słownik z danymi wulkanu Mount Rainier)
    {"name": "Redoubt", "lat": 60.4850, "lon": -152.7420, "alert_level": 1},  # Dictionary for Redoubt volcano data (Słownik z danymi wulkanu Redoubt)
]  # Close the backup list of volcanoes (Zamyka zapasową listę wulkanów)

--- tu
FALLBACK_WORLD_GEOJSON = {
    "type": "FeatureCollection",
    "features": [
        { }
    ]
}

def fetch_volcanoes(url: str) -> list[dict]:  # Define a function that fetches volcano data and returns a list of dictionaries (Definiuje funkcję pobierającą dane o wulkanach i zwracającą listę słowników)
    try:  # Start a safe block that catches network or parsing errors without crashing (Rozpoczyna bezpieczny blok, który łapie błędy sieci i nie wywala programu)
        response = requests.get(url, timeout=10)  # Send a GET request to the API and wait at most 10 seconds (Wysyła zapytanie GET do API i czeka maksymalnie 10 sekund)
        response.raise_for_status()  # Raise an error if the server replied with a bad status like 404 or 500 (Zgłasza błąd, jeśli serwer odpowiedział złym kodem np. 404 lub 500)
        raw_data = response.json()  # Convert the JSON text reply from the API into Python data (Zamienia odpowiedź JSON z API na struktury danych w Pythonie)
        parsed = []  # Create an empty list to store clean volcano records (Tworzy pustą listę na oczyszczone dane o wulkanach)
        items = raw_data if isinstance(raw_data, list) else raw_data.get("volcanoes", [])  # Grab the list of items whether the root is a list or a dictionary (Pobiera listę elementów niezależnie czy główny obiekt to lista czy słownik)
        for item in items:  # Loop through each volcano item returned by the API (Pętla przechodząca po każdym wulkanie zwróconym przez API)
            name = item.get("volcano_name") or item.get("name")  # Get the volcano name using whichever key name exists (Pobiera nazwę wulkanu niezależnie od tego, jak nazywa się klucz)
            lat = item.get("latitude") or item.get("lat")  # Get latitude from the item (Pobiera szerokość geograficzną z elementu)
            lon = item.get("longitude") or item.get("lon")  # Get longitude from the item (Pobiera długość geograficzną z elementu)
            if name is not None and lat is not None and lon is not None:  # Check that name and both coordinates actually exist (Sprawdza, czy nazwa i obie współrzędne naprawdę istnieją)
                parsed.append({  # Add a clean dictionary to the parsed list (Dodaje czysty słownik do listy wynikowej)
                    "name": str(name),  # Save volcano name as text (Zapisuje nazwę wulkanu jako tekst)
                    "lat": float(lat),  # Save latitude as a decimal number (Zapisuje szerokość geograficzną jako liczbę zmiennoprzecinkową)
                    "lon": float(lon),  # Save longitude as a decimal number (Zapisuje długość geograficzną jako liczbę zmiennoprzecinkową)
                    "alert_level": int(item.get("alert_level_num") or item.get("alert_level") or 1),  # Save alert level as a whole number, defaulting to 1 (Zapisuje poziom alertu jako liczbę całkowitą, domyślnie 1)
                })  # Finish adding the dictionary (Kończy dodawanie słownika)
        if parsed:  # Check if we successfully collected at least one volcano (Sprawdza, czy udało się zebrać przynajmniej jeden wulkan)
            return parsed  # Return the list of parsed volcanoes (Zwraca listę przetworzonych wulkanów)
        return FALLBACK_VOLCANOES  # Return backup volcanoes if the API returned nothing usable (Zwraca wulkany zapasowe, jeśli API nie zwróciło nic użytecznego)
    except Exception as exc:  # Catch any error that happened inside the try block (Łapie dowolny błąd, który wydarzył się w bloku try)
        print(f"API fallback triggered: {exc}")  # Print a message explaining we switched to backup data (Wypisuje komunikat, że przełączono się na dane zapasowe)
        return FALLBACK_VOLCANOES  # Return the backup volcano list so the script still works (Zwraca zapasową listę wulkanów, żeby skrypt nadal działał)


def analyze_volcanoes(volcanoes: list[dict]) -> dict:  # Define a function that runs NumPy and SciPy math on the volcanoes (Definiuje funkcję wykonującą obliczenia NumPy i SciPy na wulkanach)
    coords = np.array([[v["lat"], v["lon"]] for v in volcanoes], dtype=float)  # Build a 2D NumPy array of [latitude, longitude] pairs (Tworzy dwuwymiarową tablicę NumPy z par [szerokość, długość])
    alerts = np.array([v["alert_level"] for v in volcanoes], dtype=float)  # Build a 1D NumPy array of alert levels (Tworzy jednowymiarową tablicę NumPy z poziomami alertu)

    mean_alert = float(np.mean(alerts))  # Calculate the average alert level across all volcanoes (Liczy średni poziom alertu dla wszystkich wulkanów)
    std_alert = float(np.std(alerts))  # Calculate how spread out the alert levels are (Liczy odchylenie standardowe, czyli rozrzut poziomów alertu)
    if std_alert > 0:  # Avoid dividing by zero if every volcano has the exact same alert level (Chroni przed dzieleniem przez zero, gdy wszystkie wulkany mają ten sam alert)
        z_scores = (alerts - mean_alert) / std_alert  # Compute z-scores to see which volcanoes stand out above average (Liczy z-score, żeby zobaczyć, które wulkany odstają powyżej średniej)
    else:  # Run this branch when standard deviation is zero (Wykonuje tę gałąź, gdy odchylenie standardowe wynosi zero)
        z_scores = np.zeros_like(alerts)  # Create an array of zeros of the same shape as alerts (Tworzy tablicę samych zer o takim samym kształcie jak alerts)

    tree = cKDTree(coords)  # Build a SciPy spatial tree from coordinates for fast neighbor lookup (Buduje drzewo przestrzenne SciPy ze współrzędnych do szybkiego szukania sąsiadów)
    distances, neighbor_indices = tree.query(coords, k=2)  # Find the 2 closest points to each volcano (itself at index 0 and nearest neighbor at index 1) (Szuka 2 najbliższych punktów dla każdego wulkanu: siebie i sąsiada)

    enriched = []  # Create a list to hold volcanoes enriched with analysis results (Tworzy listę na wulkany wzbogacone o wyniki analizy)
    for idx, vol in enumerate(volcanoes):  # Loop over volcanoes together with their index number (Pętla po wulkanach wraz z ich numerem indeksu)
        nearest_idx = int(neighbor_indices[idx, 1])  # Get the index of the closest neighboring volcano (Pobiera indeks najbliższego sąsiedniego wulkanu)
        nearest_dist_deg = float(distances[idx, 1])  # Get coordinate distance to that nearest neighbor (Pobiera odległość we współrzędnych do najbliższego sąsiada)
        enriched.append({  # Add a dictionary with original data plus NumPy/SciPy metrics (Dodaje słownik z oryginalnymi danymi oraz wynikami z NumPy i SciPy)
            **vol,  # Copy all existing keys and values from the volcano dictionary (Kopiuje wszystkie istniejące klucze i wartości ze słownika wulkanu)
            "alert_z_score": round(float(z_scores[idx]), 2),  # Add rounded alert z-score (Dodaje zaokrąglony z-score poziomu alertu)
            "nearest_volcano": volcanoes[nearest_idx]["name"],  # Add the name of the closest neighbor volcano (Dodaje nazwę najbliższego sąsiedniego wulkanu)
            "nearest_lat": volcanoes[nearest_idx]["lat"],  # Save nearest neighbor latitude for drawing a map line (Zapisuje szerokość sąsiada do narysowania linii na mapie)
            "nearest_lon": volcanoes[nearest_idx]["lon"],  # Save nearest neighbor longitude for drawing a map line (Zapisuje długość sąsiada do narysowania linii na mapie)
            "nearest_distance_deg": round(nearest_dist_deg, 2),  # Add distance in degrees to the closest neighbor (Dodaje odległość w stopniach do najbliższego sąsiada)
        })  # Close the enriched volcano dictionary (Zamyka słownik wzbogaconego wulkanu)

    return {  # Return a summary dictionary with overall stats and per-volcano results (Zwraca słownik podsumowujący z ogólnymi statystykami i wynikami dla każdego wulkanu)
        "total_volcanoes": len(volcanoes),  # Store how many volcanoes were analyzed (Zapisuje liczbę przeanalizowanych wulkanów)
        "mean_alert": round(mean_alert, 2),  # Store rounded average alert level (Zapisuje zaokrąglony średni poziom alertu)
        "volcanoes": enriched,  # Store the detailed list of volcanoes (Zapisuje szczegółową listę wulkanów)
    }  # Close the returned summary dictionary (Zamyka zwracany słownik podsumowujący)


def alert_to_color(alert_level: int) -> str:  # Define a helper function that maps alert numbers to marker colors (Definiuje funkcję pomocniczą zamieniającą poziom alertu na kolor pinezki)
    if alert_level >= 3:  # Check if alert level is high (3 or more) (Sprawdza, czy poziom alertu jest wysoki, czyli 3 lub więcej)
        return "red"  # Return red for high alert (Zwraca czerwony kolor dla wysokiego alertu)
    if alert_level == 2:  # Check if alert level is medium (2) (Sprawdza, czy poziom alertu jest średni, czyli 2)
        return "orange"  # Return orange for medium alert (Zwraca pomarańczowy kolor dla średniego alertu)
    return "green"  # Return green for low/normal alert (Zwraca zielony kolor dla niskiego lub normalnego alertu)


def build_map(report: dict, output_path: str) -> None:  # Define a function that creates and saves the Folium HTML map (Definiuje funkcję tworzącą i zapisującą interaktywną mapę HTML w Folium)
    volcanoes = report["volcanoes"]  # Extract the enriched list of volcanoes from the report (Wyciąga z raportu wzbogaconą listę wulkanów)
    center_lat = float(np.mean([v["lat"] for v in volcanoes]))  # Compute average latitude so the map starts centered near the data (Liczy średnią szerokość, żeby mapa wyśrodkowała się blisko danych)
    center_lon = float(np.mean([v["lon"] for v in volcanoes]))  # Compute average longitude for the initial map center (Liczy średnią długość dla początkowego środka mapy)

    volcano_map = folium.Map(location=[center_lat, center_lon], zoom_start=3, tiles=None)  # Create an empty Folium map without default blocked tiles (Tworzy pustą mapę Folium bez domyślnych, zablokowanych kafelków)

    TileLayer(  # Create a custom tile layer that avoids the OSM 403 block (Tworzy własną warstwę kafelków, która omija blokadę 403 z OSM)
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",  # URL template for clean CartoDB Positron map tiles (Adres URL szablonu czystych kafelków mapy CartoDB Positron)
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',  # Required attribution text shown on the map (Wymagany tekst z informacją o autorach wyświetlany na mapie)
        name="CartoDB Positron",  # Give the map layer a readable name (Nadaje warstwie mapy czytelną nazwę)
        max_zoom=19,  # Set maximum zoom level supported by these tiles (Ustawia maksymalny poziom przybliżenia obsługiwany przez te kafelki)
        user_agent="VolcanoPortfolioAnalyzer/1.0 (student portfolio project)",  # Send a custom User-Agent identifying your app (Wysyła własny User-Agent identyfikujący Twoją aplikację)
    ).add_to(volcano_map)  # Add the custom tile layer onto the map (Dodaje własną warstwę kafelków do mapy)

    for vol in volcanoes:  # Loop through each volcano to add its marker and neighbor line (Pętla po każdym wulkanie, aby dodać jego pinezkę i linię do sąsiada)
        popup_text = (  # Build multi-line popup HTML text with volcano stats (Tworzy wielolinijkowy tekst okienka popup ze statystykami wulkanu)
            f"<b>{vol['name']}</b><br>"  # Show volcano name in bold (Pokazuje nazwę wulkanu pogrubioną czcionką)
            f"Alert level: {vol['alert_level']}<br>"  # Show numeric alert level (Pokazuje liczbowy poziom alertu)
            f"Alert z-score: {vol['alert_z_score']}<br>"  # Show NumPy z-score metric (Pokazuje wskaźnik z-score obliczony w NumPy)
            f"Nearest: {vol['nearest_volcano']} ({vol['nearest_distance_deg']} deg)"  # Show nearest volcano and distance in degrees (Pokazuje najbliższy wulkan i odległość w stopniach)
        )  # Finish building the popup text string (Kończy składanie tekstu okienka popup)

        folium.CircleMarker(  # Add a colored circle marker at the volcano's coordinates (Dodaje kolorowe kółko-znacznik we współrzędnych wulkanu)
            location=[vol["lat"], vol["lon"]],  # Set marker position to [latitude, longitude] (Ustawia pozycję znacznika na [szerokość, długość])
            radius=7,  # Set circle size in pixels on screen (Ustawia rozmiar kółka w pikselach na ekranie)
            color=alert_to_color(vol["alert_level"]),  # Set outline color based on alert level (Ustawia kolor obramowania na podstawie poziomu alertu)
            fill=True,  # Enable filling the inside of the circle (Włącza wypełnienie wnętrza kółka)
            fill_color=alert_to_color(vol["alert_level"]),  # Set fill color to match alert level (Ustawia kolor wypełnienia zgodny z poziomem alertu)
            fill_opacity=0.85,  # Make the circle slightly transparent so overlapping markers stay visible (Ustawia lekka przezroczystość, żeby nachodzące punkty były widoczne)
            popup=folium.Popup(popup_text, max_width=260),  # Attach the clickable info popup to the marker (Przypina klikalne okienko informacyjne do znacznika)
            tooltip=vol["name"],  # Show volcano name when hovering the mouse over the marker (Pokazuje nazwę wulkanu po najechaniu myszką na znacznik)
        ).add_to(volcano_map)  # Add this marker onto the map object (Dodaje ten znacznik do obiektu mapy)

        folium.PolyLine(  # Draw a dashed line connecting the volcano to its nearest neighbor (Rysuje przerywaną linię łączącą wulkan z jego najbliższym sąsiadem)
            locations=[[vol["lat"], vol["lon"]], [vol["nearest_lat"], vol["nearest_lon"]]],  # Pass start and end [lat, lon] coordinates for the line (Przekazuje współrzędne [lat, lon] początku i końca linii)
            color="#555555",  # Set a dark gray color for the connecting line (Ustawia ciemnoszary kolor linii łączącej)
            weight=1.5,  # Set line thickness in pixels (Ustawia grubość linii w pikselach)
            dash_array="5, 5",  # Make the line dashed with 5px dash and 5px gap (Tworzy linię przerywaną: 5 px kreski i 5 px przerwy)
        ).add_to(volcano_map)  # Add the line onto the map object (Dodaje linię do obiektu mapy)

    volcano_map.save(output_path)  # Save the full interactive map as an HTML file you can open in any browser (Zapisuje całą interaktywną mapę jako plik HTML do otwarcia w przeglądarce)


def main() -> None:  # Define the main entry-point function of the program (Definiuje główną funkcję startową programu)
    volcanoes = fetch_volcanoes(API_URL)  # Fetch volcano data from the API or fallback list (Pobiera dane o wulkanach z API lub z listy zapasowej)
    report = analyze_volcanoes(volcanoes)  # Run NumPy and SciPy analysis on the fetched volcanoes (Uruchamia analizę NumPy i SciPy na pobranych wulkanach)
    build_map(report, OUTPUT_MAP_FILE)  # Generate and save the interactive HTML map file (Generuje i zapisuje interaktywną mapę w pliku HTML)
    print(f"Map saved to {OUTPUT_MAP_FILE}")  # Confirm in console that the map file was created (Wypisuje w konsoli potwierdzenie utworzenia pliku mapy)
    print(json.dumps(report, indent=2))  # Print the final report formatted nicely as readable JSON (Wypisuje końcowy raport ładnie sformatowany jako czytelny JSON)


if __name__ == "__main__":  # Run main() only when executing this file directly, not when importing it (Uruchamia main() tylko przy bezpośrednim odpaleniu pliku, a nie przy imporcie)
    main()  # Call the main function to start the script (Wywołuje funkcję main, aby uruchomić skrypt)