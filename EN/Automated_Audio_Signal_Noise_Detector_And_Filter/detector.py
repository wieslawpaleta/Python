# Import the NumPy library for numerical operations and matrix calculations (Importujemy bibliotekę NumPy do operacji numerycznych i obliczeń na macierzach/tablicach)
import numpy as np

# Import the signal module from SciPy to perform filtering and signal analysis (Importujemy moduł 'signal' z biblioteki SciPy do filtrowania i analizy sygnałów)
from scipy import signal

# Import the fft module from SciPy to transform signal from time domain to frequency domain (Importujemy moduł 'fft' z SciPy do przekształcania sygnału ze dziedziny czasu do dziedziny częstotliwości)
from scipy.fft import fft, fftfreq


# Define the sampling rate: how many data points/measurements we take per second (Definiujemy częstotliwość próbkowania: ile punktów danych/pomiarów zbieramy na jedną sekundę)
SAMPLING_RATE = 1000

# Define the duration of the audio signal in seconds (Definiujemy czas trwania sygnału dźwiękowego w sekundach)
DURATION = 2.0


# Generate an array of time steps from 0 to DURATION with a step size of 1/SAMPLING_RATE (Tworzymy tablicę punktów czasowych od 0 do DURATION z krokiem równym 1/SAMPLING_RATE)
time = np.arange(0, DURATION, 1 / SAMPLING_RATE)

# Create a clean signal using a sine wave with a frequency of 5 Hz (Tworzymy czysty sygnał za pomocą fali sinusoidalnej o częstotliwości 5 Hz)
# 2 * pi * 5 * time calculates the angle for each time point (2 * pi * 5 * time oblicza kąt dla każdego punktu w czasie)
clean_signal = np.sin(2 * np.pi * 5 * time)


# Fix the random seed so we get the exact same random numbers every time we run the code (Ustawiamy ziarno losowości, aby generować dokładnie te same losowe liczby przy każdym uruchomieniu kodu)
np.random.seed(42)

# Generate high-frequency random noise with a frequency of 50 Hz using a sine wave (Generujemy losowy szum o wysokiej częstotliwości 50 Hz używając fali sinusoidalnej)
noise_high_freq = 0.5 * np.sin(2 * np.pi * 50 * time)

# Generate pure random white noise using a normal (Gaussian) distribution (Generujemy czysty losowy szum biały używając rozkładu normalnego/Gaussa)
random_white_noise = np.random.normal(0, 0.2, len(time))

# Combine the clean signal and all noise components together (Łączymy czysty sygnał ze wszystkimi elementami szumu w jedną całość)
noisy_signal = clean_signal + noise_high_freq + random_white_noise


# Calculate the total number of samples/data points in the signal (Obliczamy całkowitą liczbę próbek/punktów danych w sygnale)
N = len(noisy_signal)

# Perform Fast Fourier Transform (FFT) on the noisy signal to get frequency amplitudes (Wykonujemy Szybką Transformatę Fouriera na zaszumionym sygnale, aby uzyskać amplitudy częstotliwości)
fft_values = fft(noisy_signal)

# Generate the corresponding frequency values in Hertz for the FFT result (Generujemy odpowiadające wartości częstotliwości w Hercach dla wyniku FFT)
fft_frequencies = fftfreq(N, 1 / SAMPLING_RATE)

# Take only the positive frequencies because FFT results are symmetric (Bierzemy tylko dodatnie częstotliwości, ponieważ wyniki FFT są symetryczne)
positive_frequencies = fft_frequencies[: N // 2]

# Compute the absolute amplitude value of the complex FFT output for positive frequencies (Obliczamy bezwzględną wartość amplitudy ze złożonego wyniku FFT dla dodatnich częstotliwości)
magnitude = np.abs(fft_values[: N // 2]) * (2.0 / N)


# Define the cutoff frequency for our low-pass filter: drop frequencies above 10 Hz (Definiujemy częstotliwość odcięcia dla naszego filtru dolnoprzepustowego: odrzucamy częstotliwości powyżej 10 Hz)
CUTOFF_FREQUENCY = 10.0

# Calculate the Nyquist frequency, which is always half of the sampling rate (Obliczamy częstotliwość Nyquista, która zawsze wynosi połowę częstotliwości próbkowania)
nyquist_freq = 0.5 * SAMPLING_RATE

# Normalize the cutoff frequency relative to the Nyquist frequency as required by SciPy (Normalizujemy częstotliwość odcięcia względem częstotliwości Nyquista, co jest wymagane przez SciPy)
normalized_cutoff = CUTOFF_FREQUENCY / nyquist_freq

# Create coefficients (b, a) for a 4th-order Butterworth low-pass filter (Tworzymy współczynniki (b, a) dla filtru dolnoprzepustowego Butterwortha 4. rzędu)
b, a = signal.butter(N=4, Wn=normalized_cutoff, btype="low", analog=False)

# Apply the filter forward and backward (filtfilt) to clear noise without shifting phase (Stosujemy filtr w przód i w tył (filtfilt), aby usunąć szum bez przesuwania fazy sygnału)
filtered_signal = signal.filtfilt(b, a, noisy_signal)


# Calculate Mean Squared Error (MSE) between clean signal and noisy signal (Obliczamy błąd średniokwadratowy (MSE) między czystym sygnałem a zaszumionym sygnałem)
noisy_mse = np.mean((clean_signal - noisy_signal) ** 2)

# Calculate Mean Squared Error (MSE) between clean signal and filtered signal (Obliczamy błąd średniokwadratowy (MSE) między czystym sygnałem a przefiltrowanym sygnałem)
filtered_mse = np.mean((clean_signal - filtered_signal) ** 2)

# Print the noise error result to the console (Wyświetlamy wynik błędu szumu w konsoli)
print(f"Noise Signal MSE (Błąd zaszumionego sygnału): {noisy_mse:.4f}")

# Print the filtered signal error result to the console (Wyświetlamy wynik błędu przefiltrowanego sygnału w konsoli)
print(f"Filtered Signal MSE (Błąd przefiltrowanego sygnału): {filtered_mse:.4f}")

# Calculate percentage improvement after noise filtering (Obliczamy procentową poprawę jakości po przefiltrowaniu szumu)
improvement = ((noisy_mse - filtered_mse) / noisy_mse) * 100

# Print the overall percentage improvement (Wyświetlamy ogólną procentową poprawę jakości)
print(f"Signal Noise Reduction Improvement (Poprawa jakości sygnału): {improvement:.2f}%")