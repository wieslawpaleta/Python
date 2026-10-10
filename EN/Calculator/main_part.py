import os
import math
import figure_classes_area
import figure_classes_volume
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = Tk()

window.title("My Calculator")
window.geometry("720x480")
window.minsize(480, 360)


current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, "favicon.ico")
window.iconbitmap(icon_path)


#Buttons with images in order to 

#Classic formula for the area of triangle

image_path = os.path.join(current_dir, "Images/StandardTriangle.jpg")
pil_image = Image.open(image_path)
resized_image_areaStTriang = pil_image.resize((150, 50), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(resized_image_areaStTriang)

btn = tk.Button(window, image=icon, command=lambda: count_areaStTriang())
btn.pack(pady=1)

lbl_wynik = tk.Label(window, text="", font=("Arial", 12))
lbl_wynik.pack(pady=5)

def count_areaStTriang():
    triangle = figure_classes_area.StandardTriangle()
    result = triangle.areaStTriang()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of rectangle

image_path_areaStRec = os.path.join(current_dir, "Images/StandardRectangle.jpg")
pil_image_areaStRec = Image.open(image_path_areaStRec)
resized_image_areaStRec = pil_image_areaStRec.resize((150, 50), Image.Resampling.LANCZOS)
icon_areaStRec = ImageTk.PhotoImage(resized_image_areaStRec)

btn_areaStRec = tk.Button(window, image=icon_areaStRec, command=lambda: count_areaStRec())
btn_areaStRec.pack(pady=1)

lbl_wynik_areaStRec = tk.Label(window, text="", font=("Arial", 12))
lbl_wynik_areaStRec.pack(pady=6)

def count_areaStRec():
    triangle = figure_classes_area.StandardRectangle()
    result = triangle.areaStRec()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

window.config(background="#FFFFFF")


frame = Frame(window, bg='#ffffff')


standard_triangle_button = Button(frame)
frame.pack(expand=YES)
window.mainloop()