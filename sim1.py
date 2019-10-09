import math
import time
import sys

def phi(time):
    return 100000

def freqFromTime(t, dist):
    return freq(t-dist/c)

def isInBoundsInitial():
    return satXPos <= initialSatEntrancePoint and satXPos >= initialSatExitPoint

def isInBoundsSecond():
    return satXPos <= secondSatEntrancePoint and satXPos >= secondSatExitPoint

def shouldContinueSimulation():
    return(satXpos >= secondSatExitPoint)

time = 0
tStep = 0.1
# Velocity in m / tstep
xVeloc = 100
c = 300000000 # meters per second (speed of light in vacuum)
satYPos = 100
satXPos = 0
# First boundry
distance = 290
# Degrees from the horizontal
lowerAngle = 10
upperAngle = 20
# Height that a given radio wave bounces off the ionosphere. Changes based on frequency.
heightOfWaveReflection = 2352345245435
initialFreq = 0
freq = initialFrequency
# Hz / second
chirpRate = 100000

# Figuring out upper and lower bounds of the ionosonde radio wave. Variable names confusing?
initialSatEntrancePoint = satYPos / tan(upperAngle)   # Leftmost point of non-reflected radio wave
initialSatExitPoint = satYPos / tan(lowerAngle)   # Rightmost point of non-reflected radio wave
finalSatEntrancePoint = (height - satYPos) / tan(upperAngle) # sat enters the area where it would be affected by the wave
finalSatExitPoint = (height - satYPos) / tan(lowerAngle)


frequencyToHeightConversionRate = 475 / 7000
dataArr = []
while True:
    initialFreq += chirpRate * 0.1
    time += tStep
    # The x component of the Sat is increased by its velocity every tstep
    satXPos += xVeloc
    heightOfWaveReflection = time * c / 2 # This isnt right yet
    secondSatEntrancePoint = (heightOfWaveReflection - satYPos) / tan(upperAngle)
    secondSatExitPoint = (heightOfWaveReflection - satYPos) / tan(lowerAngle)
    freq = time * chirpRate
    if inBoundsInitial():
        dataArr.append([time, freq])
    elif inBoundsSecond():
        dataArr.append([time,freq])    #TODO: figure out how to calculate the frequency after it has reflected
    elif inBoundsInitial() and inBoundsSecond():
        print "we don't know how to calculate what happens when the Sat is in this zone yet"
        sys.exit(2)
        # TODO figure out how to calculate frequency in this area
    else:
        pass
        # Not sensing anything
    # there was an empty todo here so rewrite the todo if you see this
    if shouldExitSimulation():
        break

#TODO: Output the data to a text file and a graph
