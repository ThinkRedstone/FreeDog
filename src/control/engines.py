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

def notConnectedToServer():
        for x in range(0, 10):
                time.sleep(0.2)
                val = x%2==0
                GPIO.output(13,val)

def socketConnected():
        for x in range(0, 2):
                time.sleep(1)
                val = x%2==0
                GPIO.output(13,val)
