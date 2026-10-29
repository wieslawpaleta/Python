# TASK 2.  

# Using data format from first task, write function `task2`,  
# which will count weighted average (one number) for given key list  
# rounded to one decimal place as string.

# Assume that value column is integer.

# Weight is:
# - `10` if value is odd
# - `20` if value is even

# **Example call:**

# task2(
#     [
#         {'side': 'IN', 'currency': 'PLN'},
#         {'side': 'OUT', 'currency': 'EUR'},
#     ], 
#     'side,currency,value\nIN,PLN,1\nIN,EUR,2\nOUT,ANY,3'
# ) 
#
# Rozwiązanie
# W poniższym formularzu zamieść wynik task2 dla pliku z danymi pod linkiem find_match_average_v2.dat.lz4 oraz kluczy

#  [
#   {'a': 862984, 'b': 29105, 'c': 605280, 'd': 678194, 'e': 302120},
#   {'a': 20226, 'b': 781899, 'c': 186952, 'd': 506894, 'e': 325696}
#  ]

# część komentarzy zostały napisane dla 
# search = [
#    {'side': 'IN', 'currency': 'PLN'},
#    {'side': 'IN', 'currency': 'EUR'},
# i
# data = 'side,currency,value\nIN,PLN,1\nIN,EUR,2\nOUT,ANY,3'
# ponieważ jest to prostsze rozwiązanie

_data_cache = {} # tu przechowuje się to, co zwróci "if data in _data_cache:" + jest to zmienna prywatna, bo (_)

def get_parsed_data(data):
    # jeśli ten tekst był już kiedyś przeanalizowany, od razu zwracamy gotowy wynik z pamięci
    if data in _data_cache: # jeśli data znajduje się w _data_cache, to
        return _data_cache[data] # zwracamy już gotowe, przetworzone dane (header, rows) przypisane do tego klucza 'data'

    # jeśli widzimy te dane pierwszy raz, wykonujemy operacje niżej
    data1 = data.split("\n") # Pozbywamy się \n i tworzą się listy "side,currency,value", "IN,PLN,1", "IN,EUR,2", "OUT,ANY,3"
    data2 = [[element.strip() for element in x.split(",")] for x in data1 if x.strip()] 
    # pozbywamy się przecinków, if x.strip() usuwa białe linie i tworzymy liste z listami 
    # [['side', 'currency', 'value'], ['IN', 'PLN', '1'], ['IN', 'EUR', '2'], ['OUT', 'ANY', '3']]
    # przy czym "[element.strip() for element in x.split(",")]" usuwa niewidzialne znaki np. "\r"

    header = data2[0] # tu oddzielamy ['side', 'currency', 'value'] od data2, żeby potem porównać nagłówki
    rows = data2[1:] # tu oddzielamy [['IN', 'PLN', '1'], ['IN', 'EUR', '2'], ['OUT', 'ANY', '3']] od data2, żeby potem przeszły iterację i porównanie z wartościami z search

    
    _data_cache[data] = (header, rows) # zapamiętujemy wynik w cache dla przyszłych wywołań
    return header, rows # zwracamy header i rows, które zostaną pobrane przez task1

