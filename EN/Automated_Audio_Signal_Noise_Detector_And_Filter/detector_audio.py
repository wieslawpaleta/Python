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
        # Fix the random seed to ensure consistent noise generation across runs (Ustawiamy ziarno losowości, aby zapewnić spójne generowanie szumu przy kolejnych uruchomieniach)
        np.random.seed(42)

        # Generate high-frequency sinusoidal noise to simulate interference (Generujemy szum sinusoidalny o wysokiej częstotliwości, aby symulować zakłócenia)
        noise_high_freq = 0.3 * np.sin(2 * np.pi * 1500 * self.time)

        # Generate random white noise using a normal Gaussian distribution (Generujemy losowy szum biały, używając normalnego rozkładu Gaussa)
        random_white_noise = np.random.normal(0, 0.1, len(self.time))

        # Add the noise components to the original clean audio signal (Dodajemy elementy szumu do oryginalnego czystego sygnału dźwiękowego)
        self.noisy_signal = self.audio_data + noise_high_freq + random_white_noise

    # Define a method to filter out noise using a Butterworth low-pass filter (Definiujemy metodę do odfiltrowywania szumu za pomocą dolnoprzepustowego filtru Butterwortha)
    def filter_signal(self):
        # Calculate the Nyquist frequency, which is half of the sampling rate (Obliczamy częstotliwość Nyquista, która stanowi połowę częstotliwości próbkowania)
        nyquist_freq = 0.5 * self.sampling_rate

        # Normalize the custom cutoff frequency relative to the Nyquist frequency (Normalizujemy niestandardową częstotliwość odcięcia względem częstotliwości Nyquista)
        normalized_cutoff = self.cutoff_freq / nyquist_freq

        # Create filter coefficients (b, a) for a 4th-order Butterworth low-pass filter (Tworzymy współczynniki filtra (b, a) dla filtru dolnoprzepustowego Butterwortha 4. rzędu)
        b, a = signal.butter(
            N=4, Wn=normalized_cutoff, btype="low", analog=False
        )

        # Apply the filter forward and backward to remove noise without phase delay (Stosujemy filtr w przód i w tył, aby usunąć szum bez opóźnienia fazowego)
        self.filtered_signal = signal.filtfilt(b, a, self.noisy_signal)

    # Define a method to save the cleaned audio signal back to disk as a .wav file (Definiujemy metodę do zapisywania oczyszczonego sygnału dźwiękowego z powrotem na dysk jako plik .wav)
    def save_audio(self):
        # Convert floating-point signal back to 16-bit signed integers for WAV format (Konwertujemy sygnał zmiennoprzecinkowy z powrotem na 16-bitowe liczby całkowite ze znakiem dla formatu WAV)
        filtered_int16 = np.int16(self.filtered_signal * 32767)

        # Write the processed audio data into the specified output filename (Zapisujemy przetworzone dane dźwiękowe do wskazanej nazwy pliku wyjściowego)
        wavfile.write(self.output_file, self.sampling_rate, filtered_int16)

    # Define a method to display comparison graphs using Matplotlib (Definiujemy metodę do wyświetlania wykresów porównawczych za pomocą biblioteki Matplotlib)
    def plot_signals(self):
        # Create a figure window containing 3 vertically stacked subplots (Tworzymy okno figury zawierające 3 ułożone pionowo podwykresy)
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

        # Plot time versus original clean audio on the first subplot (Rysujemy czas względem oryginalnego czystego dźwięku na pierwszym podwykresie)
        ax1.plot(self.time, self.audio_data, color="blue")
        ax1.set_title("Original Audio Signal / Oryginalny sygnał dźwiękowy")
        ax1.grid(True)

        # Plot time versus noisy audio on the second subplot (Rysujemy czas względem zaszumionego dźwięku na drugim podwykresie)
        ax2.plot(self.time, self.noisy_signal, color="orange")
        ax2.set_title("Noisy Audio Signal / Zaszumiony sygnał dźwiękowy")
        ax2.grid(True)

        # Plot time versus filtered audio on the third subplot (Rysujemy czas względem przefiltrowanego dźwięku na trzecim podwykresie)
        ax3.plot(self.time, self.filtered_signal, color="green")
        ax3.set_title("Filtered Audio Signal / Przefiltrowany sygnał dźwiękowy")
        ax3.grid(True)

        # Adjust subplot layouts automatically so they don't overlap (Automatycznie dostosowujemy układy podwykresów, żeby na siebie nie nachodziły)
        plt.tight_layout()

        # Render and open the interactive chart window on screen (Renderujemy i otwieramy interaktywne okno wykresu na ekranie)
        plt.show()

    # Define a method to evaluate and print performance metrics (Definiujemy metodę do obliczania i wypisywania wskaźników wydajności)
    def evaluate(self):
        # Calculate Mean Squared Error between clean audio and noisy audio (Obliczamy błąd średniokwadratowy między czystym dźwiękiem a zaszumionym dźwiękiem)
        noisy_mse = np.mean((self.audio_data - self.noisy_signal) ** 2)

        # Calculate Mean Squared Error between clean audio and filtered audio (Obliczamy błąd średniokwadratowy między czystym dźwiękiem a przefiltrowanym dźwiękiem)
        filtered_mse = np.mean((self.audio_data - self.filtered_signal) ** 2)

        # Print the noise error value to the console (Wyświetlamy wartość błędu szumu w konsoli)
        print(f"Noise Signal MSE (Błąd zaszumionego sygnału): {noisy_mse:.4f}")

        # Print the filtered error value to the console (Wyświetlamy wartość błędu przefiltrowanego w konsoli)
        print(f"Filtered Signal MSE (Błąd przefiltrowanego sygnału): {filtered_mse:.4f}")

        # Calculate percentage improvement in signal quality (Obliczamy procentową poprawę jakości sygnału)
        improvement = ((noisy_mse - filtered_mse) / noisy_mse) * 100

        # Print the overall percentage reduction improvement (Wyświetlamy ogólną procentową poprawę redukcji szumu)
        print(f"Signal Noise Reduction Improvement (Poprawa jakości sygnału): {improvement:.2f}%")


