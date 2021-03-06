#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create your objects here.
ev3 = EV3Brick()

# Iniciar motor en puerto A y D
izquierdo = Motor(Port.A)
derecho = Motor(Port.D)

# Inicializar el sensor de luz
sensor = ColorSensor(Port.S1)

# Inicializar DriveBase()
robot = DriveBase(izquierdo, derecho, wheel_diameter=55.5, axle_track=170)

# Declarar velocidad de motores
VELOCIDAD = 100

# Calcular el limite de luz
NEGRO = 11
BLANCO = 97
umbral = (NEGRO + BLANCO) / 2

# Declarar ganancias proporcional
#PROPORTIONAL_GAIN = 1.2

# Write your program here.
ev3.speaker.beep(3000, 0.5)

while True:
    # Calcula la desviacion
    # Calcula la desviacion
    valor= sensor.reflection()
    ev3.screen.print(valor)
    if (valor<=umbral):
        derecho.stop()
        izquierdo.run(VELOCIDAD)
    else:
        izquierdo.stop() 
        derecho.run(VELOCIDAD)
        