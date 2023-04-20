import time
import board
import adafruit_dht
import pymongo
import json

import os.path

class DHTSensor( ):
    def __init__(self, pin, Pin):
        super().__init__()
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.pin = Pin

    def get_temperatures(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            return print("Temperatura F: {:.1f}, Temperatura C: {:.1f}, Humedad: {}%".format(temperature_f, temperature_c, humidity))
        except RuntimeError as error:
            print(error.args[0])
            return None


    def limpiar(self):
        self.dhtDevice.exit()

    
if __name__ == "__main__":
    temperatura = DHTSensor(board.D16, 16)
    while True:
        temperatura.get_temperatures()
        time.sleep(30)  # sleep for 5 minutes
