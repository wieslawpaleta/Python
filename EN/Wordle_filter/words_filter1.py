import os
import re
import json
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
import google.generativeai as genai

# Configure your Gemini API key [Konfiguracja klucza API Gemini]
genai.configure(api_key="TUTAJ_WKLEJ_SWOJ_API_KEY")

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
   
   
    # Validate words using Gemini API to filter out OCR junk/abbreviations
    # Weryfikacja słów przy użyciu API Gemini w celu odrzucenia śmieci OCR i skrótów
    model = genai.GenerativeModel('gemini-1.5-flash')
    verified_words = []
    batch_size = 50

    for i in range(0, len(words_list), batch_size):
        batch = words_list[i:i + batch_size]
        prompt = ()