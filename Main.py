import math
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import Data
from WiFi import WiFi


_list = []

wifi = WiFi("D:\\mathDoor.json")

scale = 61

plt.figure(dpi=600)

image = plt.imread("plan1.png")
plt.imshow(image, zorder=0, extent=[0, 3028, 0, 1251])


# plt.xlabel("X")
# plt.ylabel("Y")
# plt.suptitle("WiFi Access Points")

for val in wifi.load(wifi.read(), False, "FIS"):
    point = Data.addresses.get(val[0][:-3])
    if point.z is 4:
        pprint(val[0][:-3])
        pprint(val[1].toDistance())
        size = math.pow(val[1].toDistance(),2)*scale
        pprint(size)
        plt.scatter(point.x*scale, point.y*scale, s=size, marker="s", color="#0F0F0F1F", edgecolors="red", linewidths=0.5)


plt.show()
