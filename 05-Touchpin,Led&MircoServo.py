# This code contain codes from file 01 to 04.5
# Import libraries
from machine import Pin, TouchPad,PWM
from time import sleep

# Assign pins
touch = TouchPad(Pin(13))
led = Pin(2, Pin.OUT)
led.off()
servo = PWM(Pin(25), freq=50)

# Define the threshold value -> for the touch pin 
THRESHOLD = 100

# Variable 
touch_count = 0  # Initialize the touch count

# Funtion for the microservo motor
def set_servo_angle(angle):
    duty = int((angle / 180) * 115 + 20)
    servo.duty(duty)
    sleep(1)

while True:
    if touch.read() <= THRESHOLD:  # Pin is touched
        if touch_count == 0:  # First touch, turn on the LED
            led.on()
            touch_count = 1
            set_servo_angle(70)
            print("LED on")
        else:  # Second touch, turn off the LED
            led.off()
            touch_count = 0
            print("LED off")
            set_servo_angle(0)
        sleep(0.5)
    else:
        sleep(0.5)
