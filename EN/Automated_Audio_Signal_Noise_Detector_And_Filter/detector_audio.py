# Import the NumPy library for numerical operations and matrix calculations (Importujemy bibliotekę NumPy do operacji numerycznych i obliczeń na macierzach/tablicach)
import numpy as np

# Import the signal module from SciPy to perform filtering and signal analysis (Importujemy moduł 'signal' z biblioteki SciPy do filtrowania i analizy sygnałów)
from scipy import signal

# Import the wavfile module from SciPy to read and write .wav audio files (Importujemy moduł 'wavfile' z SciPy do odczytu i zapisu plików dźwiękowych .wav)
from scipy.io import wavfile

# Import the pyplot module from matplotlib to create visual charts and graphs (Importujemy moduł pyplot z biblioteki matplotlib, żeby tworzyć wizualne wykresy i grafiki)
import matplotlib.pyplot as plt


# Define the filename of our input audio file to load (Definiujemy nazwę pliku naszego wejściowego pliku dźwiękowego do wczytania)
INPUT_FILENAME = r"C:\Users\NazwaUżytkownika\Downloads\Program\Python\Projects EN\Automated_Audio_Signal_Noise_Detector_And_Filter\modemsciana.wav"

# Define the filename where our cleaned output audio will be saved (Definiujemy nazwę pliku, w którym zapiszemy nasz oczyszczony wyjściowy dźwięk)
OUTPUT_FILENAME = "output_audio.wav"


# Read the sampling rate and raw audio data from the .wav file (Odczytujemy częstotliwość próbkowania oraz surowe dane dźwiękowe z pliku .wav)
sampling_rate, audio_data = wavfile.read(INPUT_FILENAME)

# Check if the audio file has two channels (stereo) and convert it to mono by averaging them (Sprawdzamy, czy plik dźwiękowy ma dwa kanały (stereo) i konwertujemy go do mono poprzez uśrednienie ich)
if len(audio_data.shape) > 1:
    audio_data = np.mean(audio_data, axis=1)

# Normalize integer audio data to floating-point values between -1.0 and 1.0 (Normalizujemy całkowitoliczbowe dane dźwiękowe do wartości zmiennoprzecinkowych z zakresu od -1.0 do 1.0)
audio_data = audio_data / np.max(np.abs(audio_data))

# Calculate the total duration of the loaded audio file in seconds (Obliczamy całkowity czas trwania wczytanego pliku dźwiękowego w sekundach)
DURATION = len(audio_data) / sampling_rate

# Create an array of time steps for each sample based on the sampling rate (Tworzymy tablicę kroków czasowych dla każdej próbki na podstawie częstotliwości próbkowania)
time = np.arange(0, len(audio_data)) / sampling_rate


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