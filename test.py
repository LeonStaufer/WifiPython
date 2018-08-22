import matplotlib.pyplot as plt

from numpy import *
from scipy.optimize import leastsq

points = [(21.8, 3.74, 5.768968649587894),
          (31.2, 3.74, 1.6941731714390469),
          (47.3, 13.87, 16.757730182816537),
          (40.64, 3.74, 4.569936016072616)]


def residuals(point, data):
    d = sqrt(square(data[0] - point[0]) + square(data[1] - point[1])) * square(data[2])
    return d


p0 = [0, 0]

plsq = leastsq(residuals, p0, args=points)
print(plsq[0])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim((0, 80))
ax.set_ylim((-40, 40))

# Plot section
for p in points:
    circ = plt.Circle((p[0], p[1]), radius=p[2], color='b', alpha=0.5)
    circ2 = plt.Circle((p[0], p[1]), radius=0.1, color='r', alpha=1)
    ax.add_patch(circ)
    ax.add_patch(circ2)

circ = plt.Circle(plsq[0], radius=1, color='g', alpha=0.8)
ax.add_patch(circ)
plt.show()