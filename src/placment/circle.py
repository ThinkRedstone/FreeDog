# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "ThinkRedstone"
__date__ = "$06-Jul-2015 20:58:59$"
from math import *
userLong = 0
userLat = 0
previousLong = 0
previousLat = 0
currentLong = 0
currentLat = 0
turnRadius = 0
firstRun = True
#longtitute is x

def setUser(long, lat):
    global userLong
    global userLat
    userLong = long
    userLat = lat

def updatePosition(long, lat):
    global firstRun
    global userLong
    global userLat 
    global previousLong 
    global previousLat 
    global currentLong 
    global currentLat 
    global turnRadius 
    if firstRun:
        previousLong = long - userLong
        previousLat = lat - userLat
        #So we don't set the previous values to zero next run
        currentLong = previousLong
        currentLat = previousLat
        firstRun = False
        return "First run"
    else:
        previousLong = currentLong
        previousLat = currentLat
        #Correct so we don't need to calculate big numbers
        currentLong = long - userLong
        currentLat = lat - userLat
        if(checkPosition(currentLat, currentLong, turnRadius)):
            return turn(previousLong, previousLat, currentLong, currentLat)
        else:
            return "OK"


def checkPosition(currentLat, currentLong, turnRadius): #Returns true if outside turn radius
    return sqrt(currentLat ** 2 + currentLong ** 2) > turnRadius

def turn(previousLong, previousLat, currentLong, currentLat):
    if currentLong > 0:
        if previousLat > (currentLat / currentLong) * previousLong:
            return "left"
        else:
            return "right"
    else:
        if previousLat > (currentLat / currentLong) * previousLong:
            return "right"
        else:
            return "left"
    
