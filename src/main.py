#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 13, 2015 2:03:09 PM$"
from gpsProcessing.gpsData import *
from placment.circle import *
from server.connector import *
from control.engines import *
import os
from time import sleep

if __name__ == "__main__":
    
##    startGPS()
    startConnection()
    try:
        while True:
##            os.system('clear')            
##            print 'Long: ', getLongitude()  #from raspberry
##            print 'Lat: ', getLatitude() #from raspberry
            setUser(getUserLongtitude(),getUserLatitude()) #from client
            turnRadius = getDistance()
            direction = updatePosition(getLongitude(),getLatitude())
##            print 'Turn: ', direction
            if((direction == 'left') or (getCommand() is 'TURN_LEFT')):
                print 'turn Left'
                turnLeft()                 
            if((direction == 'right') or (getCommand() is 'TURN_RIGHT')):
                print 'turn Right'
                turnRight()
                

           
    except(KeyboardInterrupt, SystemExit):
        closeConnection()
        closeGPS()
        print 'Exiting...'
