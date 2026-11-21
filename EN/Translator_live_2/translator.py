# Import GoogleTranslator and MyMemoryTranslator from deep_translator
from deep_translator import GoogleTranslator, MyMemoryTranslator # (Zaimportuj GoogleTranslator oraz MyMemoryTranslator z deep_translator)

# Import TooManyRequests exception so we can catch this specific error
from deep_translator.exceptions import TooManyRequests # (Zaimportuj wyjątek TooManyRequests, aby móc złapać ten konkretny błąd)

# Import pykakasi to convert Japanese text into Romaji
import pykakasi # (Zaimportuj bibliotekę pykakasi do zamiany tekstu japońskiego na Romaji)

# Import pypinyin to convert Chinese characters into Pinyin
from pypinyin import pinyin, Style # (Zaimportuj funkcje pinyin oraz Style z pypinyin do zamiany znaków chińskich na Pinyin)

# Initialize the Japanese converter object
kks = pykakasi.kakasi() # (Utwórz obiekt konwertera kks z biblioteki pykakasi)

# Helper function to convert Japanese text into Romaji
def to_romaji(japanese_text): # (Funkcja pomocnicza zamieniająca tekst japoński na Romaji)
    # Convert Japanese string into a list of dictionaries with pronunciation data
    converted = kks.convert(japanese_text) # (Przekonwertuj tekst japoński na listę słowników z wymową)
    # Join 'hepburn' (Romaji) pieces with spaces and remove leading/trailing spaces
    return " ".join(item["hepburn"] for item in converted).strip() # (Połącz części 'hepburn' czyli Romaji spacjami i przytnij spacje na końcach)

# Helper function to convert Chinese text into Pinyin with tone marks
def to_pinyin(chinese_text): # (Funkcja pomocnicza zamieniająca tekst chiński na Pinyin ze znakami tonów)
    # Convert each character into Pinyin syllables
    syllables = pinyin(chinese_text, style=Style.TONE) # (Zamień każdy znak na sylaby Pinyin w stylu Style.TONE)
    # Flatten the list and join syllables with spaces
    return " ".join(item[0] for item in syllables).strip() # (Spłaszcz listę i połącz sylaby spacjami)

# Helper function that tries GoogleTranslator first, and falls back to MyMemoryTranslator if rate-limited
def safe_translate(text, target_lang="pl"): # (Funkcja bezpiecznego tłumaczenia: najpierw próbuje Google, a w razie limitu przełącza na MyMemory)
    # Try using GoogleTranslator first
    try: # (Rozpocznij blok próbny dla GoogleTranslator)
        # Create GoogleTranslator with automatic source language detection
        google_tr = GoogleTranslator(source="auto", target=target_lang) # (Utwórz obiekt GoogleTranslator z automatycznym wykrywaniem języka źródłowego)
        # Return the translated string
        return google_tr.translate(text) # (Zwróć przetłumaczony tekst)
    # Catch TooManyRequests error if Google blocks or throttles the request
    except TooManyRequests: # (Złap błąd TooManyRequests, jeśli Google chwilowo zablokuje zapytania)
        # Notify the user in the console that we are switching fallback translators
        print("Google rate-limited requests; switching to MyMemoryTranslator...") # (Wypisz w konsoli informację o przełączeniu na zapasowy translator MyMemory)
        # Create fallback translator (MyMemory requires explicit source language like 'ja-JP' or 'zh-CN')
        fallback_tr = MyMemoryTranslator(source="ja-JP", target="pl-PL") # (Utwórz translator zapasowy MyMemory z japońskiego 'ja-JP' na polski 'pl-PL')
        # Return translation from fallback service
        return fallback_tr.translate(text) # (Zwróć tłumaczenie z zapasowego serwisu)
    # Catch any other unexpected translation errors so the script does not crash
    except Exception as error: # (Złap wszelkie inne nieprzewidziane błędy tłumaczenia, aby program się nie wyłożył)
        # Return a readable error message instead of crashing
        return f"[Translation error: {error}]" # (Zwróć czytelny komunikat błędu zamiast przerywać działanie programu)

# Example Japanese text to test translation and Romaji
source_text = "おはようございます" # (Przykładowy tekst po japońsku do przetestowania tłumaczenia i Romaji)

# Translate the text safely into Polish
translated_text = safe_translate(source_text, target_lang="pl") # (Bezpiecznie przetłumacz tekst na język polski)

# Generate Romaji pronunciation
romaji_text = to_romaji(source_text) # (Wygeneruj wymowę Romaji dla tekstu źródłowego)

# Print results to the console
print("Original:", source_text) # (Wypisz oryginalny tekst)
print("Romaji:", romaji_text) # (Wypisz wymowę Romaji)
print("Translation (PL):", translated_text) # (Wypisz przetłumaczony tekst po polsku)