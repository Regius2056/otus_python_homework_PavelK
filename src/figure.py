from abc import abstractclassmethod, ABC

class Figure(ABC):

    @property
    @abstractclassmethod
    def perimeter(self):
        pass

    @property
    @abstractclassmethod
    def area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError('Can add only other figure')

        return self.area + other_figure.area
