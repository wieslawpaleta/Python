# Import the argparse module to parse command-line arguments passed from the terminal (Importujemy moduł argparse do parsowania argumentów wiersza poleceń przekazywanych z terminala)
import argparse

# Import the NumPy library for numerical operations and matrix calculations (Importujemy bibliotekę NumPy do operacji numerycznych i obliczeń na macierzach/tablicach)
import numpy as np

# Import the signal module from SciPy to perform filtering and signal analysis (Importujemy moduł 'signal' z biblioteki SciPy do filtrowania i analizy sygnałów)
from scipy import signal

# Import the wavfile module from SciPy to read and write .wav audio files (Importujemy moduł 'wavfile' z SciPy do odczytu i zapisu plików dźwiękowych .wav)
from scipy.io import wavfile

# Import the pyplot module from matplotlib to create visual charts and graphs (Importujemy moduł pyplot z biblioteki matplotlib, żeby tworzyć wizualne wykresy i grafiki)
import matplotlib.pyplot as plt


# Define a class called AudioCleaner to bundle all audio processing logic together (Definiujemy klasę o nazwie AudioCleaner, aby połączyć całą logikę przetwarzania dźwięku w jedną całość)
class AudioCleaner:

    # Define the initialization constructor method for our class (Definiujemy metodę konstruktora inicjalizującego dla naszej klasy)
    def __init__(self, input_file, output_file, cutoff_freq):
        # Save the input file path as an object attribute (Zapisujemy ścieżkę pliku wejściowego jako atrybut obiektu)
        self.input_file = input_file

        # Save the output file path as an object attribute (Zapisujemy ścieżkę pliku wyjściowego jako atrybut obiektu)
        self.output_file = output_file

        # Save the cutoff frequency value as an object attribute (Zapisujemy wartość częstotliwości odcięcia jako atrybut obiektu)
        self.cutoff_freq = cutoff_freq

        # Initialize sampling_rate attribute as None before loading (Inicjalizujemy atrybut częstotliwości próbkowania jako None przed wczytaniem)
        self.sampling_rate = None

        # Initialize audio_data attribute as None before loading (Inicjalizujemy atrybut danych dźwiękowych jako None przed wczytaniem)
        self.audio_data = None

        # Initialize time attribute as None before calculation (Inicjalizujemy atrybut czasu jako None przed obliczeniem)
        self.time = None

        # Initialize noisy_signal attribute as None before generation (Inicjalizujemy atrybut zaszumionego sygnału jako None przed wygenerowaniem)
        self.noisy_signal = None

        # Initialize filtered_signal attribute as None before filtering (Inicjalizujemy atrybut przefiltrowanego sygnału jako None przed filtrowaniem)
        self.filtered_signal = None

    # Define a method to load and normalize the audio file (Definiujemy metodę do wczytywania i normalizacji pliku dźwiękowego)
    def load_audio(self):
        # Read sampling rate and raw audio data from the input .wav file (Odczytujemy częstotliwość próbkowania i surowe dane dźwiękowe z wejściowego pliku .wav)
        self.sampling_rate, self.audio_data = wavfile.read(self.input_file)

        # Check if the audio file has multiple dimensions (stereo channels) (Sprawdzamy, czy plik dźwiękowy ma wiele wymiarów (kanały stereo))
        if len(self.audio_data.shape) > 1:
            # Convert stereo audio to mono by calculating the mean across channels (Konwertujemy dźwięk stereo na mono poprzez obliczenie średniej wzdłuż kanałów)
            self.audio_data = np.mean(self.audio_data, axis=1)

        # Normalize the audio array values to float numbers between -1.0 and 1.0 (Normalizujemy wartości tablicy dźwiękowej do liczb zmiennoprzecinkowych z zakresu od -1.0 do 1.0)
        self.audio_data = self.audio_data / np.max(np.abs(self.audio_data))

        # Create an array of time steps for every sample in the audio (Tworzymy tablicę kroków czasowych dla każdej próbki w dźwięku)
        self.time = np.arange(0, len(self.audio_data)) / self.sampling_rate

# Define a method to add synthetic high-frequency noise and white noise (Definiujemy metodę do dodawania sztucznego szumu wysokiej częstotliwości oraz szumu białego)
def add_noise(self):
# Treat the loaded and normalized audio as our clean signal source (Traktujemy wczytany i znormalizowany dźwięk jako nasze źródło czystego sygnału)
clean_signal = audio_data


