import math


#Rectangle, Square, Trapezoid, Rhombus, Hexagon formulas
class StandardRectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def areaStRec(self):
        calculation = self.length * self.width
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
    def __init__ (self, bottomBase, topBase, height):
        self.bottomBase = bottomBase
        self.topBase = topBase
        self.height = height

    def areaStTrap(self):
        calculation = round((self.bottomBase + self.topBase / 2) * self.height, 4)
        return f"The area of your trapezoid is: {calculation}"


class StandardRhombus:
    def __init__ (self, diameter1, diameter2):
        self.diameter1 = diameter1
        self.diameter2 = diameter2

    def areaStRhom(self):
        calculation = round(self.diameter1 * self.diameter2 / 2, 4)
        return f"The area of your rhombus is: {calculation}"


class StandardRegularHexagon:
    def __init__(self, side):
        self.side = side

    def StRegHex(self):
        calculation = round(6 * (self.side ** 2 * 3 ** (1/2) / 4), 4)
        return f"The area of your hexagon is: {calculation}"


#Triangle formulas
class StandardTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def areaStTriang(self):
        calculation = round(self.base * self.height / 2, 4)
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
    def __init__ (self, radius):
        self.radius = radius

    def areaStCirc(self):
        calculation = round(3.14159 * self.radius, 4)
        return f"The area of your circle is: {calculation}"


class DiameterCircle:
    def __init__ (self, diameter):
        self.diameter = diameter

    def areaDiamCirc(self):
        calculation = round(3.14159 * self.diameter ** 2 / 4, 4)
        return f"The area of your circle is: {calculation}"