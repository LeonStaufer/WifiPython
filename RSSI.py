import math


class RSSI(object):
    transmitPower = -35
    LIGHT = 299_792_458

    def __init__(self, RSSI, frequency):
        self.rssi = float(RSSI)
        self.frequency = float(frequency)

    def toDistance(self):
        return self.toDistanceDecayIndoor()

    def toDistanceDefault(self):
        n = 3  # path loss exponent
        return math.pow(10, (self.transmitPower - self.rssi) / (10*n))

    def toDistanceDecayIndoor(self):
        n = 3
        pathLoss = 18
        wavelength = self.LIGHT / (self.frequency * 1e9)
        numerator = math.fabs(self.rssi) - (20 * math.log10((4 * math.pi * 1) / wavelength))
        return math.pow(10, (numerator / (10 * n))*1)
        # https: // electronics.stackexchange.com / a / 195738
