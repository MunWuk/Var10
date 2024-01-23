from geometric_shape import GeometricShape
from color import Color
import math

class Circle(GeometricShape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Circle - Radius: {}, Color: {}, Area: {}".format(
            self.radius, self.color.color, self.calculate_area()
        )
