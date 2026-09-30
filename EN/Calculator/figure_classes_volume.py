import math


class ClassicCube:
    def __init__ (self, side):
        self.side = side

    def volumeClc(self):
        calculation = (self.side ** 3, 4)
        return f"The volume of your cube is: {calculation}"

your_cubeClc = ClassicCube(5)

print(your_cubeClc.volumeClc())


class ClassicSphere:
    def __init__(self, radius):
        self.radius = radius

    def volumeClsp(self):
        calculation = (4 / 3 * (3.14159 * (self.radius ** 3)), 4)
        return f"The volume of your sphere is: {calculation}"

your_sphereClsp = ClassicSphere(5)

print(your_sphereClsp.volumeClsp())