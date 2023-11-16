# Import libraries
from machine import Pin, TouchPad
from time import sleep

# Assign pins
touch = TouchPad(Pin(4))
led = Pin(2, Pin.OUT)
led.off()

# Define the threshold value
THRESHOLD = 100

touch_count = 0  # Initialize the touch count

while True:
    if touch.read() <= THRESHOLD:  # Pin is touched
        if touch_count == 0:  # First touch, turn on the LED
            led.on()
            touch_count = 1
            print("LED on")
        else:  # Second touch, turn off the LED
            led.off()
            touch_count = 0
            print("LED off")
        sleep(0.5)
    else:
        sleep(0.5)