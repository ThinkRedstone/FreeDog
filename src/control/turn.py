import RPi.GPIO as GPIO
import os
from time import sleep

# note: when done using motors call GPIO.cleanup(). when you want to reuse turn() functions call setup()

left_motor_a = 23  # left motor a pin number
left_motor_b = 24  # left motor b pin number
left_motor_e = 25  # left motor enable pin number
right_motor_e = 26  # right motor a pin number
right_motor_a = 35  # right motor b pin number
right_motor_b = 37  # right motor enable pin number
left_command_audio = "randomfile"  # honor left command audio file directory with filename
right_command_audio = "randomfile2"  # honor right command audio file directory with filename

def setup(*args):
    """
    IMPORTANT: always order pin numbers by a,b,e, must have a number of arguments that can be divided by 3 i.e. 3,6,9,12 etc.
    EXAMPLE: setup(left_motor_a, left_motor_b, left_motor_e, right_motor_a, right_motor_b, right_motor_e)
    :param args: some arguments
    """
    GPIO.setmode(GPIO.BCM)  # setup pin number references
    if len(args) > 0 and len(args) % 3 == 0:
        for n in args:
            GPIO.setup(n, GPIO.OUT)

'''
def setup():
    GPIO.setmode(GPIO.BCM)  # setup pin number references
    GPIO.setup(left_motor_a, GPIO.OUT)
    GPIO.setup(left_motor_b, GPIO.OUT)
    GPIO.setup(left_motor_e, GPIO.OUT)
    GPIO.setup(right_motor_a, GPIO.OUT)
    GPIO.setup(right_motor_b, GPIO.OUT)
    GPIO.setup(right_motor_e, GPIO.OUT)
'''

def playAudio(filename):
    os.system('mpg123 -q ' + filename + ' &')  # you must install mpg123 in order for this to work

def turnMotorOn(pin_number_e, pin_number_a, pin_number_b, turn_forward):
    if turn_forward:
        GPIO.output(pin_number_a, GPIO.HIGH)
        GPIO.output(pin_number_b, GPIO.LOW)
        GPIO.output(pin_number_e, GPIO.HIGH)
    else:
        GPIO.output(pin_number_a, GPIO.Low)
        GPIO.output(pin_number_b, GPIO.HIGH)
        GPIO.output(pin_number_e, GPIO.HIGH)

def turn_motor_off(pin_number_e):
    GPIO.output(pin_number_e, GPIO.LOW)

def turnMotorOff(pin_number_a, pin_number_b):
    GPIO.output(pin_number_a, GPIO.Low)
    GPIO.output(pin_number_b, GPIO.Low)
    
def pull(pin_number_e, pin_number_a, pin_number_b, elapse_time):
    """

    :param pin_number_e:
    :param pin_number_a:
    :param pin_number_b:
    :param elapse_time:
    """
    turn_motor_on(pin_number_e, pin_number_a, pin_number_b, True)
    sleep(elapse_time)
    turn_motor_off(pin_number_e)

def release(pin_number_e, pin_number_a, pin_number_b, elapse_time):
    """

    :param pin_number_e:
    :param pin_number_a:
    :param pin_number_b:
    :param elapse_time:
    """
    turn_motor_on(pin_number_e, pin_number_a, pin_number_b, False)
    sleep(elapse_time)
    turn_motor_off(pin_number_e)

def turn(direction="left", post_audio_elapse_time=1.5, motor_runtime_elapse_time=1.0):
    """
    :param direction:
        value either "left" or "right" to determine the turn direction of the dog
    :param post_audio_elapse_time:
        the amount of time to wait after audio was played to start turning the dog
    :param motor_runtime_elapse_time:
        the amount of time to run the motor
    """
    if direction is "left":
        play_audio(left_command_audio)
        sleep(post_audio_elapse_time)
        pull(left_motor_e, left_motor_a, left_motor_b, motor_runtime_elapse_time)
        release(left_motor_e, left_motor_a, left_motor_b, motor_runtime_elapse_time)
    else:
        play_audio(left_command_audio)
        sleep(post_audio_elapse_time)
        pull(right_motor_e, right_motor_a, right_motor_b, motor_runtime_elapse_time)
        release(right_motor_e, right_motor_a, right_motor_b, motor_runtime_elapse_time)

turnMotorOn(right_motor_e, right_motor_a, right_motor_b, True)
sleep(1.5)
turnMotorOn(right_motor_e, right_motor_a, right_motor_b, False)
sleep(1.5)
turnMotorOff(right_motor_a, right_motor_b)
sleep(1.5)