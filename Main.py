from pprint import pprint

import matplotlib.pyplot as plt

import Data
from Trilaterate import trilaterate_opti
from WiFi import WiFi

wifi = WiFi("raw/businessDoor.json")

scale = 61

plt.figure(dpi=400, figsize=(7, 3))

ax = plt.gca(aspect='equal')
ax.cla()
ax.set_xlim((0, 3000))
ax.set_ylim((0, 1200))

image = plt.imread("plan1.png")
plt.imshow(image, zorder=0, extent=[0, 3028, 0, 1251])

points = []
values = wifi.load(wifi.read(), False, "FIS")
points2 = []

"""
    helper function for returning the predominant height
    allows the trilateration to take place in only 2 dimensions
"""


def predominant_height(point_list):
    lst = []
    for val in point_list:
        point = Data.addresses.get(val[0][:-3])
        lst.append(point.z)

    return max(set(lst), key=lst.count)


predom_height = predominant_height(values)

for val in values:
    point = Data.addresses.get(val[0][:-3])
    if point.z is predom_height:
        points.append(point)
        dict = [point.x, point.y, val[1].toDistance()]
        points2.append(dict)
        radius = val[1].toDistance() * scale
        ax.add_artist(plt.Circle((point.x*scale, point.y*scale), radius, color="#0F0F0F1F", alpha=0.5))


tripoint = trilaterate_opti(points2)
pprint(tripoint)
ax.add_artist(plt.Circle((42*scale, 7.5*scale), 20, color="blue"))
ax.add_artist(plt.Circle((tripoint[0]*scale, tripoint[1]*scale), 20, color="red"))

plt.axis("off")
plt.tight_layout()
plt.savefig("assets/business.png")
plt.show()
