from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

db = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=56,
    axle_track=120
)

distance = 300
turn_angle = 90

def drive_square():
    for i in range(4):
        db.straight(distance)
        db.turn(turn_angle)

db.reset()

drive_square()

wait(1000)

print("Fertig!")
