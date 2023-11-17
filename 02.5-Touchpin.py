from machine import Pin, TouchPad
from time import sleep

# Assign pins
touch = TouchPad(Pin(4))

while True:
    # Displays the touch pin4 capacitance
        # When the pin is not touched, the capacitance reading is at a range from 500 - 600 
        # When the pin is touched, the capacitance reads is at 300  or below 
    print(touch.read())
    sleep(0.5) 