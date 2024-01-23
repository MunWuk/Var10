from geometric_shape import GeometricShape
from color import Color

class Rectangle(GeometricShape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def calculate_area(self):
        return self.width * self.height

    def __repr__(self):
        return "Rectangle - Width: {}, Height: {}, Color: {}, Area: {}".format(
            self.width, self.height, self.color.color, self.calculate_area()
        )
