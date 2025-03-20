# We imports the GPIO module
import RPi.GPIO as GPIO
# We import the command sleep from time
import time
import keyboard

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
time.sleep(5)


clickLeft(p)
clickRight(p)
clickLeft(p)
clickLeft(p)
clickLeft(p)
clickLeft(p)
clickRight(p)
# for duty in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
# for duty in range(25, 130, 5):
# for duty in [middle,left,middle,right,middle]:
#     print(duty)
#     p.ChangeDutyCycle(duty)
#     time.sleep(1)


print("end")

# print("middle")
# p.ChangeDutyCycle(middle)


p.stop(middle)
GPIO.cleanup()

# try:
# while True:
#     key = keyboard.read_key()
#     if (key == "a"):
#         print("left")
#         # p.ChangeDutyCycle(left)
#     elif (key == "d"):
#         print("right")
#         # p.ChangeDutyCycle(right)
#     else:
#         print("middle")
#         # p.ChangeDutyCycle(middle)


# except KeyboardInterrupt:
    # p.stop()
    # GPIO.cleanup()


