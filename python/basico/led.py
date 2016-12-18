import RPi.GPIO as GPIO
import time

def blink( pin, delay ):

    on(pin)
    time.sleep(delay)
    off(pin)
    time.sleep(delay)

def on(pin):

    GPIO.output(pin, GPIO.HIGH)
    print("Led on")

def off(pin):
    
    GPIO.output(pin, GPIO.LOW)
    print("Led off")
