import RPi.GPIO as GPIO
import time

PIR    = 23
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

try:
    while True:
        time.sleep(1)
        if GPIO.input(PIR) == 1:
            print("Motion detected")
        else:
            print("No motion detected")
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()