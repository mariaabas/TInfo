import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def encendre_pin():
	for i in range(0, 100000):
		GPIO.output(17, GPIO.HIGH)
		

encendre_pin()
