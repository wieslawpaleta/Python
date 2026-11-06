import os
import re
import json
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
import google.generativeai as genai

# Configure your Gemini API key [Konfiguracja klucza API Gemini]
genai.configure(api_key="AQ.Ab8RN6LZcEPOzjGtT_f2wp4NUf6XOhpafaRCnRBRwkmha4Ds0Q")

def process_pdf_for_wordle(pdf_path, output_json="wordle_clean_words.json"):
    # Check if the PDF file exists [Sprawdzenie, czy plik PDF istnieje]
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File '{pdf_path}' not found! [Błąd: Nie znaleziono pliku!]")
        return []

    raw_words = set()
    
    # 1. Extract text from text-based layers [Wyciąganie tekstu z warstw tekstowych]
    print("⏳ Extracting text layer... [Wyciąganie warstwy tekstowej...]")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Fix line-break hyphens [Naprawianie myślników na końcu linii]
                    text = re.sub(r'-\s*\n\s*', '', text)
                    tokens = text.split()
                    for token in tokens:
                        # Clean surrounding punctuation [Czyszczenie otaczającej interpunkcji]
                        clean_token = re.sub(r'^[^\w]+|[^\w]+$', '', token)
                        # Match 5-letter words (Latin + Cyrillic) [Wzorzec 5-literowych słów: łacina + cyrylica]
                        if re.match(r'^[a-zA-Zа-яА-ЯёЁіІїЇєЄґҐ]{5}$', clean_token):
                            raw_words.add(clean_token.upper())
    except Exception as e:
        print(f"⚠️ Error reading text layer: [Błąd odczytu warstwy tekstowej:] {e}")

    # 2. Extract text from images using OCR [Wyciąganie tekstu z obrazów przy użyciu OCR]
    print("⏳ Running OCR on images... [Uruchamianie OCR na obrazach...]")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            ocr_text = pytesseract.image_to_string(image)
            if ocr_text:
                tokens = ocr_text.split()
                for token in tokens:
                    clean_token = re.sub(r'^[^\w]+|[^\w]+$', '', token)
                    if re.match(r'^[a-zA-Zа-яА-ЯёЁіІїЇєЄґҐ]{5}$', clean_token):
                        raw_words.add(clean_token.upper())
    except Exception as e:
        print(f"⚠️ OCR Error: [Błąd OCR:] {e}")

    words_list = sorted(list(raw_words))
    print(f"✅ Extracted {len(words_list)} potential words. Validating with Gemini... [Wyciągnięto {len(words_list)} potencjalnych słów. Trwa weryfikacja przez Gemini...]")

    # 3. Validate words using Gemini API to filter out OCR junk/abbreviations
    # [Weryfikacja słów przy użyciu API Gemini w celu odrzucenia śmieci OCR i skrótów]
    model = genai.GenerativeModel('gemini-3.8-flash')
    verified_words = []
    batch_size = 300

    for i in range(0, len(words_list), batch_size):
        batch = words_list[i:i + batch_size]
        prompt = (
            "Review the following list of 5-letter words. Remove any acronyms, abbreviations, "
            "partial chemical formulas, random character strings, or OCR errors that are not real, "
            "valid standalone words. Return *only* a valid JSON array of strings containing the valid words:\n"
            f"{json.dumps(batch, ensure_ascii=False)}"
        )
        try:
            response = model.generate_content(prompt)
            clean_text = response.text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            
            batch_result = json.loads(clean_text.strip())
            verified_words.extend(batch_result)
        except Exception as e:
            print(f"⚠️ Error in batch validation: [Błąd weryfikacji partii:] {e}")

    final_words = sorted(list(set(verified_words)))

    # 4. Save to JSON file [Zapis do pliku JSON]
    try:
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(final_words, f, ensure_ascii=False, indent=4)
        print(f"📁 Saved clean words to: [Zapisano czyste słowa do:] {output_json}")
    except Exception as e:
        print(f"❌ Error saving JSON: [Błąd zapisu JSON:] {e}")

    return final_words

if __name__ == "__main__":
    # Path to your PDF file [Ścieżka do Twojego pliku PDF]
    pdf_file_path = r"C:\Users\Łukasz\Downloads\Program\Python\Projects EN\Wordle_filter\chemia.pdf"
    process_pdf_for_wordle(pdf_file_path)