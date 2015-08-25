#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 13, 2015 2:03:09 PM$"
import socket
from gpsProcessing.gpsData import startGPS,getTime,getAltitude, getLongitude, getLatitude, closeGPS
from placment.circle import updatePosition
from control import engines
import os
import time
import traceback
from threading import Thread
##from sql.logger import startLogger, stopLogger
received = ''
class Connector(Thread):
        
    def __init__(self):
        
        Thread.__init__(self)
        
        
    def run(self):
        global received
        self.running = True
        print "Connecting to Server"
        host = '10.0.0.30'
##        host = '91.205.155.231'
        port = 11000

        while self.running:
            self.index = 0
            
            try:
                self.connection = socket.socket()
                self.connection.connect((host,port))
                print "Socket connected"

                while self.running:
                
                
                    for x in range(0, 10):
                        time.sleep(0.1)

        ##            sendData(index)
                          
                    self.toSend = str(self.index) + ";" + str(getLongitude()) + ';' + str(getLatitude()) + ';' + str(getAltitude()) + ';' + str(getTime())
                    print "Send to server " + self.toSend
                    self.connection.send(self.toSend)
                    
                    received = self.connection.recv(1024)
                    print "Recived from server: " + str(received)
        ##            sendData(index)
                    self.index += 1
            except Exception, err:
                    print(traceback.format_exc())                
                
    
def startConnection():
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
    
    global received
    try:
        ##print 'Data: ' + received
        splitted = received.split(";")
        if len(splitted) > place:
            try:
                return float(splitted[place])
            except:
                return 0
        else:
            return 0
    except Exception, err:
        print(traceback.format_exc())
        print 'Data Error'
        return 0

def getUserLongtitude():
    return getData(3)   

def getUserLatitude():   
    return getData(2)

def getUserUTCseconds():   
    return getData(1)

def getDistance():    
    return getData(6)

def getCommand():   
    return getData(5)
    
##if __name__ == "__main__":    
##    
##    startGPS()
##    ##engines.setup()
##    ##startLogger()
##    while True:
##        try:
##            notConnectedToServer()           
##            print "Connecting to Server"
##            host = '10.0.0.30'
##            port = 11000
##            s= socket.socket()
##            s.connect((host,port))
##            index = 0;
##            print "Socket connected"
####            GPIO.output(13,True)            
##            while True:               
##                socketConnected()
##                toSend = str(index) + ";" + str(getLongitude()) + ';' + str(getLatitude())
##                print "Send to server " + toSend
##                s.send(toSend)
##
##                data = s.recv(1024)                
##                print "Recived from server: " + str(data)   
##                index = index + 1
##                
##        except Exception, err:
##                    print(traceback.format_exc())
##    ##		stopLogger()
##              ##      closeGPS()
##                    print 'Disconnected...'
##
