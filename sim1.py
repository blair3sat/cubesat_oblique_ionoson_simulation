import math

def phi(time):
    return 100000

def freqFromTime(t, dist):
    return freq(t-dist/c)

def inBounds1(time):
    return sX<=UpperBound1 and sX>=LowerBound1

def inBounds2(time):
    return sX<=UpperBound2 and sX>=LowerBound2

t = 0
tStep = 0.1
xVeloc = 1
c = 300000000 #meters per second
satYPos = 290
x1 = 290
y1 = 290
x2 = 290
y2 = 290
distance = 290
theta = 290
beta = 290
height = 290
freq = 0
LowerBound1 = (sY-y1)/math.tan(theta+beta)+x1
UpperBound1 = (sY-y1)/math.tan(beta)+x1
sX = (sY-y1)/math.tan(theta+beta)+x1
dataArr = []
while True:
    t += tStep
    sX += xVeloc
    LowerBound2 = (2*h-sY-y1)/math.tan(theta+beta)+x1
    UpperBound2 = (2*h-sY-y1)/math.tan(beta)+x1

    freq += phi(t) * tStep

    if inBounds1(t) and inBounds2(t):
        pass
    elif inBounds1(t):
        dataArr.append([t, freq])
    elif inBounds2(t):
        #TODO: figure out how to calculate the frequency after it has reflected
    else:
        pass

    #there was an empty todo here so rewrite the todo if you see this
    if noLongerNeedToSimulate:
        break

#TODO: Output the data to a text file and a graph
