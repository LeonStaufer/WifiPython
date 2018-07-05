import json
from subprocess import call

from RSSI import RSSI


class WiFi:
    path = "temp.json"

    def __init__(self, path):
        self.path = path

    def scrape(self):
        call("cmd /c WifiInfoView.exe /sjson "+self.path)

    def read(self):
        with open(self.path, encoding="utf-16") as file:
            return json.load(file)

    def load(self, file, use5Ghz, SSID):
        mylist = []

        for line in file:
            _read = float(line["Frequency"]) > 5 if use5Ghz else float(line["Frequency"]) < 5
            _ssid = SSID == line["SSID"]
            if _read and _ssid:
                mylist.append([
                    line["MAC Address"],
                    RSSI(line["RSSI"], line["Frequency"]),
                    line["Frequency"]])

        sorted(mylist, key=lambda _line:
                _line[1].rssi
               )

        return mylist
