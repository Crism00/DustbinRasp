import serial
import json
import pymongo

<<<<<<< HEAD
ser = serial.Serial('/dev/ttyACM0', 9600) # especifica el puerto y la velocidad de transmisión de datos

while True:
    data = ser.readline().decode('utf-8').rstrip() # lee los datos que llegan por el puerto serial
    print(data) # muestra los datos recibidos en la consola
=======
class Sensor:
    def __init__(self ,tipo="sen", id="SEN", valor=0, pinOut=0, pinIn=0):
        self.tipo = tipo
        self.id = id
        self.valor = valor
        self.pinOut = pinOut
        
    def recibir():
        ser = serial.Serial('/dev/ttyUSB0', 9600) # especifica el puerto y la velocidad de transmisión de datos

        while True:
            data = ser.readline().decode('utf-8').rstrip() # lee los datos que llegan por el puerto serial
        return data;
    
    def jotason(data):
        datosJson = json.dumps(data) # convierte los datos a formato json
        print(datosJson)
        return datosJson;
        
    def conexionMongo(datos):
        cliente = pymongo.MongoClient("mongodb+srv://root:admin@cluster0.urq1yx8.mongodb.net/?retryWrites=true&w=majority")
        # Selecciona una base de datos
        db = client["Prueba"]
        # Selecciona una colección
        collection = db["Datos"]
        # Ejemplo de inserción de un documento
        
        x = collection.insert_one(datos)
>>>>>>> 60eb6cd9dae7542d4fb22caf5b64c8953557acbb
