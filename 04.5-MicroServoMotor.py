from machine import Pin, PWM
from time import sleep

servo=PWM(Pin(4), freq=50)

servo.duty(20) # to position servo at 9 degree
sleep(1)
servo.duty(70) # to position servo at 90 degree
sleep(1)
servo.duty(120) # to position servo at 180 degree
sleep(1)