import math
from tkinter import simpledialog


#Rectangle, Square, Trapezoid, Rhombus, Hexagon formulas
class StandardRectangle:
    def __init__(self, window):
        self.window = window

    def areaStRec(self):
        length = simpledialog.askfloat("Input", "Pass the length: ", parent=self.window)
        if length is None:
            return "Canceled"
        width = simpledialog.askfloat("Input", "Pass the width: ", parent=self.window)
        if width is None:
            return "Canceled"
        calculation = round(length * width, 4)
        return f"The area of your rectangle is: {calculation}" 


class PowerSquare:
    def __init__(self, length):
        self.length = length

    def areaPowSq(self):
        calculation = pow(self.length, 2)
        return f"The area of your square is: {calculation}"


class DiagonalSquare:
    def __init__(self, diagonal):
        self.diagonal = diagonal

    def areaDiagSq(self):
        calculation = self.diagonal ** 2 / 2
        return f"The area of your square is: {calculation}"


class StandardTrapezoid:
    def __init__ (self, window):
        self.window = window

    def areaStTrap(self):
        bottomBase = simpledialog.askfloat("Input", "Pass the bottom base: ", parent=self.window)
        if bottomBase is None:
            return "Canceled"
        topBase = simpledialog.askfloat("Input", "Pastt the top base: ", parent=self.window)
        if topBase is None:
            return "Canceled"
        height = simpledialog.askfloat("Input", "Pass the height; ", parent=self.window)
        if height is None:
            return "Canceled"
        calculation = round((bottomBase + topBase) / 2 * height, 4)
        return f"The area of your trapezoid is: {calculation}"


class StandardRhombus:
    def __init__ (self, window):
        self.window = window

    def areaStRhom(self):
        diagonal1 = simpledialog.askfloat("Input", "Pass the first diagonal: ", parent=self.window)
        if diagonal1 is None:
            return "Canceled"
        diagonal2 = simpledialog.askfloat("Input", "Pass the second diagonal: ", parent=self.window)
        if diagonal2 is None:
            return "Canceled"
        calculation = round(diagonal1 * diagonal2 / 2, 4)
        return f"The area of your rhombus is: {calculation}"


class StandardRegularHexagon:
    def __init__(self, side):
        self.side = side

    def StRegHex(self):
        calculation = round(6 * (self.side ** 2 * 3 ** (1/2) / 4), 4)
        return f"The area of your hexagon is: {calculation}"


#Triangle formulas
class StandardTriangle:
    def __init__ (self, window):
        self.window = window

    def areaStTriang(self):
        base = simpledialog.askfloat("Input", "Pass the base: ", parent=self.window)
        if base is None: 
            return "Canceled"
        height = simpledialog.askfloat("Input", "Pass the height:", parent=self.window)
        if height is None: 
            return "Canceled"
        calculation = round(base * height / 2, 4)
        return f"The area of your triangle is: {calculation}"

        


class EquilateralTriangleA234:
    def __init__(self, side):
        self.side = side    

    def areaEqTriangA234(self):
        calculation = round(self.side ** 2 * 3 ** (1/2) / 4, 4)
        return f"The area of your equilateral triangle is: {calculation}"


class EquilateralTriangleHeight:
    def __init__ (self, height):
        self.height = height

    def areaEqTriangH(self):
        calculation = round((self.height ** 2) * (3 ** (1/2)) / 3, 4)
        return f"The area of your triangle is: {calculation}"


class EquilateralCircumscribedCircleTriangle:
    def __init__ (self, Radius):
        self.Radius = Radius

    def areaEqCircumCircTriang(self):
        calculation = round((3 * self.Radius ** 2) * 2 ** (1/2) / 4, 4)
        return f"The area of your triangle is: {calculation}"


class EquilateralInscribedCircleTriangle:
    def __init__ (self, radius):
        self.radius = radius

    def areaEqInscrCircTriang(self):
        calculation = round((3 * self.radius ** 2) * 3 ** (1/2), 4)
        return f"The area of your triangle is: {calculation}"


#Circle formulas
#pi = 3.14159
class StandardCircle:
    def __init__ (self, window):
        self.window = window

    def areaStCirc(self):
        radius = simpledialog.askfloat("Input", "Pass the radius: ", parent=self.window)
        if radius is None:
            return "Canceled"
        calculation = round(3.14159 * radius, 4)
        return f"The area of your circle is: {calculation}"


class DiameterCircle:
    def __init__ (self, diameter):
        self.diameter = diameter

    def areaDiamCirc(self):
        calculation = round(3.14159 * self.diameter ** 2 / 4, 4)
        return f"The area of your circle is: {calculation}"