# Check if the script is being run directly from the command line (Sprawdzamy, czy skrypt jest uruchamiany bezpośrednio z wiersza poleceń)
if __name__ == "__main__":
    # Create an argument parser object to handle CLI inputs (Tworzymy obiekt parsera argumentów do obsługi wejść z CLI)
    parser = argparse.ArgumentParser(
        description="Automated Audio Signal Noise Detector & Filter (Automatyczny detektor i filtr szumów w sygnałach audio)"
    )

    # Add an argument for the input wav filename with a default value (Dodajemy argument dla wejściowej nazwy pliku wav z wartością domyślną)
    parser.add_argument(
        "--input",
        type=str,
        default= r"C:\Users\NazwaUżytkownika\Downloads\Program\Python\Projects EN\Automated_Audio_Signal_Noise_Detector_And_Filter\input_audio.wav",
        help="Path to input .wav file (Ścieżka do wejściowego pliku .wav)",
    )

    # Add an argument for the output wav filename with a default value (Dodajemy argument dla wyjściowej nazwy pliku wav z wartością domyślną)
    parser.add_argument(
        "--output",
        type=str,
        default="output_audio.wav",
        help="Path to output .wav file (Ścieżka do wyjściowego pliku .wav)",
    )

    # Add an argument for the low-pass filter cutoff frequency with a default value (Dodajemy argument dla częstotliwości odcięcia filtru dolnoprzepustowego z wartością domyślną)
    parser.add_argument(
        "--cutoff",
        type=float,
        default=800.0,
        help="Cutoff frequency in Hz (Częstotliwość odcięcia w Hz)",
    )

    # Parse all command-line arguments provided by the user (Parsujemy wszystkie argumenty wiersza poleceń podane przez użytkownika)
    args = parser.parse_args()

    # Instantiate our AudioCleaner class with parsed command-line arguments (Tworzymy instancję naszej klasy AudioCleaner z zaparsowanymi argumentami wiersza poleceń)
    cleaner = AudioCleaner(
        input_file=args.input,
        output_file=args.output,
        cutoff_freq=args.cutoff,
    )

    # Call the load method to fetch and prepare audio data (Wywołujemy metodę wczytywania, aby pobrać i przygotować dane dźwiękowe)
    cleaner.load_audio()

    # Call the add_noise method to corrupt the signal for testing (Wywołujemy metodę add_noise, aby zafałszować sygnał w celach testowych)
    cleaner.add_noise()

    # Call the filter_signal method to clean up the noise (Wywołujemy metodę filter_signal, żeby oczyścić szum)
    cleaner.filter_signal()

    # Call the save_audio method to export the resulting .wav file (Wywołujemy metodę save_audio, aby wyeksportować powstały plik .wav)
    cleaner.save_audio()

    # Call the evaluate method to print error statistics to the console (Wywołujemy metodę evaluate, aby wypisać statystyki błędów do konsoli)
    cleaner.evaluate()

    # Call the plot_signals method to render visual comparison charts (Wywołujemy metodę plot_signals, aby wyrenderować wizualne wykresy porównawcze)
    cleaner.plot_signals()