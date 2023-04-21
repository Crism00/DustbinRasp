import RPi.GPIO as GPIO
import time

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
IN1 = 24
IN2 = 23
IN3 = 5
IN4 = 6
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Establecer la velocidad del motor



class CarController():
    # Función para avanzar el motor
    @staticmethod
    def avanzar():
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        print("avanzar")

    # Función para detener el motor
    @staticmethod
    def detener():
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        
        
    @staticmethod
    def izquierda():
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)

    @staticmethod
    def centro():
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        
    @staticmethod
    def derecha():
        GPIO.output(IN1, GPIO.LOW);
        GPIO.output(IN2, GPIO.HIGH);
        
    @staticmethod
    def reversa():
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        
    @staticmethod
    def limpiar():
        GPIO.cleanup()

