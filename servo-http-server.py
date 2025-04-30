# fastapi run servo-http-server.py 
from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
# We imports the GPIO module
import RPi.GPIO as GPIO
# We import the command sleep from time
import time

# https://cdn.shopify.com/s/files/1/0015/7571/4865/files/datasheet_SG90Servo.pdf?353
middle = 7
left = 5
right = 9

def clickLeft(pin):
    pin.ChangeDutyCycle(left)
    time.sleep(0.5)
    pin.ChangeDutyCycle(middle)
    time.sleep(0.5)

def clickRight(pin):
    pin.ChangeDutyCycle(right)
    time.sleep(0.5)
    pin.ChangeDutyCycle(middle)
    time.sleep(0.5)



# servoPIN = 23
# GPIO.setmode(GPIO.BCM)
servoPIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)



print("start")
p.start(middle)


@asynccontextmanager
async def lifespan(app: FastAPI):
    p.stop(middle)
    GPIO.cleanup()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/servo/left-click")
def leftClick():
    clickLeft(p)
    return {"ok": True, "operation": "left-click"}

@app.put("/servo/right-click")
def rightClick():
    clickRight(p)
    return {"ok": True, "operation": "right-click"}




