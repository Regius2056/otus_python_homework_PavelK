import math

from src.figure import Figure

class Circle(Figure):

    def __init__(self, radius):
        if isinstance(radius, str):
            raise ValueError('Only numbers are allowed')
        if radius <= 0:
            raise ValueError(f'Radius of Circle should be above 0, actual is {radius}')

        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
