# Import the 'mss' library for ultra-dast screenshots (Importujemy bibliotekę 'mss' do ultraszybkich zrzutów ekranu)
import mss

# Import 'numpy' to handle math arrays of image pixels (Importujemy 'numpy' do obsługi matematycznych tablic pikseli obrazu)
import numpy as np

# Import 'cv2' (OpenCV) to resize and format image colors (Importujemy 'cv2' (OpenCV) do zmiany rozmiaru i formatowania kolorów obrazu)
import cv2

# Import 'pyvirtualcam' to send frames to the virtual camera driver (Importujemy 'pyvirtualcam', aby wysyłać klatki do sterownik wirtualnej kamery)
import pyvirtualcam

# Define the region of the screen we want to stream (Definiujemy obszar ekranu, który chcemy przesyłać strumieniowo)
monitor_area = {
    "top": 100, # Distance from the top of the screen (Odległość od góry ekranu)
    "left": 100, # Distance from the left of the screen (Odległość od lewej strony ekranu)
    "width": 1280, # Width of the frame - virtual cameras love standard HD sizes like 1280 (Szerokość klatkość - wirtualne kamery lubią standardowe rozmiary HD jak 1280)
    "height": 720 # Height of the frame (Wysokość klatki)
}

# Target frame rate for our virtual camera video stream (Docelowa liczba klatek na sekundę dla naszego strumienia wideo z wirtualnej kamery)
FPS = 30

# Initialize screen capture using mss (Inicjalizujemy przechwytywanie ekranie za pomocą mss)
with mss.MSS() as sct:

    # Start the virtual camera context with matching width, height, and fps (Uruchamiamy kontekst wirtualnej kamery z pasującą szerokością, wysokością i fps)
    with pyvirtualcam.Camera(width=monitor_area["width"], height=monitor_area["height"], fps=FPS) as cam:

        # Print a message to the console showing it is successfully running (Wypisujemy wiadomość w konsoli pokazującą, że program pomyślnie działa)
        print(f"Virtual camera started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)")
        print("Press Ctrl+C in your terminal to stop")

        # Start and infinite loop to push video frames continuously (Rozpoczynamy nieskończoną pętlę, aby ciągle przesyłać klatki wideo)
        while True:

            # Grab a screenshot of the specified monitor area (Pobieramy zrzut ekranu określonego obszaru monitora)
            raw_screenshot = sct.grab(monitor_area)

            # Convert screenshot bytes into a numpy array (Konwertujemy bajty zrzutu ekranu na tablicę numpy)
            image_array = np.array(raw_screenshot)

            # Convert color format from BGRA (Blue-Green-Red-Alpha) to RGB 
            frame = cv2.cvtColor(image_array, cv2.COLOR_BGRA2RGB)

            # Send the converted RGB frame directly into the virtual camera (Wysyłamy skonwertowaną klatkę RGB bezpośrednio do wirtualnej kamery)
            cam.send(frame)

            # Wait for the next frame to match out target FPS speed (Czekamy na następną klatkę, aby dopasować prędkość do docelowego FPS)
            cam.sleep_until_next_frame
