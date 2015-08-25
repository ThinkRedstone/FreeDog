import RPi.GPIO as GPIO
import time

##GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

def turnLeft():
	GPIO.output(19,True)
	time.sleep(2)
	GPIO.output(19,False)
	GPIO.output(16,True)
	time.sleep(2)
	GPIO.output(16,False)
	time.sleep(10)

def turnRight():
	GPIO.output(19,True)
	time.sleep(2)
	GPIO.output(19,False)
	GPIO.output(16,True)
	time.sleep(2)
	GPIO.output(16,False)
	time.sleep(10)

def notConnectedToServer():
        for x in range(0, 10):
                sleep(0.2)
                val = x%2==0
                GPIO.output(13,val)

def socketConnected():
        for x in range(0, 2):
                sleep(1)
                val = x%2==0
                GPIO.output(13,val)
