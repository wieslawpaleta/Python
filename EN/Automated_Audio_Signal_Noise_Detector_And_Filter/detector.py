# Import the NumPy library for numerical operations and matrix calculations (Importujemy bibliotekę NumPy do operacji numerycznych i obliczeń na macierzach/tablicach)
import numpy as np

# Import the signal module from SciPy to perform filtering and signal analysis (Importujemy moduł 'signal' z biblioteki SciPy do filtrowania i analizy sygnałów)
from scipy import signal

# Import the fft module from SciPy to transform signal from time domain to frequency domain (Importujemy moduł 'fft' z SciPy do przekształcania sygnału z dziedziny czasu do dziedziny częstotliwości)
from scipy.fft import fft, fftfreq


# Define the sampling rate: how many data points/measurements we take per second (Definiujemy częstotliwość próbkowania: ile punktów danych/pomiarów zbieramy na jedną sekundę)
SAMPLING_RATE = 1000

# Define the duration of the audio signal in seconds (Definiujemy czas trwania sygnału dźwiękowego w sekundach)
DURATION = 2.0


# Generate an array of time steps from 0 to DURATION with a step size of 1/SAMPLING_RATE (Tworzymy tablicę punktów czasowych od 0 do DURATION z krokiem równym 1/SAMPLING_RATE)
time = np.arange(0, DURATION, 1 / SAMPLING_RATE)

# Create a clean signal using a sine wave with a frequency of 5 Hz (Tworzymy czysty sygnał za pomocą fali sinusoidalnej o częstotliwości 5 Hz)
# 2 * pi * 5 time calculates the angle for each time point (2 * pi * 5 * time oblicza kąt dla każdego punktu w czasie)
clean_signal = np.sin(2 * np.pi * 5 * time)


# Fix the random speed so we get the exact same random numbers every time we run the code (Ustawiamy ziarno losowości, aby generować dokładnie te same losowe liczby przy każdym uruchomieniu kodu)
np.random.seed(42)