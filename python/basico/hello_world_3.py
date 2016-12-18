import RPi.GPIO as GPIO
import led as Led

led = 17
delay = 1

def setup():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

setup()

try:

    while True:

        Led.blink(led, delay)

except KeyboardInterrupt:
    
    GPIO.cleanup()
