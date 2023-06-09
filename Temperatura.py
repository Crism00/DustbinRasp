import time
import board
import adafruit_dht
import pymongo
import json

import os.path

class DHTSensor( ):
    def __init__(self, pin, Pin, client):
        super().__init__()
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.pin = Pin
        self.client = client

    def get_temperatures(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            
            
            return temperature_c, temperature_f, humidity
        except RuntimeError as error:
            print(error.args[0])
            return None
        
    def save_to_mongo(self, temperature_c, temperature_f, humidity):
        db = self.client['sensor_data']
        temperatura_collection = db['temperatura']
        temperatura_data = {
            'tipo': 'Temperatura',
            'id_sensor': 6,
            'valor1':  temperature_c ,
            'valor2': humidity
            
        }
        temperatura_collection.insert_one(temperatura_data)

        sensor_collection = db['sensor']
        sensor_data = {
            'id_sensor': 6,
            'pin_in': self.pin,
            'pin_out':0,
            'descripcion': ' sensor de temperatura y humedad'
        }
        sensor_collection.insert_one(sensor_data)

        

    def limpiar(self):
        self.dhtDevice.exit()

    
if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
    temperatura = DHTSensor(board.D16, 16,client)
    while True:

        temperature_c, temperature_f, humidity = temperatura.get_temperatures()
        temperatura.save_to_mongo(temperature_c, temperature_f, humidity)


        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))

        time.sleep(20)  # 