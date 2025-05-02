from machine
from chittiSat.mq2 import MQ2
import utime

sensor = MQ2(pinData =26)

sensor. calibrate()

while True:
    Smoke= sensor.readSmoke()
    LPG = sensor.readLPG()
    Methane = sensor.readMethane()
    Hydrogen = sensor.readHydrogen()

    dashboard. sendAir(Smoke, GAS, Methane,Hydrogen)
