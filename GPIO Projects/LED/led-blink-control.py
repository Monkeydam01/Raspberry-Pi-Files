#import
import RPi.GPIO as GPIO
import time

#led
led = 14
sol = 0

#definition
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

#program
GPIO.output(led, GPIO.LOW)
print("Welcome to the LED!")

while True:
    imput = input("What do you want to do? (on/off)")
    
    if(imput == "on"):
        if(sol == 0):
            GPIO.output(led, GPIO.HIGH)
            sol = 1
        
        else:
            print("The LED is already on!")
            
    elif(imput == "off"):
        if(sol == 1):
            GPIO.output(led, GPIO.LOW)
            sol = 0
            
        else:
            print("The LED is already off!")
            
    else:
        print("ERROR")