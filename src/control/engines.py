import RPi.GPIO as GPIO
from threading import Thread
import time


connectionLed = 13
runningLed = 14
leftMotor = 19
rightMotor = 16

##GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(connectionLed,GPIO.OUT)
GPIO.setup(runningLed,GPIO.OUT)
GPIO.setup(leftMotor,GPIO.OUT)
GPIO.setup(rightMotor,GPIO.OUT)

class ConnectionLight(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        self.running = True
        global connectionLed
        val = True
        for x in range(0, 2):
            sleep(1)
            val = not val
            GPIO.output(connectionLed, val)
        self.running = False

class RunningLight(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        self.running = True
        global runningLed
        GPIO.output(runningLed, True)
        sleep(1)
        GPIO.output(runningLed, False)
        sleep(5)
        self.running = False

def turnLeft():
    GPIO.output(leftMotor, True)
    time.sleep(2)
    GPIO.output(leftMotor, False)
    GPIO.output(rightMotor, True)
    time.sleep(2)
    GPIO.output(rightMotor, False)
    time.sleep(10)

def turnRight():
    GPIO.output(rightMotor, True)
    time.sleep(2)
    GPIO.output(rightMotor, False)
    GPIO.output(leftMotor, True)
    time.sleep(2)
    GPIO.output(leftMotor, False)
    time.sleep(10)

def runningLights():
    global runLightThread
    try:
        if not runLightThread.running:
            runLightThread = RunningLight()
            runLightThread.start()
    finally:
        runLightThread = RunningLight()
        runLightThread.start()

def socketConnectedLights():
    global connectionLightThread
    try:
        if not connectionLightThread.running:
            connectionLightThread = ConnectionLight()
            connectionLightThread.start()
    finally:
        connectionLightThread = ConnectionLights()
        connectionLightThread.start()
