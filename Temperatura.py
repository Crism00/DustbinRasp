import time
import board
import adafruit_dht
import pymongo

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
            return print("Temperatura F: {:.1f}, Temperatura C: {:.1f}, Humedad: {}%".format(temperature_f, temperature_c, humidity))
        except RuntimeError as error:
            print(error.args[0])
            return None
    
    def save_to_mongo(self, temperature_c, temperature_f, humidity):
        db = self.client['sensor_data']
        temperatura_collection = db['temperatura']
        temperatura_data = {
            'tipo': 'Temperatura',
            'id_sensor': '6',
            'valor': {
                'temperatura_c': temperature_c,
                'temperatura_f': temperature_f,
                'humedad': humidity
            }
        }
        temperatura_collection.insert_one(temperatura_data)

        sensor_collection = db['sensor']
        sensor_data = {
            'id_sensor': '6',
            'pin_in': 'D16',
            'pin_out': 'D16',
            'descripcion': 'Sensor de temperatura y humedad DHT11'
        }
        sensor_collection.insert_one(sensor_data)

    def limpiar(self):
        self.dhtDevice.exit()

if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb+srv://admin:<password>@cluster0.qf2sgqk.mongodb.net/test')
    temperatura = DHTSensor(board.D16, 16, client)
    while True:
        temperature_c, temperature_f, humidity = temperatura.get_temperatures()
        temperatura.save_to_mongo(temperature_c, temperature_f, humidity)
        time.sleep(300)  # sleep for 5 minutes
