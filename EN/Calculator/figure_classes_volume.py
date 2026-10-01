import math


class ClassicCube:
    def __init__ (self, side):
        self.side = side

    def volumeClc(self):
        calculation = round(self.side ** 3, 4)
        return f"The volume of your cube is: {calculation}"

your_cubeClc = ClassicCube(5)

print(your_cubeClc.volumeClc())


class ClassicSphere:
    def __init__(self, radius):
        self.radius = radius

    def volumeClsp(self):
        calculation = round(4 / 3 * 3.14159 * self.radius ** 3, 4)
        return f"The volume of your sphere is: {calculation}"

your_sphereClsp = ClassicSphere(5)

print(your_sphereClsp.volumeClsp())

class ClassicCylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volumeClcy(self):
        calculation = round((3.14159 * self.radius ** 2) * self.height, 4)
        return f"The volume of your cylinder is: {calculation}"

your_cylinderClcy = ClassicCylinder(5, 5)

print(your_cylinderClcy.volumeClcy())

class ClassicCone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volumeClco(self):
        calculation = round(1 / 3 * 3.14159 * self.radius ** 2 * self.height, 4)
        return f"The volume of your cone is: {calculation}"

your_coneClco = ClassicCone(5, 5)

print(your_coneClco.volumeClco())