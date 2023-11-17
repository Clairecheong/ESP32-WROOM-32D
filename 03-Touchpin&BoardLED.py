
# Import libraries
import machine
from machine import Pin, TouchPad
from time import sleep

# Assign pins
touch = TouchPad(Pin(4))
led = machine.Pin(2, machine.Pin.OUT)
led.off()

# Threshold values: the pin needs to be in contact with a conductive material
# When the pin is not touched, the value should be 500 or higher
# When the pin is touched, the value decreases to below 100

touch.config(100)

while True:
    if touch.read() <= 100:
        led.on()
        print("Touched, Touchpin current value=" + str(touch.read()))
        sleep(0.5)
    else:
        led.off()
        print("Waiting")
        sleep(2)