def task2(search, data):
    header, rows = get_parsed_data(data) # pobieramy z get_parsed_data header i rows

    header1 = set(header) - {'value'} # tworzymy zbiór, ponieważ elementy we wnętrzu są unikatowe, nie mają stałego miejsca i porównanie zależy tylko od samych elementów, a nie indeksu. Value usuwamy, ponieważ tego nie ma w header 2
    header2 = set(search[0].keys()) # # wyciągamy klucze z search, które tworzą zbiór, który możemy porównać z header 1, ale tutaj korzystamy ze słownika pod indeksem 0

    if header2 != header1: # tu porównujemy header2 z header1 w if JEŚLI NIE SĄ równe. Jeśli nie sa równe, to program podnosi KeyError
        raise KeyError("Key mismatch") # Podniesienie KeyError, jeśli header2 nie jest równy header1

    total_weighted_value = 0 # to suma iloczynów wartości i ich wag, a zero jest wyjściową wartością tej zmiennej, ponieważ nie znaleźliśmy jeszcze żadnego pasującego wiersza.
    total_weights = 0 # to jest suma wszystkich wag, a zero jest wyjściową wartością tej zmiennej, ponieważ nie znaleźliśmy jeszcze żadnego pasująćego wiersza.

    search_indices = {key: header.index(key) for key in search[0].keys()} # tutaj robimy iterację dla kluczy w słowniku {'side': 'IN', 'currency': 'PLN'}, który znajduję się pod indeksem 0, wyświetlając klucz i indeks klucza w header
    value_index = header.index('value') # bierzemy index, który należy do 'value' w zmiennej header, która jest listą ['side', 'currency', 'value']

    for search1 in search:
        # pętla rozdziela listę search na:
        # {'side': 'IN', 'currency': 'PLN'}
        # {'side': 'IN', 'currency': 'EUR'}
        # jako search1 <class 'dict'>
        lookup_criteria = [(search_indices[k], v) for k, v in search1.items()] 
        # tutaj pętla for robi ze słowników 
        # {'side': 'IN', 'currency': 'PLN'} 
        # {'side': 'IN', 'currency': 'EUR'}
        # listę krotek, gdzie zamiast nazwy klucz jest jego indeks, który ma w header
        # [(0, 'IN'), (1, 'PLN')]
        # [(0, 'IN'), (1, 'EUR')]
        # zapisujemy to jako zmienną lookup_criteria. Czyli: dla pobranych kluczy i wartości słownikowych z search1 (items), program sprawdza jaki indeks ma dany klucz w "search_indices" i paruje go z wartością "v".
        for row in rows:
            # tutaj iterują się elementy listy [['IN', 'PLN', '1'], ['IN', 'EUR', '2'], ['OUT', 'ANY', '3']] do: 
            # ['IN', 'PLN', '1'] 
            # ['IN', 'EUR', '2'] 
            # ['OUT', 'ANY', '3']
            match_found = True # tutaj wzięty element z listy rows dostaje match_found True i idzie do sprawdzenia w wewnętrznej pętli for

            # Błyskawiczna weryfikacja wiersza na podstawie przygotowanych indeksów
            for col_idx, expected_value in lookup_criteria: 
                # tutaj iterację po zmiennej 'lookup_criteria', która zawiera np:
                # [(0, 862984), (1, 29105), (2, 605280), (3, 678194), (4, 302120)]
                # [(0, 20226), (1, 781899), (2, 186952), (3, 506894), (4, 325696)]
                # i czyni np. 0, 20226, czyli rozbija te listy na elementy np. 0 20226 dzięki czemu
                if row[col_idx] != str(expected_value): # tutaj jeśli row[0] nie jest równe stringowi(20226) to zwraca False, porównujemy string i liczbą przeksztalconą w string
                    match_found = False # tutaj wzięty element z list rows, jeśli nie spełnia warunku, dostaje wartość False i zostaje odrzucony
                    break # przerywamy działanie pętli "for col_idx, expected_value in lookup_criteria", jeśli jest False

            if match_found: 
                # jeśli match_found znajdzie dopasowanie, czyli jest True, to zwraca sumę iloczynów wartości 
                # (czyli znajduje pasujący wiersz, bierze jego wartość, mnoży ją przez odpowiednią wagę i dodaje do total_weighted_value)
                # i sumę wszystkich wag, czyli dla każdego znalezionego dopasowania dodaje odpowiednią wagę
                value_index = header.index('value') # tu pobieramy index, pod którym znajduje się 'value' w header i zapisujemy w zmiennej value_index
                val = int(row[value_index]) # tutaj tworzy się zmienna val z liczbą całkowitą, którą jest wartość dla row pod indexem odpowiadającym value_index

                if val % 2 != 0: # tutaj tworzymy if z val i modulo %, czyli jeśli reszta z dzielenia przez 2 nie jest równa 0 wtedy:
                    weight = 10  # waga wynosi 10
                else:            # inaczej
                    weight = 20  # 20, czyli jeśli to reszta z tego dzielenia wynosi 0

                total_weighted_value += val * weight # czyli total_weighted_value = total_weighted_value + val * weight, czyli iloczyn wartości i wagi, który zostaje dodany do total_weighted_value
                total_weights += weight # tutaj dodajemy wagę do total_weights, czyli total_weights = total_weights + weight
                

    if total_weights == 0: # if, czyli założenie, co się stanie, kiedy suma wag będzie wynosić 0
        return '-1' # jeśli total_weights wynosi 0, to zwraca -1
        

    weighted_average = total_weighted_value / total_weights # oblicza średnią ważoną
    return f"{weighted_average:.1f}" # zwraca średnią ważoną z dokładnością do jednego miejsca po przecinku

print("Pobieranie pliku 'find_match_average_v2.dat'...") # program wyświela informacje dla użytkownika, że zostaje pobrany plik, który został w zmiennej "path"

path = r"C:\Users\NazwaUżytkownika\Downloads\Program\Python\ZadanieRekrutacyjen\find_match_average_v2.dat" # wczytuję plik rekrutacyjny

try: #próbujemy wczytać zawartość 
    print("Wczytywanie pliku tekstowego...") # komunikujemy użytkownikowi, że wczytujemy plik rekrutracyjny
    with open(path, "r", encoding="utf-8") as f: # otwieramy rozpakowany plik lokalny z kodowaniem utf-8, który zapisaliśmy w "path", "r" to jest odczyt i zapisujemy jako f
        data_from_file = f.read()  # żeby potem odczytać to f i zapisać jako data_from_file
    
    # Klucze z Twojego formularza rekrutacyjnego
    search_keys = [ # tutaj znajduje się lista ze słownikami, które trzeba znaleźć w "data_from_file" i dokonać obliczeń
      {'a': 862984, 'b': 29105, 'c': 605280, 'd': 678194, 'e': 302120},
      {'a': 20226, 'b': 781899, 'c': 186952, 'd': 506894, 'e': 325696}
    ]

    print("Obliczanie wyniku...") # informujemy użytkownika, że program liczy wynik
    wynik_koncowy = task2(search_keys, data_from_file) # zmienna "wynik_koncowy" wywołuje funkcję "task2" za pomocą "search_keys" i "data_from_file"
    
    print("\n========================================") # dekoracja
    print(f" WYNIK DO WPISANIA W FORMULARZU: {wynik_koncowy}") #ostateczny wynik
    print("========================================\n") #dekoracja

except Exception as e: # jeśli coś poszło nie tak, to wyświetlamy komunikat
    print(f"Wystąpił błąd podczas wczytywania pliku: {e}") # wyświetlamy komunikat dla użytkownika o błędzie
