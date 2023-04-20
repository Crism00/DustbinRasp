import time

import Adafruit_DHT
import pymongo
import json

import os.path

class DHTSensor( ):
    def __init__(self, pin,Pin):
        super().__init__()
        self.dhtDevice = Adafruit_DHT.DHT11(pin)
        self.pin = Pin

    def get_temperatures(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            return temperature_f, temperature_c, humidity
        except RuntimeError as error:
            print(error.args[0])
            return None

   

    def limpiar(self):
        self.dhtDevice.exit()

    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                temperatures = self.get_temperatures()
                if temperatures is not None:
                    self.check_internet(*temperatures)
                    print("Temperatura F: {:.1f}, Temperatura C: {:.1f}, Humedad: {}%".format(*temperatures))
                    self.check_internet(*temperatures)

                    
            elif opcion == 2:
                break
            else:
                print("Opcion no valida")

    def menu(self):
        print("1. Temperatura y humedad")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    

if __name__ == "__main__":
    sensor = DHTSensor(16,16)
    sensor.run()
    sensor.limpiar()