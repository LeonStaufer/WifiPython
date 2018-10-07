import math

import numpy
import scipy.optimize

from Point import Point

ITER = 4
ALPHA = 2
RATIO = 0.99


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

    # from wikipedia
    # transform to get circle 1 at origin
    # transform to get circle 2 on x axis
    ex = (P2 - P1) / (numpy.linalg.norm(P2 - P1))
    i = numpy.dot(ex, P3 - P1)
    ey = (P3 - P1 - i * ex) / (numpy.linalg.norm(P3 - P1 - i * ex))
    ez = numpy.cross(ex, ey)
    d = numpy.linalg.norm(P2 - P1)
    j = numpy.dot(ey, P3 - P1)

    # from wikipedia
    # plug and chug using above values
    x = (pow(DistA, 2) - pow(DistB, 2) + pow(d, 2)) / (2 * d)
    y = ((pow(DistA, 2) - pow(DistC, 2) + pow(i, 2) + pow(j, 2)) / (2 * j)) - ((i / j) * x)

    # raise error if sqrt would be negative
    if pow(DistA, 2) - pow(x, 2) - pow(y, 2) < 0:
        raise ArithmeticError("When calculating Z, the sqrt would have to be negative")

    z = numpy.sqrt(pow(DistA, 2) - pow(x, 2) - pow(y, 2))

    # triPt is an array with ECEF x,y,z of trilateration point
    triPt = P1 + x * ex + y * ey + z * ez
    print(triPt.item(0))
    print(triPt)
    return triPt


"""
    Trilateration solution from StackOverflow, ported from C++
"""


def trilaterate_approx(points, dist):
    res = Point()
    alpha = ALPHA
    for iter in range(ITER):
        delta = Point()
        for i in range(len(points)):
            d = res.distanceFrom(points[i])
            diff = (points[i] - res) * (alpha * (d - dist[i] / max(dist[i], d)))
            delta = delta + diff
        delta = delta * (1.0 / len(points))
        alpha = alpha * RATIO
        res = res + delta
    return res


"""
    function to be optimized    
"""


def distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2)


def distance_sum(x, points):
    distsum = 0
    for c in points:
        dist = distance(x, c) - x[2] * c[2]
        distsum += pow(dist, 2)
    return distsum


"""
    Trilateration solution from https://github.com/henrik-muehe/trilateration/blob/master/trilat_optproblem.py
"""


def trilaterate_opti(points):
    limit = 10
    count = 0

    result = scipy.optimize.fmin(distance_sum, [0, 0, 0], args=(points,), xtol=0.0001, ftol=0.0001, disp=False)
    return result
