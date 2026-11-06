import google.generativeai as genai

# Configure your Gemini API key [Konfiguracja klucza API Gemini]
genai.configure(api_key="AQ.Ab8RN6LZcEPOzjGtT_f2wp4NUf6XOhpafaRCnRBRwkmha4Ds0Q")

# List all models supporting content generation [Wyświetl wszystkie modele obsługujące generowanie treści]
print("🔍 Checking available models for your API key... [Sprawdzanie dostępnych modeli dla Twojego klucza API...]")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Model name [Nazwa modelu]: {m.name}")