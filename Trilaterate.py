import math

import numpy
import scipy.optimize

"""
    mathematical approach to trilateration
"""


def trilaterate_mathematical(points, values, scale):
    for counter, point in enumerate(points):
        if counter == 0:
            P1 = numpy.array([point.x * scale, point.y * scale, point.z * scale])
        elif counter == 1:
            P2 = numpy.array([point.x * scale, point.y * scale, point.z * scale])
        elif counter == 2:
            P3 = numpy.array([point.x * scale, point.y * scale, point.z * scale])

    for counter, val in enumerate(values):
        if counter == 0:
            DistA = val[1].toDistance() * scale
        elif counter == 1:
            DistB = val[1].toDistance() * scale
        elif counter == 2:
            DistC = val[1].toDistance() * scale

    # from Wikipedia derivation
    # transform to get circle 1 at origin
    # transform to get circle 2 on x axis
    ex = (P2 - P1) / (numpy.linalg.norm(P2 - P1))
    i = numpy.dot(ex, P3 - P1)
    ey = (P3 - P1 - i * ex) / (numpy.linalg.norm(P3 - P1 - i * ex))
    ez = numpy.cross(ex, ey)
    d = numpy.linalg.norm(P2 - P1)
    j = numpy.dot(ey, P3 - P1)

    # from Wikipedia derivation
    # insert all values and solve
    x = (pow(DistA, 2) - pow(DistB, 2) + pow(d, 2)) / (2 * d)
    y = ((pow(DistA, 2) - pow(DistC, 2) + pow(i, 2) + pow(j, 2)) / (2 * j)) - ((i / j) * x)

    # raise error if sqrt would be negative
    if pow(DistA, 2) - pow(x, 2) - pow(y, 2) < 0:
        raise ArithmeticError("When calculating Z, the sqrt would have to be negative")

    z = numpy.sqrt(pow(DistA, 2) - pow(x, 2) - pow(y, 2))

    # triPt is an array with x,y,z of trilateration point
    tri_point = P1 + x * ex + y * ey + z * ez
    return tri_point


"""
    Trilateration solution from https://github.com/henrik-muehe/trilateration/blob/master/trilat_optproblem.py
"""


def trilaterate_opti(points):
    """
        helper function
    """
    def _distance(point1, point2):
        return math.sqrt(
            (point1[0] - point2[0]) ** 2 +
            (point1[1] - point2[1]) ** 2)

    """
        helper function for average position
    """
    def _average(points):
        x_sum, y_sum = 0, 0

        for point in points:
            x_sum += point[0]
            y_sum += point[1]

        x = int(x_sum/len(points))
        y = int(y_sum/len(points))

        return [x, y]

    """
        function to be optimized    
    """
    def _distance_sum(x, points):
        distsum = 0
        for c in points:
            dist = _distance(x, c) - x[2] * c[2]
            distsum += pow(dist, 2)
        return distsum

    result = scipy.optimize.fmin(_distance_sum, [_average(points)[0], _average(points)[1], 0], args=(points,), xtol=0.0001, ftol=0.0001, disp=False)
    return result
