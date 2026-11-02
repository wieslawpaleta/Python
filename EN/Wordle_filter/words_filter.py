import os
import re
import json
import pdfplumber

def extract_and_save_wordle_words(pdf_path, output_txt="wordle_words.txt", output_json="wordle_words.json"):
    # Check if file exists [Sprawdzenie, czy plik istnieje]
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File '{pdf_path}' not found! [Błąd: Nie znaleziono pliku!]")
        return []

    unique_words = set()
    
    print("⏳ Extracting text layer... [Wyciąganie warstwy tekstowej...]")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Find only 5-letter words made of standard alphabetic characters
                    # [Wyszukiwanie tylko 5-literowych słów składających się z liter]
                    words = re.findall(r'\b[a-zA-Z]{5}\b', text)
                    for word in words:
                        # Normalize to uppercase for Wordle standard [Konwersja na wielkie litery - standard Wordle]
                        unique_words.add(word.upper())
    except Exception as e:
        print(f"⚠️ Error reading PDF: [Błąd podczas odczytu PDF:] {e}")

    sorted_words = sorted(list(unique_words))
    print(f"✅ Found {len(sorted_words)} unique 5-letter words. [Znaleziono {len(sorted_words)} unikalnych słów 5-literowych.]")

    # 1. Save to TXT file (one word per line) [Zapis do pliku TXT (jedne słowo na linijkę)]
    try:
        with open(output_txt, "w", encoding="utf-8") as f_txt:
            for word in sorted_words:
                f_txt.write(word + "\n")
        print(f"📁 Saved words to TXT file: [Zapisano słowa do pliku TXT:] {output_txt}")
    except Exception as e:
        print(f"❌ Could not save TXT file: [Nie udało się zapisać pliku TXT:] {e}")

    # 2. Save to JSON file [Zapis do pliku JSON]
    try:
        with open(output_json, "w", encoding="utf-8") as f_json:
            json.dump(sorted_words, f_json, ensure_ascii=False, indent=4)
        print(f"📁 Saved words to JSON file: [Zapisano słowa do pliku JSON:] {output_json}")
    except Exception as e:
        print(f"❌ Could not save JSON file: [Nie udało się zapisać pliku JSON:] {e}")

    return sorted_words

if __name__ == "__main__":
    # Use full path with r"" prefix [Użyj pełnej ścieżki z przedrostkiem r""]
    pdf_file_path = r"C:\Users\Nazwaużytkownika\Downloads\Program\Python\Projects EN\Wordle_filter\chemia.pdf"
    
    words_list = extract_and_save_wordle_words(pdf_file_path)