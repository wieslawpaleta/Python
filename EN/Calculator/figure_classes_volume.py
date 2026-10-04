import math

class ClassicCuboid:
    def __init__ (self, aSide, bSide, cSide):
        self.aSide = aSide
        self.bSide = bSide
        self.cSide = cSide

    def volumeClCubo(self):
        calculation = round(self.aSide * self.bSide * self.cSide)
        return f"The volume of your cuboid is: {calculation}"


class ClassicCube:
    def __init__ (self, side):
        self.side = side

    def volumeClc(self):
        calculation = round(self.side ** 3, 4)
        return f"The volume of your cube is: {calculation}"


class ClassicSphere:
    def __init__(self, radius):
        self.radius = radius

    def volumeClsp(self):
        calculation = round(4 / 3 * 3.14159 * self.radius ** 3, 4)
        return f"The volume of your sphere is: {calculation}"


class ClassicCylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volumeClcy(self):
        calculation = round((3.14159 * self.radius ** 2) * self.height, 4)
        return f"The volume of your cylinder is: {calculation}"


class ClassicCone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volumeClco(self):
        calculation = round(1 / 3 * 3.14159 * self.radius ** 2 * self.height, 4)
        return f"The volume of your cone is: {calculation}"