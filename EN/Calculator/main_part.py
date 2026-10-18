import os
import math
import figure_classes_area
import figure_classes_volume
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

window = Tk()

window.title("My Calculator")
window.geometry("1200x800")
window.minsize(640, 480)

current_dir1 = os.path.dirname(__file__)
image_path_background = os.path.join(current_dir1, "Images/Background.jpg")
pil_img_background = Image.open(image_path_background)
image_background = ImageTk.PhotoImage(pil_img_background)
bg_label = tk.Label(window, image=image_background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, "favicon.ico")
window.iconbitmap(icon_path)
frame = Frame(window, bg="#E6E5E5")
window_welcome = Label(window, text="CALCULATOR FOR AREAS AND VOLUMES", font=("Courrier", 40), bg="#2E5C46", fg='white')
window_welcome.grid(row=0, column=1, columnspan=5, padx=5, pady=1, sticky="nsew")


#Buttons with images in order to calculate area/volume.
#Here are results

lbl_wynik = tk.Label(window, text="Choose your figure", font=("Arial", 12), width=30, height=15, bg="lightgray")
lbl_wynik.grid(row=3, column=3, padx=5, pady=1, sticky="nsew")


#Classic formula for the area of square

image_path_areaPowSquare = os.path.join(current_dir, "Images/PowerSquare.png")
pil_image_areaPowSquare = Image.open(image_path_areaPowSquare)
resized_image_areaPowSquare = pil_image_areaPowSquare.resize((300, 100), Image.Resampling.LANCZOS)
icon_areaPowSquare = ImageTk.PhotoImage(resized_image_areaPowSquare)

btn_areaPowSquare = tk.Button(window, image=icon_areaPowSquare, command=lambda: count_areaPowSquare())
btn_areaPowSquare.grid(row=1, column=3, padx=5, pady=1, sticky="nsew")

def count_areaPowSquare():
    triangle = figure_classes_area.PowerSquare(window)
    result = triangle.areaPowSquare()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of triangle

