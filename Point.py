import math


class Point(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def distanceFrom( self, x, y, z):
        return math.sqrt(
            (self.x-x)**2 +
            (self.y-y)**2 +
            (self.z-z)**2)

    def distanceFrom(self, point):
        return math.sqrt(
            (self.x-point.x)**2 +
            (self.y-point.y)**2 +
            (self.z-point.z)**2)
