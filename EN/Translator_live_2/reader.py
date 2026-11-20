# Import the easyocr library for reading text from images
import easyocr # (Zaimportuj bibliotekę easyocr do odczytywania tekstu z obrazków)

# Create an OCR Reader for Japanese ('ja') and English ('en'); set gpu=False if you don't have a supported NVIDIA GPU
reader = easyocr.Reader(["ja", "en"], gpu=False) # (Utwórz czytnik OCR dla japońskiego 'ja' i angielskiego 'en'; ustaw gpu=False, jeśli nie masz karty NVIDIA obsługującej CUDA)

# Run OCR on the 'capture.png' image saved in Step 1
# detail=1 returns bounding box coordinates, text, and confidence score for each detection
results = reader.readtext("capture.png", detail=1) # (Uruchom OCR na obrazku 'capture.png' zapisanym w Kroku 1; detail=1 zwraca współrzędne ramki, tekst i pewność odczytu)

# Loop through each detected text block in the results
for box, text, confidence in results: # (Przejdź w pętli przez każdy wykryty blok tekstu w wynikach)
    # Print the extracted text and its confidence score (0.0 to 1.0)
    print(f"Detected: {text} (Confidence: {confidence:.2f})") # (Wypisz wykryty tekst oraz pewność odczytu zaokrągloną do 2 miejsc po przecinku)

    # Print the top-left and bottom-right corner coordinates of the text box
    top_left = box[0] # (Pobierz współrzędne lewego górnego rogu ramki wokół tekstu)
    bottom_right = box[2] # (Pobierz współrzędne prawego dolnego rogu ramki wokół tekstu)
    print(f"Box from {top_left} to {bottom_right}") # (Wypisz współrzędne ramki od lewego górnego do prawego dolnego rogu)