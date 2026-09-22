#W tym miejscu można przeliterować wybrane słowo.
import główne_okno


def przeliteruj():
    print("\nPRZELITERUJ SŁOWO!\n")
    while True:
        print("-" * 10)
        print("Dostępne opcje:\n")
        print("1) Wpisz słowo, które chcesz przeliterować,")
        print("2) Wpisz \"Pwrt\", żeby wrócić do głównego okna,")
        print("3) Wpisz \"Wsc\", żeby zakończyć działanie programu.")
        print("-" * 10)
        rozkład = input("Co zamierzasz? ")


        if rozkład.lower() == "pwrt":
            print("\nNo to wracamy!")
            return główne_okno.główne_okno()
        
        
        elif rozkład.lower() == "wsc":
            print("\nDo zobaczenia!")
            exit()


        elif rozkład.isalpha():
            print("")    
            for x in rozkład:
                print(x)
            print("")
 
        else:
            print("Spróbuj jeszcze raz.")
        