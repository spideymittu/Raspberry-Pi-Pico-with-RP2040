import machine
import utime
from chittiSat.sdcard import*
import uos


spi = machine. SPI(1, sck = machine.Pin(14), mosi = machine.Pin(15), miso = machine.Pin(12))

sd = SDCard(spi)

usi.mount(sd, '/sd')
print("sd card connected")
print(uos . listdir( ' /sd'))
