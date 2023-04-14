import serial
import json
import pymongo

class Sensor:
    def __init__(self, tipo="sen", id="SEN", valor=0, pinOut=0, pinIn=0):
        self.tipo = tipo
        self.id = id
        self.valor = valor
        self.pinOut = pinOut
        
    def recibir(self):
        ser = serial.Serial('/dev/ttyUSB0', 9600) # especifica el puerto y la velocidad de transmisión de datos

        while True:
            data = ser.readline().decode('utf-8').rstrip() # lee los datos que llegan por el puerto serial
            return data
    
    def jotason(self, data):
        datosJson = json.dumps(data) # convierte los datos a formato json
        print(datosJson)
        return datosJson
        
    def conexionMongo(self, datos):
        cliente = pymongo.MongoClient("mongodb+srv://root:admin@cluster0.urq1yx8.mongodb.net/?retryWrites=true&w=majority")
        # Selecciona una base de datos
        db = cliente["Prueba"]
        # Selecciona una colección
        collection = db["Datos"]
        # Ejemplo de inserción de un documento
        
        x = collection.insert_one(datos)
