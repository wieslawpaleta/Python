# Import the mss class from the mss library for fast screen capturing
from mss import mss # (Zaimportuj klasę mss z biblioteki mss do szybkiego przechwytywania ekranu)

# Import the Image module from Pillow so we can save the screenshot as a file
from PIL import Image # (Zaimportuj moduł Image z Pillow, aby zapisać zrzut ekranu jako plik)

# Define the screen area we want to capture (in pixels)
# top = distance from top edge, left = distance from left edge, width = box width, height = box height
monitor_area = {"top": 100, "left": 100, "width": 500, "height": 200} # (Zdefiniuj obszar ekranu w pikselach: top = od góry, left = od lewej, width = szerokość, height = wysokość)

# Create an mss instance using a 'with' block so resources are cleaned up automatically
with mss() as sct: # (Utwórz obiekt sct w bloku 'with', aby po zakończeniu automatycznie posprzątać pamięć)
    # Capture the raw pixel data of the defined screen area
    raw_screenshot = sct.grab(monitor_area) # (Zrób surowy zrzut pikseli ze wskazanego obszaru monitor_area)

    # Convert the raw BGRA bytes from mss into a standard RGB Pillow Image
    img = Image.frombytes("RGB", raw_screenshot.size, raw_screenshot.bgra, "raw", "BGRX") # (Zamień surowe bajty BGRA z mss na zwykły obrazek RGB w bibliotece Pillow)

    # Save the image to the current folder as 'capture.png'
    img.save("capture.png") # (Zapisz obrazek w bieżącym folderze pod nazwą 'capture.png')

# Print a confirmation message to the console
print("Screenshot saved as capture.png!") # (Wypisz w konsoli potwierdzenie, że zrzut ekranu został zapisany jako capture.png)