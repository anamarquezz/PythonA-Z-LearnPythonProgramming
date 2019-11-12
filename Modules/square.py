#import Polygon
from Polygon import Polygon
from shape import Shape


class Square(Polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height()
