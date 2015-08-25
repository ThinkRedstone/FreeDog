#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 26, 2015 1:27:44 PM$"
from gpsProcessing.gpsData import closeGPS
from gpsProcessing.gpsData import getLatitude
from gpsProcessing.gpsData import getLongitude
from gpsProcessing.gpsData import getTime
from gpsProcessing.gpsData import startGPS
from server.connector import *
from sqlProcessing import *
from threading import Thread
from time import sleep

class Logger(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.index = 0
    def run(self):
        while self.running:
            log(self.index)
            self.index += 1
            sleep(1)
            
def log(index):
    execute("insert into log values(%d,%d,%d,%d,%s,%d,%d,%s,%d)" % (index, getLongitude(), getLatitude(), getTime(), getUserLatitude(), getUserLongtitude(), getCommand(), getDistance()))

def startLogger():
    startConnection("test")
    deleteTable("log")
    createTable("log")
    global logger
    startGPS()
    logger = Logger()
    logger.start()
    
def stopLogger():
    global logger
    closeGPS()
    logger.running = False
    logger.join()
    
def createTable(name):
    execute("create table " + name + "(ind int,longtitude double, latitude double, altitude double, time varchar(50), userLong double, userLat double, command varchar(20), distance double")

def deleteTable(name):
    execute("drop table " + name)

if __name__ == "__main__":
    startLogger()
    sleep(15)
    stopLogger()