# Fix the random seed so we get the exact same random numbers every time we run the code (Ustawiamy ziarno losowości, aby generować dokładnie te same losowe liczby przy każdym uruchomieniu kodu)
np.random.seed(42)

# Generate high-frequency random noise using a sine wave to simulate interference (Generujemy losowy szum o wysokiej częstotliwości używając fali sinusoidalnej, aby symulować zakłócenia)
noise_high_freq = 0.3 * np.sin(2 * np.pi * 1500 * time)

# Generate pure random white noise using a normal distribution (Generujemy czysty losowy szum biały używając rozkładu normalnego)
random_white_noise = np.random.normal(0, 0.1, len(time))

# Combine the clean signal and all noise components together into a messy signal (Łączymy czysty sygnał ze wszystkimi elementami szumu w jeden zaszumiony sygnał)
noisy_signal = clean_signal + noise_high_freq + random_white_noise


# Define the cutoff frequency for our low-pass filter in Hertz (Definiujemy częstotliwość odcięcia dla naszego filtru dolnoprzepustowego w Hercach)
CUTOFF_FREQUENCY = 800.0

# Calculate the Nyquist frequency, which is half of the sampling rate (Obliczamy częstotliwość Nyquista, która stanowi połowę częstotliwości próbkowania)
nyquist_freq = 0.5 * sampling_rate

# Normalize the cutoff frequency relative to the Nyquist frequency as required by SciPy (Normalizujemy częstotliwość odcięcia względem częstotliwości Nyquista, co jest wymagane przez SciPy)
normalized_cutoff = CUTOFF_FREQUENCY / nyquist_freq

# Create coefficients (b, a) for a 4th-order Butterworth low-pass filter (Tworzymy współczynniki (b, a) dla filtru dolnoprzepustowego Butterwortha 4. rzędu)
b, a = signal.butter(N=4, Wn=normalized_cutoff, btype="low", analog=False)

# Apply the filter forward and backward to clear noise without phase shift (Stosujemy filtr w przód i w tył, aby usunąć szum bez przesunięcia fazowego)
filtered_signal = signal.filtfilt(b, a, noisy_signal)


# Convert the floating-point filtered signal back to 16-bit integers for WAV format (Konwertujemy przefiltrowany sygnał zmiennoprzecinkowy z powrotem na 16-bitowe liczby całkowite dla formatu WAV)
filtered_int16 = np.int16(filtered_signal * 32767)

# Save the cleaned audio array into a new output .wav file on disk (Zapisujemy tablicę oczyszczonego dźwięku do nowego wyjściowego pliku .wav na dysku)
wavfile.write(OUTPUT_FILENAME, sampling_rate, filtered_int16)


# Create a figure window with 3 separate subplots stacked vertically (Tworzymy okno figury z 3 osobnymi podwykresami ułożonymi pionowo)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

# Plot time versus clean signal on the first subplot (Rysujemy czas względem czystego sygnału na pierwszym podwykresie)
ax1.plot(time, clean_signal, label="Original Audio (Oryginalny dźwięk)", color="blue")
ax1.set_title("Original Audio Signal from .wav file / Oryginalny sygnał z pliku .wav")
ax1.grid(True)

# Plot time versus noisy signal on the second subplot (Rysujemy czas względem zaszumionego sygnału na drugim podwykresie)
ax2.plot(time, noisy_signal, label="Noisy Audio (Zaszumiony dźwięk)", color="orange")
ax2.set_title("Noisy Audio Signal (Zaszumiony dźwięk z dodatkowym szumem)")
ax2.grid(True)

# Plot time versus filtered signal on the third subplot (Rysujemy czas względem przefiltrowanego sygnału na trzecim podwykresie)
ax3.plot(time, filtered_signal, label="Filtered Audio (Przefiltrowany dźwięk)", color="green")
ax3.set_title("Filtered Audio Signal (Przefiltrowany dźwięk po usunięciu szumu)")
ax3.grid(True)

# Automatically adjust spacing between subplots (Automatycznie dopasowujemy odstępy między podwykresami)
plt.tight_layout()

# Display the generated charts in a pop-up window (Wyświetlamy wygenerowane wykresy w wyskakującym oknie)
plt.show()


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