import machine
import utime

on_board_led = machine.Pin(25,machine.Pin.OUT)
on_board_led.on()