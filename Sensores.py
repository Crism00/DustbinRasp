from uuid import uuid4
from parse_json import ParseJson
import serial
import json
import pymongo
import sys

class Sensor:
    def __init__(self, tipo="sen", id="SEN", valor=0, pinOut=0, pinIn=0):
        self.uri = "mongodb+srv://caesarwenli:adminadmin@cluster0.vk6alym.mongodb.net/?retryWrites=true&w=majority"
        self.tipo = tipo
        self.id = id
        self.valor = valor
        self.pinOut = pinOut
        self.cliente = pymongo.MongoClient(self.uri)
        # Selecciona una base de datos
        self.db = self.cliente["Prueba"]
        self.collection = self.db["test"]
        # Selecciona una colección
        print('/dev/'+sys.argv[1])
        
    def recibir(self):
        baudrate = 9600
        if sys.argv[1] == '/dev/ttyACM1':
            baudrate = 19200
        try:
            ser = serial.Serial('/dev/'+sys.argv[1], baudrate )
        except Exception as e:
            print(e)
        data = ser.readline().decode('utf-8').rstrip()
        print(data)
        result = json.loads(data)
        
        try:
            if ('sensor' in result):
                self.conexionMongo(result['sensor'], "Sensores")
                
            if ('detalle' in result):
                self.conexionMongo(result['detalle'], "Detalles")
                
            # print(data)
        except Exception as E:
            print(E)
            
        return data
        
    def conexionMongo(self, datos, coleccion):
        datos['_id'] = str(uuid4())
        self.collection = self.db[coleccion]
        try:
            self.insert_failed(coleccion)
            self.collection.insert_one(datos)

        except Exception as e:
            failed = ParseJson(coleccion).read()
            failed.append(datos)
            ParseJson(coleccion).write(failed)
            print(e)

    
    def insert_failed(self, collection_name) -> None:
        print(collection_name)
        failed = ParseJson(collection_name).read()
        if len(failed) > 0:
            try:
                self.collection.insert_many(failed)
                ParseJson(collection_name).write([])
                print("Failed dumps inserted")
            except:
                print("Failed to insert failed dumps")

