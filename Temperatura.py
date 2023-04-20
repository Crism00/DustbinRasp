import time
import board
import adafruit_dht
import pymongo
import json

import os.path

class DHTSensor():
    def __init__(self, pin, Pin):
        super().__init__()
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.pin = Pin
        self.client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.qf2sgqk.mongodb.net/test")
        self.db = self.client["temperature_db"]
        self.temp_collection = self.db["temperature_data"]
        self.sensor_collection = self.db["sensor_data"]
        self.sensor_id = 6
        self.pin_in = "D16"
        self.pin_out = "D16"
        self.descripcion = "DHT11 Sensor"

    def get_temperatures(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            return temperature_f, humidity
        except RuntimeError as error:
            print(error.args[0])
            return None
    
    def save_temperature_data(self, temperature, humidity):
        data = {
            "tipo": "Temperatura",
            "id_sensor": self.sensor_id,
            "valor": {"temperatura": temperature, "humedad": humidity}
        }
        self.temp_collection.insert_one(data)
    
    def save_sensor_data(self):
        data = {
            "id_sensor": self.sensor_id,
            "pin_in": self.pin_in,
            "pin_out": self.pin_out,
            "descripcion": self.descripcion
        }
        self.sensor_collection.insert_one(data)

    def limpiar(self):
        self.dhtDevice.exit()

    
if __name__ == "__main__":
    temperatura = DHTSensor(board.D16, 16)
    temperatura.save_sensor_data()
    while True:
        temperature, humidity = temperatura.get_temperatures()
        if temperature and humidity:
            temperatura.save_temperature_data(temperature, humidity)
            print("Temperatura F: {:.1f}, Humedad: {}%".format(temperature, humidity))
        time.sleep(30)  # sleep for 30 seconds
