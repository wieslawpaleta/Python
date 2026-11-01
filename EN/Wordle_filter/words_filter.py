import re
import pdfplumber
from pdf2image import convert_from_path
import pytesseract

def extract_five_letter_words(pdf_path):
    # Initialize a set to store unique words [Inicjalizacja zbioru do przechowywania unikalnych słów]
    unique_words = set()
    
    # 1. Extract text from text-based layers [Wyciąganie tekstu z warstw tekstowych]
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Find all 5-letter words using regex [Wyszukiwanie wszystkich 5-literowych słów za pomocą wyrażenia regularnego]
                    words = re.findall(r'\b[a-zA-Z]{5}\b', text)
                    for word in words:
                        unique_words.add(word.lower()) # Convert to lowercase [Konwersja na małe litery]
    except Exception as e:
        print(f"Error reading text layer: [Błąd odczytu warstwy tekstowej:] {e}")

    # 2. Extract text from images using OCR [Wyciąganie tekstu z obrazów przy użyciu OCR]
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            # Run OCR on the page image [Uruchomienie OCR na obrazie strony]
            ocr_text = pytesseract.image_to_string(image)
            if ocr_text:
                ocr_words = re.findall(r'\b[a-zA-Z]{5}\b', ocr_text)
                for word in ocr_words:
                    unique_words.add(word.lower())
    except Exception as e:
        print(f"Error during OCR processing (make sure Tesseract is installed): [Błąd podczas przetwarzania OCR (upewnij się, że Tesseract jest zainstalowany):] {e}")

    # Return sorted unique words as a list [Zwrócenie posortowanych unikalnych słów jako listy]
    return sorted(list(unique_words))

if __name__ == "__main__":
    # Path to your PDF file [Ścieżka do Twojego pliku PDF]
    pdf_file_path = r"C:\Users\Nazwaużytkownika\Downloads\Program\Python\Projects EN\Wordle_filter\familia_romana.pdf"
    
    print(f"Processing PDF file: [Przetwarzanie pliku PDF:] {pdf_file_path}")
    result = extract_five_letter_words(pdf_file_path)
    
    print(f"\nFound {len(result)} unique 5-letter words: [Znaleziono {len(result)} unikalnych 5-literowych słów:]")
    print(result)