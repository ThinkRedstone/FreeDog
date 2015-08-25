#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 13, 2015 2:03:09 PM$"
from gpsProcessing.gpsData import *
from placment.circle import updatePosition
from server.connector import *
from control.engines import *
import os
from time import sleep
from sql.logger import startLogger, stopLogger

if __name__ == "__main__":
    startGPS()
    startConnection()
    try:
        while True:
            os.system('clear')
            print 'Long: ', getLongitude()
            print 'Lat: ', getLatitude()
            updateUser(getUserLongtitude(),getUserLatitude())
            turnRadius = getDistance()
            direction = updatePosition(getLongitude(),getLatitude())
            print 'Turn: ', direction
            if(direction is 'left' || getCommand() is 'TURN_LEFT':
                turnLeft()
            if(direction is 'right' || getCommand is 'TURN_RIGHT':
                turnRight()
    except(KeyboardInterrupt, SystemExit):
        closeConnection()
        closeGPS()
        print 'Exiting...'
