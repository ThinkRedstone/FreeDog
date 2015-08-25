# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "ThinkRedstone"
__date__ = "$06-Jul-2015 20:58:59$"
import math
userLong = 0
userLat = 0
previousLong = 0
previousLat = 0
currentLong = 0
currentLat = 0
turnRadius = 0
firstRun = True
#longtitute is x

def setUser(longitude, latitude):
    global userLong
    global userLat
    userLong = longitude
    userLat = latitude

def updatePosition(longitude, latitude):
    global firstRun
    global userLong
    global userLat 
    global previousLong 
    global previousLat 
    global currentLong 
    global currentLat 
    global turnRadius 
    if firstRun:
        previousLong = longitude - userLong
        previousLat = latitude - userLat
        #so we don't set the previous values to zero next run
        currentLong = previousLong
        currentLat = previousLat
        firstRun = False
        return "First run"
    else:
        previousLong = currentLong
        previousLat = currentLat
        #correct so we don't need to calculate big numbers
       
        currentLong = longitude - userLong
        currentLat = latitude - userLat
        if(checkPosition(latitude, longitude,userLat,userLong, turnRadius)):
            return turn(previousLong, previousLat, currentLong, currentLat)
        else:
            return "OK"


def checkPosition(lat1, long1, lat2, long2, turnRadius):
    
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    kilometerDist = arc * 6373
    meterDist = kilometerDist * 1000
    toReturn = meterDist > turnRadius
    print 'distance android to ras is ' + str(meterDist)
    return toReturn

#true for left, false for right
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
    
