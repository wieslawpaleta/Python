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
#Here are results

lbl_wynik = tk.Label(window, text="Choose your figure", font=("Arial", 12))
lbl_wynik.pack(pady=10)


#Classic formula for the area of triangle

image_path = os.path.join(current_dir, "Images/StandardTriangle.jpg")
pil_image = Image.open(image_path)
resized_image_areaStTriang = pil_image.resize((150, 50), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(resized_image_areaStTriang)

btn = tk.Button(window, image=icon, command=lambda: count_areaStTriang())
btn.pack(pady=1)

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

def count_areaStRec():
    triangle = figure_classes_area.StandardRectangle()
    result = triangle.areaStRec()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of circle

image_path_areaStCirc = os.path.join(current_dir, "Images/StandardCircle.jpg")
pil_image_areaStCirc = Image.open(image_path_areaStCirc)
resized_image_areaStCirc = pil_image_areaStCirc.resize((150, 50), Image.Resampling.LANCZOS)
icon_areaStCirc = ImageTk.PhotoImage(resized_image_areaStCirc)

btn_areaStCirc = tk.Button(window, image=icon_areaStCirc, command=lambda: count_areaStCirc())
btn_areaStCirc.pack(pady=1)

def count_areaStCirc():
    circle = figure_classes_area.StandardCircle()
    result = circle.areaStCirc()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of rhombus

image_path_areaStRhom = os.path.join(current_dir, "Images/StandardRhombus.jpg")
pil_image_areaStRhom = Image.open(image_path_areaStRhom)
resized_image_areaStRhom = pil_image_areaStRhom.resize((150, 50), Image.Resampling.LANCZOS)
icon_areaStRhom = ImageTk.PhotoImage(resized_image_areaStRhom)

btn_areaStRhom = tk.Button(window, image=icon_areaStRhom, command=lambda: count_areaStRhom())
btn_areaStRhom.pack(pady=1)

def count_areaStRhom():
    circle = figure_classes_area.StandardRhombus()
    result = circle.areaStRhom()
    
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