import machine
import utime
from chittiSat.gyro import MPU6050
from chittiSat.assistant import *

i2c = machine.I2C(0, sda =machine.Pin(0),scl =machine.Pin(1))
mpu6050 = MPU6050(i2c)

while True:

    gx = round(mpu6050.gyro.x,2)
    gy = round(mpu6050.gyro.y,2)
    gz = round(mpu6050.gyro.z,2)
    
    ax = round(mpu6050.accel.x,2)
    ay = round(mpu6050.accel.y,2)
    az = round(mpu6050.accel.z,2)

    dashboard.sendGyro(gx, gy, gz, ax, ay, az)
    
    utime.sleep(0.1)