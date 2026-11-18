# Import the 'mss' library which is super fast at taking screenshots (Importujemy bibliotekę 'mss', która jest super szybka w robieniu zrzutów ekranu)
import mss

# Import 'numpy' to convert screenshot data into a math array of pixels (Importujemy 'numpy', aby zamienić dane ze zrzutu ekranu w matematyczną tablicę pikseli)
import numpy as np

# Import 'cv2' (OpenCV) to process images and show them on screen (Importujemy 'cv2' (OpenCV), aby przetwarzać obrazy i wyświetlać je na ekranie)
import cv2

# Define the area of the screen we want to record using a dictionary (Definiujemy obszar ekranu, który chcemy nagrywać, używając słownika)
monitor_area = {
    "top": 100,     # Distance in pixels from the top edge of the screen (Odległość w pikselach od górnej krawędzi ekranu)
    "left": 100,    # Distance in pixels from the left edge of the screen (Odległość w pikselach od lewej krawędzi ekranu)
    "width": 800,   # Width of the captured box in pixels (Szerokość przechwytywanego obszaru w pikselach)
    "height": 600   # Height of the captured box in pixels (Wysokość przechwytywanego obszaru w pikselach)
}

# Start the screen capture tool safely using 'with' so it cleans up memory later (Uruchamiamy narzędzie do zrzutów bezpiecznie używając 'with', aby potem posprzątało pamięć)
with mss.mss() as sct:
    
    # Start an infinite loop to take screenshots continuously like a video camera (Rozpoczynamy nieskończoną pętlę, aby robić zrzuty bez przerwy jak kamera wideo)
    while True:
        
        # Grab a single screenshot of our defined area (Pobieramy pojedynczy zrzut ekranu z naszego zdefiniowanego obszaru)
        raw_screenshot = sct.grab(monitor_area)
        
        # Convert the raw screenshot into a numpy array of numbers that Python can understand (Zamieniamy surowy zrzut ekranu w tablicę liczb numpy, którą Python rozumie)
        image_array = np.array(raw_screenshot)
        
        # Remove the transparency channel (BGRA to BGR) because OpenCV doesn't need it (Usuwamy kanał przezroczystości (z BGRA na BGR), ponieważ OpenCV go nie potrzebuje)
        frame = cv2.cvtColor(image_array, cv2.COLOR_BGRA2BGR)
        
        # Create a window named 'Screen Preview' and show our captured frame inside it (Tworzymy okno o nazwie 'Screen Preview' i pokazujemy w nim naszą przechwyconą klatkę)
        cv2.imshow("Screen Preview", frame)
        
        # Wait 1 millisecond for a key press; if the key is 'q', break out of the loop (Czekamy 1 milisekundę na wciśnięcie klawisza; jeśli to klawisz 'q', przerywamy pętlę)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Close all windows created by OpenCV to clean up the screen (Zamykamy wszystkie okna stworzone przez OpenCV, aby posprzątać ekran)
cv2.destroyAllWindows()