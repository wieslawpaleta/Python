import math
from tkinter import simpledialog

class StandardCuboid:
    def __init__ (self, window):
        self.window = window

    def volumeStCubo(self):
        aSide = simpledialog.askfloat("Input", "Pass a: ", parent=self.window)
        if aSide is None:
            return "Canceled"
        bSide = simpledialog.askfloat("Input", "Pass b: ", parent=self.window)
        if bSide is None:
            return "Canceled"
        cSide = simpledialog.askfloat("Input", "Pass c: ", parent=self.window)
        if cSide is None:
            return "Canceled"
        calculation = round(aSide * bSide * cSide)
        return f"The volume of your cuboid is: {calculation}"


class StandardCube:
    def __init__ (self, window):
        self.window = window

    def volumeStCube(self):
        side = simpledialog.askfloat("Input", "Pass a: ", parent=self.window)
        if side is None:
            return "Canceled"
        calculation = round(side ** 3, 4)
        return f"The volume of your cube is: {calculation}"


class StandardSphere:
    def __init__ (self, window):
        self.window = window
        
    def volumeStSphere(self):
        radius = simpledialog.askfloat("Input", "Pass r: ", parent=self.window)
        if radius is None:
            return "Canceled"
        calculation = round(4 / 3 * math.pi * radius ** 3, 4)
        return f"The volume of your sphere is: {calculation}"


class StandardCylinder:
    def __init__ (self, window):
        self.window = window

    def volumeStCylinder(self):
        radius = simpledialog.askfloat("Input", "Pass r: ", parent=self.window)
        if radius is None:
            return "Canceled"
        height = simpledialog.askfloat("Input", "Pass h: ", parent=self.window)
        if radius is None:
            return "Canceled"
        calculation = round((math.pi * radius ** 2) * height, 4)
        return f"The volume of your cylinder is: {calculation}"


class StandardCone:
    def __init__ (self, window):
        self.window = window

    def volumeStCone(self):
        radius = simpledialog.askfloat("Input", "Pass r: ", parent=self.window)
        if radius is None:
            return "Canceled"
        height = simpledialog.askfloat("Input", "Pass h: ", parent=self.window)
        if height is None:
            return "Canceled"
        calculation = round(1 / 3 * math.pi * radius ** 2 * height, 4)
        return f"The volume of your cone is: {calculation}"