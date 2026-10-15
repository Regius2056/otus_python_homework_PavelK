from src.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side_a):
        if not isinstance(side_a, int):
            raise ValueError('Only numbers are allowed')
        if side_a <=0:
            raise ValueError(f'Object of class Square must have sides above zero, actual is {side_a}')

        super().__init__(side_a, side_a)
