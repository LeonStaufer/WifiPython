import matplotlib.pyplot as plt

from Point import Point
from RSSI import RSSI
from Trilaterate import trilaterate_mathematical

plt.figure(dpi=300)

ax = plt.gca(aspect='equal')
ax.cla()
ax.set_xlim((0, 1200))
ax.set_ylim((0, 1000))

P1 = Point(583.65, 297.99, 1)
P2 = Point(780.51, 430.87, 1)
P3 = Point(429.78, 690.11, 1)

DistA = 237.51
DistB = 273.14
DistC = 187.97

ax.add_artist(plt.Circle((P1.x, P1.y), DistA, color="red", alpha=0.5))
ax.add_artist(plt.Circle((P2.x, P2.y), DistB, color="blue", alpha=0.5))
ax.add_artist(plt.Circle((P3.x, P3.y), DistC, color="green", alpha=0.5))

result = trilaterate_mathematical([P1, P2, P3], [[0, RSSI(DistA, 2.5)], [0, RSSI(DistB, 2.4)], [0, RSSI(DistC, 2.4)]], 1)

ax.add_artist(plt.Circle((result.item(0), result.item(0)), 10, color="black"))

plt.tight_layout(1)

plt.savefig("assets/perfectTrilateration.png")
plt.show()
