#wersja 4.0
#Tutaj znajdują się potrzebne importy.
import losowanie
import główne_okno
from słowniki_lista_losowanie import słowniki
import zgadywanka


#Tutaj dokonuje się wybór języka.    
def wybierz_słowo():


    while True:        
        print("\nStwórz listę!\n")
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


            język = input("Co zamierasz? ").strip().lower()


            if język == "en":
                print("\nWybrałeś język angielski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "ru":
                print("\nWybrałeś język rosyjski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "es":
                print("\nWybrałeś język hiszpański.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "fr":
                print("\nWybrałeś język francuski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "de":
                print("\nWybrałeś język niemiecki.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "ar":
                print("\nWybrałeś język arabski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "ch":
                print("\nWybrałeś język chiński.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "kr":
                print("\nWybrałeś język koreański.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "jp":
                print("\nWybrałeś język japoński.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "tj":
                print("\nWybrałeś język tajski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "powrót":
                print("\nNo to wracamy!")
                return główne_okno.główne_okno()   


            elif język == "wyjście":
                print("\nDo zobaczenia!")
                exit()   

            
            else:
                print("\nWybrany język jest nieobsługiwany.\n")
                

#Tutaj tworzy się lista.         
def generuj_listę_słów(język, a, b, c):

        
        while True:

            
            try:


                print("\nWybierz pierwszą liczbę od 1 do 100: ")
                a = int(input())
                print("Wybierz drugą liczbę od 1 do 100 (musi być większa niż pierwsza): ")
                b = int(input()) 
                print("Wybierz trzecią liczbę od 1 do 3: ")
                c = int(input())    


                if 1 <= a <= 100 and 1 <= b <= 100 and a < b and 1 <= c <= 3:
                    print("\nTwoja lista słów to: ")
                    for i in range(a - 1, b, c):
                        słowo_obce = słowniki[język][i]
                        słowo_pl = słowniki["pl"][i]
                        print(słowo_obce, "-", słowo_pl)


                    #Tutaj dokonuje się wybór o przyszłości.    
                    while True:     


                        print("\nWpisz 'Lista', aby stworzyć nową listę.")
                        print("Wpisz 'Losowanie', aby przejść do trybu losowania.")
                        print("Wpisz 'Zgadywanka', aby przejść do trybu zgadywania.")
                        print("Wpisz 'Powrót', aby wrócić do głównego menu.")
                        print("Wpisz 'Wyjście', aby zakończyć działanie programu.")                      
                        сozrobić = input("Co chcesz teraz zrobić?: ").strip().lower()                        


                        if сozrobić == "lista":
                            return wybierz_słowo()

                        
                        elif сozrobić == "losowanie":
                            return losowanie.początek_losowania()

                        
                        elif сozrobić == "zgadywanka":
                            return zgadywanka.zgadnij()

                        
                        elif сozrobić == "powrót":
                            print("\nNo to wracamy!")
                            return główne_okno.główne_okno()

                        
                        elif сozrobić == "wyjście":
                            print("\nDo zobaczenia!")
                            exit()


                        else:
                            print("Spróbuj jeszcze raz.")


                else:
                    print("Wprowadzone liczby nie spełniają warunków.")


            except ValueError:
                print("Błąd! Musisz wpisać liczby całkowite. Spróbuj ponownie.\n")