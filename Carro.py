import socketio
import time
from CarController import CarController


# standard Python
sio = socketio.Client()
sio.connect('http://206.189.229.90:3333')


@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('coordinates')
def on_message(data):
    carro(data);

def carro(data):
    if(data[1] > 0.1):
        CarController.avanzar()
        if(data[0] > 0.3):
            CarController.derecha();
        if(data[0] < -0.3):
            CarController.izquierda();
    if(data[0] > 0.1):
        CarController.derecha();
    if(data[0] < -0.1):
        CarController.izquierda();
    if(data[1] < -0.1):
        CarController.reversa();
        if([0] < -0.3):
            CarController.derecha();
        if([1] > 0.3):
            
        
    if(data[1] < 0.1):
        CarController.reversa();
    if(data[0]==0 and data[1]==0):
        CarController.detener();
sio.wait();