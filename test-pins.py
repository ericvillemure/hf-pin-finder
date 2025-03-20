import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIOs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
         12, 13, 16, 17, 18, 19, 20, 21,
         22, 23, 24, 25, 26, 27]

try:
    # Setup all GPIOs to input
    for gpio in GPIOs:
        print("setup pin " + str(gpio))
        GPIO.setup(gpio, GPIO.IN)
        
    # Read state for each GPIO
    for gpio in GPIOs:
        print("GPIO no " + str(gpio) + ": " + str(GPIO.input(gpio)))

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print("keyboard")
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!")
  
finally:  
    GPIO.cleanup() # this ensures a clean exit      
