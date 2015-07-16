#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 13, 2015 2:03:09 PM$"
from gpsProcessing.gpsData import startGPS, getLongitude, getLatitude, closeGPS

if __name__ == "__main__":
    startGPS()
    try:
        while True:
            print getLongitude()
            print getLatitude()
    except(KeyboardInterrupt, SystemExit):
        closeGPS()
        print 'Exiting...'
