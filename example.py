from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

db = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=56,
    axle_track=120
)
