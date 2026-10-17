import math

from src.figure import Figure

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if isinstance(side_a, str) or isinstance(side_b, str) or isinstance(side_c, str):
            raise ValueError('Only numbers are allowed')
        if side_a <=0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f'Object of class Triangle must have sides above zero, actual is {side_a}/{side_b}/{side_c}')
        sides = sorted((side_a, side_b, side_c))
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError(f'The figure with sides {side_a}, {side_b}, {side_c} is not Triangle')

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
