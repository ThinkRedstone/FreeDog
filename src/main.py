#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 13, 2015 2:03:09 PM$"
from gpsProcessing.gpsData import startGPS, getLongitude, getLatitude, closeGPS
from placment.circle import updatePosition
from control import engines
import os
from time import sleep
from sql.logger import startLogger, stopLogger

if __name__ == "__main__":
    startGPS()
    engines.setup()
    startLogger()
    try:
        while True:
            os.system('clear')
            print 'Long: ', getLongitude()
            print 'Lat: ', getLatitude()
            direction = updatePosition(getLongitude(),getLatitude())
            print 'Turn: ', direction
            engines.turn(direction, 1)
            sleep(1)
    except(KeyboardInterrupt, SystemExit):
		stopLogger()
		closeGPS()
	        print 'Exiting...'
