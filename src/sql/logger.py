#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 26, 2015 1:27:44 PM$"
from gpsProcessing.gpsData import closeGPS
from gpsProcessing.gpsData import getLatitude
from gpsProcessing.gpsData import getLongitude
from gpsProcessing.gpsData import startGPS
from sqlProcessing import *
from threading import Thread
from time import sleep

class Logger(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        startConnection("test")
        self.index = 0
    def run(self):
        while self.running:
            log(self.index)
            self.index += 1
            sleep(1)
            
def log(index):
    execute("insert into log values(%d,%d,%d)" % (index, getLongitude(), getLatitude()))
    
def startLogger():
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
    execute("create table " + name + "(ind int, longitude double, latitude double)")

def deleteTable(name):
    execute("drop table " + name)

if __name__ == "__main__":
    startLogger()
    sleep(15)
    stopLogger()
