import pymongo
from datetime import datetime
import Adafruit_DHT
import RPi.GPIO as GPIO
import json

class Temperatura:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = 16
        GPIO.setmode(GPIO.BCM)
        self.DHT_PIN = 16

    def get_temperatura_humedad(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.DHT_PIN)
        if temperature is not None and humidity is not None:
            datos = {"temperatura": temperature, "humedad": humidity, "fecha": datetime.now()}
            return datos
        else:
            return {"temperatura": 0, "humedad": 0, "fecha": datetime.now()}
        
    def temHum(self):
        print("Temperatura y humedad")
        temperatura = Temperatura()
        datos = temperatura.get_temperatura_humedad()
        print("Temperatura: ", datos["temperatura"], "C")
        print("Humedad: ", datos["humedad"], "%")
        
   


temperatura = Temperatura()
temperatura.temHum()