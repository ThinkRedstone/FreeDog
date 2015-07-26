#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0


import os
from gps import *
from time import *
import time
import threading

gpsd = None #seting the global variable


class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd #bring it in scope
		gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
		self.current_value = None
		self.running = True #setting the thread running to true

	def run(self):
		global gpsd
		while gpsp.running:
			gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer


def startGPS():
    global gpsp 
    gpsp = GpsPoller()
    gpsp.start()
    
def getLongitude():
    global gpsd
    return gpsd.fix.longitude

def getLatitude():
    global gpsd
    return gpsd.fix.latitude

def closeGPS():#if you don't close the GPS, the programme won't stop as th gps inpt stream is still running
    global gpsp
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing

if __name__ == '__main__':
	gpsp = GpsPoller() # create the thread
	try:
                index=0
                gpsData=open("gpsData.txt", "w")
                
		gpsp.start() # start it up
		while True:
			#It may take a second or two to get good data
			#print gpsd.fix.latitude,', ',gpsd.fix.longitude,'	Time: ',gpsd.utc

			os.system('clear')

			print
			print ' GPS reading'
			print '----------------------------------------'
			print 'latitude    ' , gpsd.fix.latitude
			print 'longitude   ' , gpsd.fix.longitude
			print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
			print 'altitude (m)' , gpsd.fix.altitude
			print 'eps         ' , gpsd.fix.eps
			print 'epx         ' , gpsd.fix.epx
			print 'epv         ' , gpsd.fix.epv
			print 'ept         ' , gpsd.fix.ept
			print 'speed (m/s) ' , gpsd.fix.speed
			print 'climb       ' , gpsd.fix.climb
			print 'track       ' , gpsd.fix.track
			print 'mode        ' , gpsd.fix.mode
			print
			#print 'sats        ' , gpsd.satellites


                    
                        if gpsd.fix.latitude >0 :
                                
                                      
                                gpsData.write('index:{} '.format(index))
                                
                                gpsData.write(';  Latitude: ')
                                gpsData.write(str(gpsd.fix.latitude))
                                gpsData.write(';  longitude: ')
                                gpsData.write(str(gpsd.fix.longitude))
                                gpsData.write(';  altitude: ')
                                gpsData.write(str(gpsd.fix.altitude))
                                gpsData.write(';  speedMPS: ')
                                gpsData.write(str(gpsd.fix.speed))
                                gpsData.write(';  timeUTC: ')
                                gpsData.write(str(gpsd.fix.time))
                                gpsData.write('\n')

                                index=index+1
                              
			time.sleep(1) #set to whatever
                        
			

	except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
                gpsData.close
		print "\nKilling Thread..."
		gpsp.running = False
		gpsp.join() # wait for the thread to finish what it's doing
	print "Done.\nExiting."
