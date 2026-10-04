import math
import figure_classes_area
import figure_classes_volume


def główne_okno():
    while True:

        print("Hello!")

        chooseType = input("Are you looking for area or volume? ")
        chooseFigure = input("\nChoose your figure: ")
        if chooseType and chooseFigure:
            fusionAreaVolume = "figure_classes_" + chooseType
            fusionFigure =
            return fusionAreaVolume
    
        else: 
            return "kiełbasa"


        chooseFormula = input("Choose your formula: ")


        print(f"The {chooseType} of your {chooseFigure} is: ")



if __name__ == "__main__":
    główne_okno() 
     