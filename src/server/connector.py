#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 13, 2015 2:03:09 PM$"
import socket
from gpsProcessing.gpsData import startGPS,getTime,getAltitude, getLongitude, getLatitude, closeGPS
from placment.circle import updatePosition
import RPi.GPIO as GPIO
from control import engines
from connectToServer import connectToServer
import os
import time
import traceback
from threading import Thread
##from sql.logger import startLogger, stopLogger
class Connector(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.index = 0
        print "Connecting to Server"
        host = '10.0.0.30'
        port = 11000
        self.connection = socket.socket()
        self.connection.connect((host,port))
        print "Socket connected"
    def run(self):
        while self.running:
            self.data = self.connection.recv(1024)
            print "Recived from server: " + str(data)
            sendData(index)
            index += 1

def startConncetion():
    global connector
    connector = Connector()
    startGPS()
    connector.start()
    
def closeConnection():
    global connector
    closeGPS()
    connector.running = False
    connector.join()
    
def sendData(index):
    global connector
    toSend = str(index) + ";" + str(getLongitude()) + ';' + str(getLatitude()) + ';' + str(getAltitude()) + ';' + getTime()
    print "Send to server " + toSend
    connector.connection.send(toSend)

def getData(place):
    global connector
    data = connector.data
    return data.split(";")[place]

def getUserLongitude():
    return getData(1)

def getUserLatitude():
    return getData(2)

def getDistance():
    return getData(6)

def getCommand():
    return getData(5)
    
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    startGPS()
    ##engines.setup()
    ##startLogger()
    while True:
        try:
            for x in range(0, 10):
                time.sleep(0.2)
                val = x%2==0
                GPIO.output(13,val)            
            print "Connecting to Server"
            host = '10.0.0.30'
            port = 11000
            s= socket.socket()
            s.connect((host,port))
            index = 0;
            print "Socket connected"
            GPIO.output(13,True)            
            while True:
                for x in range(0, 2):
                    time.sleep(1)
                    val = x%2==0
                    GPIO.output(13,val)
                
                toSend = str(index) + ";" + str(getLongitude()) + ';' + str(getLatitude())
                print "Send to server " + toSend
                s.send(toSend)

                data = s.recv(1024)                
                print "Recived from server: " + str(data)   
                                        
                if data == '1000;CONNECT_TO_RAS':
                    GPIO.output(13,True)
                    while data != '1000;DISCONNECT':
                        time.sleep(1)
                        toSend = str(index) + ";" + str(getLongitude()) + ';' + str(getLatitude())
                        print "Send to server " + toSend
                        s.send(toSend)

                        data = s.recv(1024)                
                        print "Recived from server: " + str(data)
                        if data == '1000;TURN_RIGHT':
                            GPIO.output(16,True)
                            time.sleep(1)
                            GPIO.output(16,False)
                        elif data == '1000;TURN_LEFT':
                            GPIO.output(19,True)
                            time.sleep(1)
                            GPIO.output(19,False)

                        index = index + 1
                ##direction = updatePosition(getLongitude(),getLatitude())
                ##print 'Turn: ', direction
                ##engines.turn(direction, 1)
                index = index + 1
        except Exception, err:
                    print(traceback.format_exc())
    ##		stopLogger()
              ##      closeGPS()
                    print 'Disconnected...'
