import math


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

your_triangleICT = EquilateralCircumscribedCircleTriangle(5)

print(your_triangleICT.areaECCT())


