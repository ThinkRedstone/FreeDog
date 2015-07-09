import os
from time import sleep
import RPi.GPIO as GPIO

motor_number1 = 23
motor_number2 = 24

def setup():
    GPIO.setmode(GPIO.BCM)  # setup pin number references
    GPIO.setup(motor_number1, GPIO.OUT)
    GPIO.setup(motor_number2, GPIO.OUT)

def play_audio(filename):
    os.system('mpg123 -q ' + filename + '&')
