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
                    # 1. Fix line-break hyphens (e.g. words split across lines like word- \n word)
                    # [Naprawianie myślników dzielących wyrazy na końcu linii]
                    text = re.sub(r'-\s*\n\s*', '', text)
                    
                    # 2. Split text into individual words by whitespace
                    # [Podział tekstu na pojedyncze słowa po białych znakach]
                    tokens = text.split()
                    
                    for token in tokens:
                        # 3. Strip surrounding punctuation (quotes, dashes, commas, etc.)
                        # [Usuwanie otaczającej interpunkcji, cudzysłowów, myślników itp.]
                        clean_token = re.sub(r'^[^\w]+|[^\w]+$', '', token)
                        
                        # 4. Check if the clean token is strictly a 5-letter standalone word (Latin or Cyrillic)
                        # [Sprawdzanie, czy oczyszczony token to ściśle 5-literowe, samodzielne słowo (łacina lub cyrylica)]
                        if re.match(r'^[a-zA-Zа-яА-ЯёЁіІїЇєЄґҐ]{5}$', clean_token):
                            unique_words.add(clean_token.upper())
                            
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
    pdf_file_path = r"C:\Users\Łukasz\Downloads\Program\Python\Projects EN\Wordle_filter\chemia.pdf"
    
    generate_multilingual_wordle_json(pdf_file_path, "wordles_words.json")