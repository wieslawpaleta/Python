import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def areaR(self):
        calculation = self.length * self.width
        return f"The area of your rectangle is: {calculation}" 


your_rectangle = Rectangle(5, 6)

print(your_rectangle.areaR())

class Square:
    def __init__(self, length):
        self.length = length


    def areaS(self):
        calculation = pow(self.length, 2)
        return f"The area of your square is: {calculation}"


your_square = Square(5)

print(your_square.areaS())

class EquilateralTriangle1:
    def __init__(self, side):
        self.side = side    


    def areaET(self):
        calculation = round(self.side ** 2 * 3 ** (1/2) / 4, 4)
        return f"The area of your equilateral triangle is: {calculation}"


your_triangleET = EquilateralTriangle1(5)

print(your_triangleET.areaET())

class ClassicTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height


    def areaCT(self):
        calculation = round(self.base * self.height / 2, 4)
        return f"The area of your triangle is: {calculation}"


your_triangleCT = ClassicTriangle(4, 5)

print(your_triangleCT.areaCT())

class TriangleHeight:
    def __init__ (self, height):
        self.height = height


    def areaTH(self):
        calculation = round((self.height ** 2) * (3 ** (1/2)) / 3, 4)
        return f"The area of your triangle is: {calculation}"


your_triangleTH = TriangleHeight(5)

print(your_triangleTH.areaTH())