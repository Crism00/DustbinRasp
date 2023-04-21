import time
import board
import adafruit_dht
import pymongo
import json

import os.path

class DHTSensor( ):
    def __init__(self, pin, Pin,client):
        super().__init__()
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.pin = Pin
        self.client = client

    def get_temperatures(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            self.save_to_mongo(temperature_c, temperature_f, humidity)
            return print("Temperatura F: {:.1f}, Temperatura C: {:.1f}, Humedad: {}%".format(temperature_f, temperature_c, humidity))


        except RuntimeError as error:
            print(error.args[0])
            return None
        

    def save_to_mongo(self, temperature_c, temperature_f, humidity):
        db = self.client['sensor_data']

        # Save temperature data to a JSON document
        temperatura_doc = {
            'tipo': 'Temperatura',
            'id_sensor': '6',
            'valor': {
                'temperatura_c': temperature_c,
                'temperatura_f': temperature_f,
                'humedad': humidity
            }
        }
        temperatura_json = json.dumps(temperatura_doc)

        # Insert temperature data JSON into collection
        temperatura_collection = db['temperatura']
        temperatura_collection.insert_one(json.loads(temperatura_json))

        # Save sensor data to a JSON document
        sensor_doc = {
            'id_sensor': '6',
            'pin_in': 'D16',
            'pin_out': 'D16',
            'descripcion': 'Sensor de temperatura y humedad DHT11'
        }
        sensor_json = json.dumps(sensor_doc)

        # Insert sensor data JSON into collection
        sensor_collection = db['sensor']
        sensor_collection.insert_one(json.loads(sensor_json))

    
    


    def limpiar(self):
        self.dhtDevice.exit()

    
if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb+srv://admin:<password>@cluster0.qf2sgqk.mongodb.net/test')

    temperatura = DHTSensor(board.D16, 16, client)
    while True:
        temperatura.get_temperatures()
        time.sleep(30)  # sleep for 5 minutes


