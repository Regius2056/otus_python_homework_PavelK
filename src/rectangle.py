from src.figure import Figure

class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if isinstance(side_a, str) or isinstance(side_b, str) :
            raise ValueError('Only numbers are allowed')
        if side_a <=0 or side_b <= 0:
            raise ValueError(f'Object of class Rectangle must have sides above zero, actual is {side_a}/{side_b}')

        self.side_a = side_a
        self.side_b = side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    @property
    def area(self):
        return self.side_a * self.side_b
