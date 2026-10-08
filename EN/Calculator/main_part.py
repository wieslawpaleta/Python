import os
import math
import figure_classes_area
import figure_classes_volume
from tkinter import *
import tkinter as tk

window = Tk()

window.title("My Calculator")
window.geometry("720x480")
window.minsize(480, 360)


current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, "favicon.ico")
window.iconbitmap(icon_path)


image_path = os.path.join(current_dir, "StandardTriangle.png")
icon = tk.PhotoImage(file=image_path)


def count_areaStTriang():
    pass

btn = tk.Button(window, image=icon, command=lambda: count_areaStTriang)
btn.pack(pady=1)

window.config(background='#ffffff')


frame = Frame(window, bg='#ffffff')


standard_triangle_button = Button(frame)
frame.pack(expand=YES)
window.mainloop()