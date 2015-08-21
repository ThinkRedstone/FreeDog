import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

def turnLeft():
	GPIO.output(19,True)
	time.sleep(1)
	GPIO.output(19,False)

def turnRight():
	GPIO.output(16,True)
	time.sleep(1)
	GPIO.output(16,False)
