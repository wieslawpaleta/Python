#To jest główne okno, w którym użytkownik wybiera tryb działania programu.
#Tutaj znajdują się potrzebne importy.
import losowanie
import lista
import zgadywanka
import edytor_słowników
import przeliterowanie

#Główne okno wyboru.
def główne_okno():


    print("\nCześć!\n")
    print("-" * 10)
    print("Dostępne tryby do wyboru:\n")
    print("1) \"Losowanie\"")
    print("2) \"Lista\"")
    print("3) \"Zgadywanka\"")
    print("4) \"Edytor słowników\"")
    print("5) \"Przeliterowanie\"")
    print("6) \"Wyjście\"")
    print("-" * 10)
    tryb = input("Co zamierzasz? ")


    while True:


        try:
            if tryb.lower() == "losowanie":
                return losowanie.początek_losowania()  

             
            elif tryb.lower() == "lista":
                return lista.wybierz_słowo()

            
            elif tryb.lower() == "zgadywanka":
                return zgadywanka.zgadnij()


            elif tryb.lower() == "edytor słowników":
                return edytor_słowników.edytor_zbioru()


            elif tryb.lower() == "przeliterowanie":
                return przeliterowanie.przeliteruj()

            
            elif tryb.lower() == "wyjście":
                print("\nDo zobaczenia!")
                exit()

                
            else:
                print("\nMasz ostatnie ostrzeżenie w tej chwili,\nmasz ostatnie ostrzeżenie!\n")
                tryb = input("Wybierz i wpisz nazwę jednego z trybów: \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")


        except ValueError:
            print("\nPosłuchaj dzieciaku!\n")


#Dzięki temu można uruchomić program.
if __name__ == "__main__":
    główne_okno() 
     


