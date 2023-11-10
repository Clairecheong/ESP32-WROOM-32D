from machine import Pin, TouchPad
from time import sleep

# Assign pins
touch = TouchPad(Pin(4))

while True:
    print(touch.read())
    sleep(0.5) 