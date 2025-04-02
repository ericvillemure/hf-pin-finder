from contextlib import asynccontextmanager
# We imports the GPIO module
import RPi.GPIO as GPIO
# We import the command sleep from time
import time

# https://cdn.shopify.com/s/files/1/0015/7571/4865/files/datasheet_SG90Servo.pdf?353
middle = 7
left = 5
right = 9

# servoPIN = 23
# GPIO.setmode(GPIO.BCM)
servoPIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)



def clickLeft(pin = p):
    pin.ChangeDutyCycle(left)
    time.sleep(0.5)
    pin.ChangeDutyCycle(middle)
    time.sleep(0.5)

def clickRight(pin = p):
    pin.ChangeDutyCycle(right)
    time.sleep(0.5)
    pin.ChangeDutyCycle(middle)
    time.sleep(0.5)


print("start")
p.start(middle)


def cleanup():
    GPIO.cleanup()


