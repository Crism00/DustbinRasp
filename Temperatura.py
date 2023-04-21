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
        
  
        

    def limpiar(self):
        self.dhtDevice.exit()

    
if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient("<mongo_uri>")
    db = client.test_database
    collection = db.test_collection

    # Create a DHTSensor object
    temperatura = DHTSensor(board.D16)

    while True:
        temperature_c, temperature_f, humidity = temperatura.get_temperatures()
        if temperature_c is not None and humidity is not None:
            # Create a dictionary object to store the data
            data = {"temperature_c": temperature_c, "temperature_f": temperature_f, "humidity": humidity}

            # Insert the data into the MongoDB collection
            collection.insert_one(data)

            print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
        else:
            print("Failed to retrieve data from sensor")

        time.sleep(20)






