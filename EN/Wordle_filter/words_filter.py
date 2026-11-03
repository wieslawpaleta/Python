import os
import re
import json
import pdfplumber

def generate_multilingual_wordle_json(pdf_path, output_json="wordle_words.json"):
    # Check if file exists [Sprawdzenie, czy plik istnieje]
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File '{pdf_path}' not found! [Błąd: Nie znaleziono pliku!]")
        return []

    unique_words = set()
    
    print("⏳ Extracting text layer from PDF... [Wyciąganie warstwy tekstowej z PDF...]")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Regex supporting both Latin and Cyrillic 5-letter words 
                    # [Wyrażenie regularne obsługujące 5-literowe słowa łacińskie i cyrylicę]
                    words = re.findall(r'\b[a-zA-Zа-яА-ЯёЁіІїЇєЄґҐ]{5}\b', text)
                    for word in words:
                        # Convert to uppercase for Wordle standard [Konwersja na wielkie litery do standardu Wordle]
                        unique_words.add(word.upper())
    except Exception as e:
        print(f"⚠️ Error reading PDF: [Błąd podczas odczytu PDF:] {e}")

    # Sort words alphabetically [Sortowanie słów alfabetycznie]
    sorted_words = sorted(list(unique_words))
    print(f"✅ Found {len(sorted_words)} unique 5-letter words (Latin + Cyrillic). [Znaleziono {len(sorted_words)} unikalnych słów (łacina + cyrylica).]")

    # Save to JSON file with UTF-8 encoding to support Cyrillic characters properly
    # [Zapis do pliku JSON z kodowaniem UTF-8, aby poprawnie zapisać znaki cyrylicy]
    try:
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(sorted_words, f, ensure_ascii=False, indent=4)
        print(f"📁 Successfully saved to: [Pomyślnie zapisano do:] {output_json}")
    except Exception as e:
        print(f"❌ Could not save JSON file: [Nie udało się zapisać pliku JSON:] {e}")

    return sorted_words

if __name__ == "__main__":
    # Use full path with r"" prefix [Użyj pełnej ścieżki z przedrostkiem r""]
    pdf_file_path = r"C:\Users\nazwauzytkownika\Downloads\Program\Python\Projects EN\Wordle_filter\chemia.pdf"
    
    generate_multilingual_wordle_json(pdf_file_path, "wordles_words.json")