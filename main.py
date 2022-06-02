#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Iniciar motor en puerto A y D
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Inicializar el sensor de luz
line_sensor = ColorSensor(Port.S1)

# Inicializar DriveBase()
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=170)

# Declarar velocidad de motores
DRIVE_SPEED = 100

# Calcular el limite de luz
BLACK = 11
WHITE = 97
limite = (BLACK + WHITE) / 2

# Declarar ganancias proporcional
#PROPORTIONAL_GAIN = 1.2

# Write your program here.
ev3.speaker.beep(3000, 0.5)

while True :
    # Calcula la desviacion
    sensor=line_sensor.reflection()
    ev3.screen.draw_text(0, 0, sensor, Color.BLACK, None)
    desviacion = line_sensor.reflection() - limite

    # Valor de giro
    valor_giro = desviacion

    # Robot avanza
    robot.drive(DRIVE_SPEED, valor_giro)