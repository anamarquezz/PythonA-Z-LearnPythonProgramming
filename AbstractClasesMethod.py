# Don't allow user to create object of my Parent class
# Method of Parent class should be implemented in sub-classes

from abc import ABC, abstractmethod

# from abc import *  -Discussing Over import and from


class Shape(ABC):  # now is an abstract class

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


#shape_obj = Shape()
square_obj = Square(10)
print(square_obj.area())