image_path = os.path.join(current_dir, "Images/StandardTriangle.png")
pil_image = Image.open(image_path)
resized_image_areaStTriang = pil_image.resize((300, 100), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(resized_image_areaStTriang)

btn = tk.Button(window, image=icon, command=lambda: count_areaStTriang())
btn.grid(row=2, column=1, padx=5, pady=1, sticky="nsew")

def count_areaStTriang():
    triangle = figure_classes_area.StandardTriangle(window)
    result = triangle.areaStTriang()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of rectangle

image_path_areaStRec = os.path.join(current_dir, "Images/StandardRectangle.png")
pil_image_areaStRec = Image.open(image_path_areaStRec)
resized_image_areaStRec = pil_image_areaStRec.resize((300, 100), Image.Resampling.LANCZOS)
icon_areaStRec = ImageTk.PhotoImage(resized_image_areaStRec)

btn_areaStRec = tk.Button(window, image=icon_areaStRec, command=lambda: count_areaStRec())
btn_areaStRec.grid(row=2, column=2, padx=5, pady=1, sticky="nsew")

def count_areaStRec():
    rectangle = figure_classes_area.StandardRectangle(window)
    result = rectangle.areaStRec()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of circle

image_path_areaStCirc = os.path.join(current_dir, "Images/StandardCircle.png")
pil_image_areaStCirc = Image.open(image_path_areaStCirc)
resized_image_areaStCirc = pil_image_areaStCirc.resize((300, 100), Image.Resampling.LANCZOS)
icon_areaStCirc = ImageTk.PhotoImage(resized_image_areaStCirc)

btn_areaStCirc = tk.Button(window, image=icon_areaStCirc, command=lambda: count_areaStCirc())
btn_areaStCirc.grid(row=2, column=3, padx=5, pady=1, sticky="nsew")

def count_areaStCirc():
    circle = figure_classes_area.StandardCircle(window)
    result = circle.areaStCirc()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of rhombus

image_path_areaStRhom = os.path.join(current_dir, "Images/StandardRhombus.png")
pil_image_areaStRhom = Image.open(image_path_areaStRhom)
resized_image_areaStRhom = pil_image_areaStRhom.resize((300, 100), Image.Resampling.LANCZOS)
icon_areaStRhom = ImageTk.PhotoImage(resized_image_areaStRhom)

btn_areaStRhom = tk.Button(window, image=icon_areaStRhom, command=lambda: count_areaStRhom())
btn_areaStRhom.grid(row=2, column=4, padx=5, pady=1, sticky="nsew")

def count_areaStRhom():
    rhombus = figure_classes_area.StandardRhombus(window)
    result = rhombus.areaStRhom()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the area of trapezoid

image_path_areaStTrap = os.path.join(current_dir, "Images/StandardTrapezoid.png")
pil_image_areaStTrap = Image.open(image_path_areaStTrap)
resized_image_areaStTrap = pil_image_areaStTrap.resize((300, 100), Image.Resampling.LANCZOS)
icon_areaStTrap = ImageTk.PhotoImage(resized_image_areaStTrap)

btn_areaStTrap = tk.Button(window, image=icon_areaStTrap, command=lambda: count_areaStTrap())
btn_areaStTrap.grid(row=2, column=5, padx=5, pady=1, sticky="nsew")

def count_areaStTrap():
    trapezoid = figure_classes_area.StandardTrapezoid(window)
    result = trapezoid.areaStTrap()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the volume of cuboid

image_path_volumeStCubo = os.path.join(current_dir, "Images/StandardCuboid.png")
pil_image_volumeStCubo = Image.open(image_path_volumeStCubo)
resized_image_volumeStCubo = pil_image_volumeStCubo.resize((300, 100), Image.Resampling.LANCZOS)
icon_volumeStCubo = ImageTk.PhotoImage(resized_image_volumeStCubo)

btn_volumeStCubo = tk.Button(window, image=icon_volumeStCubo, command=lambda: count_volumeStCubo())
btn_volumeStCubo.grid(row=5, column=1, padx=5, pady=1, sticky="nsew")

def count_volumeStCubo():
    cuboid = figure_classes_volume.StandardCuboid(window)
    result = cuboid.volumeStCubo()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the volume of cube

image_path_volumeStCube = os.path.join(current_dir, "Images/StandardCube.png")
pil_image_volumeStCube = Image.open(image_path_volumeStCube)
resized_image_volumeStCube = pil_image_volumeStCube.resize((300, 100), Image.Resampling.LANCZOS)
icon_volumeStCube = ImageTk.PhotoImage(resized_image_volumeStCube)

btn_volumeStCube = tk.Button(window, image=icon_volumeStCube, command=lambda: count_volumeStCube())
btn_volumeStCube.grid(row=5, column=2, padx=5, pady=1, sticky="nsew")

def count_volumeStCube():
    cube = figure_classes_volume.StandardCube(window)
    result = cube.volumeStCube()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the volume of sphere

image_path_volumeStSphere = os.path.join(current_dir, "Images/StandardSphere.png")
pil_image_volumeStSphere = Image.open(image_path_volumeStSphere)
resized_image_volumeStSphere = pil_image_volumeStSphere.resize((300, 100), Image.Resampling.LANCZOS)
icon_volumeStSphere = ImageTk.PhotoImage(resized_image_volumeStSphere)

btn_volumeStSphere = tk.Button(window, image=icon_volumeStSphere, command=lambda: count_volumeStSphere())
btn_volumeStSphere.grid(row=5, column=3, padx=5, pady=1, sticky="nsew")

def count_volumeStSphere():
    cube = figure_classes_volume.StandardSphere(window)
    result = cube.volumeStSphere()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the volume of cylinder

image_path_volumeStCylinder = os.path.join(current_dir, "Images/StandardCylinder.png")
pil_image_volumeStCylinder = Image.open(image_path_volumeStCylinder)
resized_image_volumeStCylinder = pil_image_volumeStCylinder.resize((300, 100), Image.Resampling.LANCZOS)
icon_volumeStCylinder = ImageTk.PhotoImage(resized_image_volumeStCylinder)

btn_volumeStCylinder = tk.Button(window, image=icon_volumeStCylinder, command=lambda: count_volumeStCylinder())
btn_volumeStCylinder.grid(row=5, column=4, padx=5, pady=1, sticky="nsew")

def count_volumeStCylinder():
    cube = figure_classes_volume.StandardCylinder(window)
    result = cube.volumeStCylinder()
    
    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#Classic formula for the volume of cone

image_path_volumeStCone = os.path.join(current_dir, "Images/StandardCone.png")
pil_image_volumeStCone = Image.open(image_path_volumeStCone)
resized_image_volumeStCone = pil_image_volumeStCone.resize((300, 100), Image.Resampling.LANCZOS)
icon_volumeStCone = ImageTk.PhotoImage(resized_image_volumeStCone)

btn_volumeStCone = tk.Button(window, image=icon_volumeStCone, command=lambda: count_volumeStCone())
btn_volumeStCone.grid(row=5, column=5, padx=5, pady=1, sticky="nsew")

def count_volumeStCone():
    cone = figure_classes_volume.StandardCone(window)
    result = cone.volumeStCone()

    if result != "Canceled":
        lbl_wynik.config(text=result)
    else:
        lbl_wynik.config(text="Canceled")

#-----------------------------------------

#GitHub Button
def open_my_github():
    webbrowser.open_new("https://github.com/wieslawpaleta")

gt_button = Button(window, text="My GitHub Profile", font=("Courrier", 25), bg='white', fg="#000000", command=open_my_github)
gt_button.grid(row=6, column=3, padx=5, pady=1, sticky="nsew")

#-----------------------------------------
window.config(background="#FFFFFF")

photo_refs = {}

def resize_images(event):
    if event.widget != window:
        return

    new_w = max(100, int(event.width / 5.5))
    new_h = max(40, int(event.height / 8))

    all_elements = [
        (pil_image, btn),
        (pil_image_areaStRec, btn_areaStRec),
        (pil_image_areaStCirc, btn_areaStCirc),
        (pil_image_areaStRhom, btn_areaStRhom),
        (pil_image_areaStTrap, btn_areaStTrap),
        (pil_image_volumeStCubo, btn_volumeStCubo),
        (pil_image_volumeStCube, btn_volumeStCube),
        (pil_image_volumeStSphere, btn_volumeStSphere),
        (pil_image_volumeStCylinder, btn_volumeStCylinder),
        (pil_image_volumeStCone, btn_volumeStCone)
    ]

    for idx, (img, button) in enumerate(all_elements):
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        new_icon = ImageTk.PhotoImage(resized)
        button.config(image=new_icon)
        photo_refs[idx] = new_icon

window.bind("<Configure>", resize_images)

for col in range(1, 6):
    window.grid_columnconfigure(col, weight=1)

window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(5, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)


window.mainloop()

