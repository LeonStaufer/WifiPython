import math
from decimal import Decimal


class Point(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, multiplicand):
        return Point(self.x * multiplicand, self.y * multiplicand, self.z * multiplicand)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

    def distanceFrom(self, x, y, z):
        return math.sqrt(
            (self.x-x)**2 +
            (self.y-y)**2 +
            (self.z-z)**2)

    def distanceFrom(self, point):
        return math.sqrt(
            (Decimal(self.x)-Decimal(point.x))**2 +
            (Decimal(self.y)-Decimal(point.y))**2 +
            (Decimal(self.z)-Decimal(point.z))**2)
