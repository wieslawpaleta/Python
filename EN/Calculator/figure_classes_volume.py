import math

class StandardCuboid:
    def __init__ (self, aSide, bSide, cSide):
        self.aSide = aSide
        self.bSide = bSide
        self.cSide = cSide

    def volumeStCubo(self):
        calculation = round(self.aSide * self.bSide * self.cSide)
        return f"The volume of your cuboid is: {calculation}"


class StandardCube:
    def __init__ (self, side):
        self.side = side

    def volumeStc(self):
        calculation = round(self.side ** 3, 4)
        return f"The volume of your cube is: {calculation}"


class StandardSphere:
    def __init__(self, radius):
        self.radius = radius

    def volumeStsp(self):
        calculation = round(4 / 3 * 3.14159 * self.radius ** 3, 4)
        return f"The volume of your sphere is: {calculation}"


class StandardCylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volumeStcy(self):
        calculation = round((3.14159 * self.radius ** 2) * self.height, 4)
        return f"The volume of your cylinder is: {calculation}"


class StandardCone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volumeStco(self):
        calculation = round(1 / 3 * 3.14159 * self.radius ** 2 * self.height, 4)
        return f"The volume of your cone is: {calculation}"