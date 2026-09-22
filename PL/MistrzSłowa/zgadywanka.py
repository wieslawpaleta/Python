#Import potrzebnych elementów.
import random
from słownik_zgadywanka import zbiór_słów
import główne_okno
import lista
import losowanie


#Tu zaczyna się gra.
def zgadnij():

    
    print("\nZgadnij słowo!\n")


    słowo = random.choice(zbiór_słów).lower()


    #Na wypadek testów.
    #print(słowo)
    tajemnicze_słowo = słowo
    zakreskowane_słowo = ["_"] * len(tajemnicze_słowo)


    próby = 0
    max_prób = len(tajemnicze_słowo) * 3


    #Pętla zgadywania słowa z możliwością powrótu do głównego menu oraz zakończenia działania programu.
    while próby < max_prób:

        print("-" * 10)
        print("Dostępne opcje:\n")
        print("1) Zgadnij literę lub słowo,")
        print("2) Wpisz \"Powrót\", żeby wrócić do głównego okna,")
        print("3) Wpisz \"Wyjście\", żeby zakończyć działanie programu.")
        print("-" * 10)
        próba = input(f"(Próba {próby + 1}/{max_prób}) co zamierzasz: ").lower()


        if próba.lower() == "wyjście":
            print("\nDo zobaczenia!")
            exit()

            
        if próba.lower() == "powrót":
            print("\nNo to wracamy!")
            return główne_okno.główne_okno()
            

        if próba == tajemnicze_słowo:
            print("\nBrawo! Odgadłeś słowo!\n")
            break


        if len(próba) != 1 or not próba.isalpha():
            print("\nPodaj jedną literę albo poprawne słowo (bez cyfr i symboli)!")
            próby += 1
            continue

        

        for i in range(len(tajemnicze_słowo)):
            if próba == tajemnicze_słowo[i]:
                zakreskowane_słowo[i] = próba        
            

        wynik_wyświetlany = " ".join(zakreskowane_słowo)
        print("\nAktualny stan słowa:", wynik_wyświetlany)
        print()
        
        if "_" not in zakreskowane_słowo:
            print("\nGratulacje! Odgadłeś słowo!\n")
            break


        próby += 1


    else:
        print(f"Przegrałeś, a tu słowo, którego szukałeś: {tajemnicze_słowo} \n")


    #Pętła wyboru trybów.
    while True:   


        print("Wpisz 'Zgadywanka', aby raz jeszcze zgadnąć słowo.")
        print("Wpisz 'Losowanie', aby przejść do trybu losowania.")
        print("Wpisz 'Lista', aby przejść do trybu listy.")
        print("Wpisz 'Powrót', aby wrócić do głównego menu.")
        print("Wpisz 'Wyjście', aby zakończyć działanie programu.")               
        сozrobić = input("Co chcesz teraz zrobić?: ").strip().lower()  

              
        if сozrobić == "zgadywanka":
            return zgadnij()

        
        elif сozrobić == "lista":
            return lista.wybierz_słowo()

        
        elif сozrobić == "losowanie":
            return losowanie.początek_losowania()

        
        elif сozrobić == "powrót":
            print("\nNo to wracamy!")
            return główne_okno.główne_okno()

        
        elif сozrobić == "wyjście":
            print("\nDo zobaczenia!")
            exit()


        else:
            print("\nSpróbuj jeszcze raz.\n")

     



