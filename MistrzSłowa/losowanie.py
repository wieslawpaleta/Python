#Tutaj znajdują się potrzebne importy.
import random
from słowniki_lista_losowanie import słowniki
import główne_okno
import lista
import zgadywanka


#Tutaj dokonuje się wybór języka.
def początek_losowania():


    while True:
        print("\nWylosuj słowo!\n")
        print("-" * 10)
        print("Dostępne opcje:\n")
        print("1) Wybierz język")
        print("2) \"Powrót\"")
        print("3) \"Wyjście\"")
        print("-" * 10)


        dostępne_języki = """angielski (en), rosyjski (ru), hiszpański (es), francuski (fr), niemiecki (de)
arabski (ar), chiński (ch), koreański (kr), japoński (jp), tajski (tj)"""   

       
        print("DOSTĘPNE JĘZYKI:\n")
        print(dostępne_języki)
        print("-" * 10)


        while True:    


            język = input("Co zamierzasz? ").strip().lower()  


            if język == "en":
                print("\nWybrałeś język angielski.")
                return losowanie_słowa(język)

            
            elif język == "ru":
                print("\nWybrałeś język rosyjski.")
                return losowanie_słowa(język)

            
            elif język == "es":
                print("\nWybrałeś język hiszpański.")
                return losowanie_słowa(język)

            
            elif język == "fr":
                print("\nWybrałeś język francuski.")
                return losowanie_słowa(język)

            
            elif język == "de":
                print("\nWybrałeś język niemiecki.")
                return losowanie_słowa(język)

            
            elif język == "ar":
                print("\nWybrałeś język arabski.")
                return losowanie_słowa(język)

            
            elif język == "ch":
                print("\nWybrałeś język chiński.")
                return losowanie_słowa(język)

            
            elif język == "kr":
                print("\nWybrałeś język koreański.")
                return losowanie_słowa(język)

            
            elif język == "jp":
                print("\nWybrałeś język japoński.")
                return losowanie_słowa(język)

            
            elif język == "tj":
                print("\nWybrałeś język tajski.")
                return losowanie_słowa(język)
            
            
            elif język == "powrót":
                print("\nNo to wracamy!")
                return główne_okno.główne_okno()


            elif język == "wyjście":
                print("\nDo zobaczenia!")
                exit()

            
            else:
                print("\nWybrany język jest nieobsługiwany.\n")
                

#Tutaj dokonuje się losowanie słowa.                
def losowanie_słowa(język):

        
        while True:


            gamba = input("\nCzy chcesz wylosować słowo? (tak/nie): ").strip().lower()


            if gamba == "tak":
                maszyna = random.randint(1, 100)
                if 1 <= maszyna <= 100:
                    słowo_obce = słowniki[język][maszyna - 1]
                    słowo_polskie = słowniki["pl"][maszyna - 1]
                    print("\nWylosowane słowo to: \n" + słowo_obce + "-" + słowo_polskie)


            #Tutaj można wybrać tryb, wrócić do głównego okna lub wyjść z programu.
            elif gamba == "nie":


                print("\nWpisz 'Losowanie', aby rozpocząć nowe losowanie.")    
                print("Wpisz 'Lista', aby przejść do trybu listy.")
                print("Wpisz 'Zgadywanka', aby przejść do trybu zgadywanki.")
                print("Wpisz 'Powrót', aby wrócić do głównego menu.")
                print("Wpisz 'Wyjście', aby zakończyć działanie programu.")
                lufa_pytanie = input("Co chcesz teraz zrobić?: ").strip().lower()


                if lufa_pytanie == "losowanie":
                    return początek_losowania()
               

                elif lufa_pytanie == "lista":
                    return lista.wybierz_słowo()

                
                elif lufa_pytanie == "zgadywanka":
                    return zgadywanka.zgadnij()

                
                elif lufa_pytanie == "powrót":
                    print("\nNo to wracamy!")
                    return główne_okno.główne_okno()

                
                elif lufa_pytanie == "wyjście":
                    print("\nDo zobaczenia!")
                    exit()
            
                
                else:
                    print("\nNiepoprawna opcja. Spróbuj ponownie.\n")


            else:
                print("\nNiepoprawna odpowiedź. Wpisz 'tak' lub 'nie'.\n")
        