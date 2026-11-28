# Import soundcard to capture system audio on Windows 11 (Importujemy soundcard, aby przechwytywać dźwięk systemowy w Windows 11)
import soundcard as sc

# Import numpy for fast math and array operations (Importujemy numpy do szybkiej matematyki i operacji na tablicach)
import numpy as np

# Import signal tools from scipy to filter frequencies (Importujemy narzędzia sygnałowe ze scipy do filtrowania częstotliwości)
from scipy import signal

# Define the sample rate in Hertz, matching CD quality (Ustalamy częstotliwość próbkowania w hercach, zgodną z jakością CD)
SAMPLE_RATE = 44100

# Define how many audio frames we read per update step (Ustalamy, ile ramek audio czytamy w jednym kroku aktualizacji)
CHUNK_SIZE = 1024

# Design a 4th-order Butterworth high-pass filter above 20 Hz to remove sub-audible rumble (Projektujemy filtr górnoprzepustowy Butterwortha 4. rzędu powyżej 20 Hz, aby usunąć niesłyszalny dudniący szum)
sos_filter = signal.butter(N=4, Wn=20, btype="highpass", fs=SAMPLE_RATE, output="sos")

# Get the default speaker that is currently playing sound on your computer (Pobieramy domyślny głośnik, który aktualnie odtwarza dźwięk na komputerze)
default_speaker = sc.default_speaker()

# Print the name of the speaker to the console so we know it works (Wypisujemy nazwę głośnika w konsoli, żeby wiedzieć, że to działa)
print(f"Monitoring speaker: {default_speaker.name}")

# Get a virtual microphone that listens to what the speaker is playing - called Loopback (Pobieramy wirtualny mikrofon, który słucha tego, co gra głośnik - tzw. Loopback)
loopback_mic = sc.get_microphone(id=str(default_speaker.name), include_loopback=True)

print("Live dBFS monitor started. Press Ctrl+C to stop.")

# Open the audio stream with a sample rate of 44100 Hz - standard CD quality (Otwieramy strumień audio z próbkowaniem 44100 Hz - standardowa jakość płyty CD)
with loopback_mic.recorder(samplerate=44100) as mic:
    # Print a message telling the user to play some sound (Wypisujemy wiadomość, żeby użytkownik włączył jakiś dźwięk)
    print("Recording 2 seconds of system audio... Play some music or a video!")
    
    # Record 88200 samples, which equals 2 seconds because 44100 * 2 = 88200 (Nagrywamy 88200 próbek, co daje 2 sekundy, bo 44100 * 2 = 88200)
    data = mic.record(numframes=88200)
    
    # Print the shape of the captured data, e.g., rows and stereo channels (Wypisujemy kształt przechwyconych danych, np. wiersze i kanały stereo)
    print(f"Captured data shape: {data.shape}")
    
    # Print the highest raw audio peak recorded during those 2 seconds (Wypisujemy najwyższy surowy skok dźwięku nagrany w ciągu tych 2 sekund)
    print(f"Max raw amplitude: {np.max(np.abs(data))}")