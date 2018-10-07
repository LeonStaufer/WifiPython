from pprint import pprint

import matplotlib.pyplot as plt

import Data
from Point import Point
from Trilaterate import trilaterate_mathematical, trilaterate_approx, trilaterate_opti
from WiFi import WiFi

wifi = WiFi("raw/mathDoor.json")

scale = 61

plt.figure(dpi=400)

ax = plt.gca(aspect='equal')
ax.cla()
ax.set_xlim((0, 3000))
ax.set_ylim((0, 1200))

image = plt.imread("plan1.png")
plt.imshow(image, zorder=0, extent=[0, 3028, 0, 1251])


# plt.xlabel("X")
# plt.ylabel("Y")
# plt.suptitle("WiFi Access Points")

points = []
values = wifi.load(wifi.read(), False, "FIS")
points2 = []

for val in values:
    point = Data.addresses.get(val[0][:-3])
    if point.z is 4:
        points.append(point)
        dict = [point.x, point.y, val[1].toDistance()]
        points2.append(dict)
        radius = val[1].toDistance() * scale
        ax.add_artist(plt.Circle((point.x*scale, point.y*scale), radius, color="#0F0F0F1F", alpha=0.5))

#result = trilaterate_mathematical(points, values, scale)
"""
print(trilaterate_approx([
    Point(21.8, 3.74, 4),
    Point(31.2, 3.74, 6),
    Point(31.2, 3.74, 4),
    Point(21.15, 12, 6),
    Point(7, 3.74, 6),
    Point(21.8, 3.74, 6),
    Point(47.3, 13.87, 6),
    Point(40.64, 3.74, 6),
    Point(47.3, 13.87, 4),
    Point(40.64, 3.74, 4),
], [
    5.768968649587894,
    19.67147263933248,
    1.6941731714390469,
    14.37303644749458,
    29.072944794470832,
    3.6399731395334642,
    14.471166480939697,
    2.677718046538936,
    16.757730182816537,
    4.569936016072616
]))
"""


tripoint = trilaterate_opti(points2)

ax.add_artist(plt.Circle((tripoint[0]*scale, tripoint[1]*scale), 20, color="red"))

plt.show()
