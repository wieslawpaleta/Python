import math


#Rectangle, Square formulas
class ClassicRectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def areaCR(self):
        calculation = self.length * self.width
        return f"The area of your rectangle is: {calculation}" 

your_rectangle = ClassicRectangle(5, 6)

print(your_rectangle.areaCR())

class PowSquare:
    def __init__(self, length):
        self.length = length

    def areaPS(self):
        calculation = pow(self.length, 2)
        return f"The area of your square is: {calculation}"

your_powsquare = PowSquare(5)

print(your_powsquare.areaPS())


class DiagonalSquare:
    def __init__(self, diagonal):
        self.diagonal = diagonal

    def areaDS(self):
        calculation = self.diagonal ** 2 / 2
        return f"The area of your square is: {calculation}"

your_diagonalsquare = DiagonalSquare(5)

print(your_diagonalsquare.areaDS())


#Triangle formulas
class ClassicTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def areaCT(self):
        calculation = round(self.base * self.height / 2, 4)
        return f"The area of your triangle is: {calculation}"

your_triangleCT = ClassicTriangle(4, 5)

print(your_triangleCT.areaCT())


class EquilateralTriangleA234:
    def __init__(self, side):
        self.side = side    

    def areaETA234(self):
        calculation = round(self.side ** 2 * 3 ** (1/2) / 4, 4)
        return f"The area of your equilateral triangle is: {calculation}"

your_triangleET = EquilateralTriangleA234(5)

print(your_triangleET.areaETA234())


class EquilateralTriangleHeight:
    def __init__ (self, height):
        self.height = height

    def areaETH(self):
        calculation = round((self.height ** 2) * (3 ** (1/2)) / 3, 4)
        return f"The area of your triangle is: {calculation}"

your_triangleTH = EquilateralTriangleHeight(5)

print(your_triangleTH.areaETH())


class EquilateralCircumscribedCircleTriangle:
    def __init__ (self, Radius):
        self.Radius = Radius

    def areaECCT(self):
        calculation = round((3 * self.Radius ** 2) * 2 ** (1/2) / 4, 4)
        return f"The area of your triangle is: {calculation}"

your_triangleECCT = EquilateralCircumscribedCircleTriangle(5)

print(your_triangleECCT.areaECCT())


class EquilateralInscribedCircleTriangle:
    def __init__ (self, radius):
        self.radius = radius

    def areaEICT(self):
        calculation = round((3 * self.radius ** 2) * 3 ** (1/2), 4)
        return f"The area of your triangle is: {calculation}"

your_triangleEICT = EquilateralInscribedCircleTriangle(5)

print(your_triangleEICT.areaEICT())


#Circle formulas
#pi = 3.14159
class ClassicCircle:
    def __init__ (self, radius):
        self.radius = radius

    def areaCC(self):
        calculation = round(3.14159 * self.radius, 4)
        return f"The area of your circle is: {calculation}"

your_circleCC = ClassicCircle(5)

print(your_circleCC.areaCC())


class DiameterCircle:
    def __init__ (self, diameter):
        self.diameter = diameter

    def areaDC(self):
        calculation = round(3.14159 * self.diameter ** 2 / 4, 4)
        return f"The area of your circle is: {calculation}"

your_circleDC = DiameterCircle(5)

print(your_circleDC.areaDC())

