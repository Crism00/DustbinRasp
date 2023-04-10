import serial

ser = serial.Serial('/dev/ttyUSB0', 9600) # especifica el puerto y la velocidad de transmisión de datos

while True:
    data = ser.readline().decode('utf-8').rstrip() # lee los datos que llegan por el puerto serial
    print(data) # muestra los datos recibidos en la consola