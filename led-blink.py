#import
import RPi.GPIO as GPIO
import time

#definition
led = 14 #your PIN

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

#program
while True:
    GPIO.output(led, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led, GPIO.LOW)
    time.sleep(1)