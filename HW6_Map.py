import graphics
from graphics import *

def initializeMap(mapFile, xPixels, yPixels):
    win = graphics.GraphWin('Sacramento Area', xPixels, yPixels)
    win.setCoords(0, 0, xPixels, yPixels)
    center = graphics.Point(xPixels/2, yPixels/2)
    image = graphics.Image(center, mapFile)
    image.draw(win)
    return win

def LatLongToPixels(latitude, longitude):
    y = (744.0/(39.03-38.24))*(abs(latitude) - 38.24)
    x = (707.0/(121.56-120.6))*(abs(longitude) - 120.6)
    return x,y

def readData1(dataFile):
    import csv
    x = []
    y = []
    price = []
    file = open(dataFile,'r')
    dRdr = csv.DictReader(file)
    for row in dRdr:
        coords = LatLongToPixels(float(row['latitude']),float(row['longitude']))
        x.append(coords[0])
        y.append(coords[1])
        price.append(int(row['price']))
    file.close()
    return x,y,color1(price)

def color1(price):
    color = []
    for i in range(len(price)):
        if price[i] < 100000:
            color.append('red')
        elif price[i] <= 200000:
            color.append('orange')
        elif price[i] <= 300000:
            color.append('yellow')
        elif price[i] <= 400000:
            color.append('green')
        elif price[i] <= 500000:
            color.append('blue')
        elif price[i] <= 600000:
            color.append('indigo')
        else:
            color.append('violet')
    return color

def keyEstate(win):
    color = ['red','orange','yellow','green','blue','indigo','violet']
    rec = Rectangle(Point(500,150),Point(704,0))
    rec.draw(win)
    rec.setFill('cyan')
    Text(Point(600,135), "<$100,000").draw(win)
    Text(Point(600,115), '$100,000-$200,000').draw(win)
    Text(Point(600,95), "$200,000-$300,000").draw(win)
    Text(Point(600,75), "$300,000-$400,000").draw(win)
    Text(Point(600,55), "$400,000-$500,000").draw(win)
    Text(Point(600,35), "$500,000-$600,000").draw(win)
    Text(Point(600,15), ">$600,000").draw(win)
    for i in range(7):
        locate = Point(680,int(135-(20*i)))
        circ = Circle(locate,4)
        circ.draw(win)
        circ.setFill(color[i])
        circ.setOutline(color[i])
    return
    

def circles1(mapFile, xPixels, yPixels, dataFile):
    win = initializeMap(mapFile, xPixels, yPixels)
    keyEstate(win)
    data = readData1(dataFile)
    x = data[0]
    y = data[1]
    color = data[2]
    for i in range (len(data[0])):
        locate = Point(x[i],y[i])
        circ = Circle(locate,4)
        circ.draw(win)
        circ.setFill(color[i])
        circ.setOutline(color[i])
    return

def readData2(dataFile):
    import csv
    x = []
    y = []
    measure = []
    file = open(dataFile,'r')
    dRdr = csv.DictReader(file)
    for row in dRdr:
        coords = LatLongToPixels(float(row['latitude']),float(row['longitude']))
        x.append(coords[0])
        y.append(coords[1])
        measure.append(int(row['ucr_ncic_code']))
    file.close()
    return x,y,color2(measure)

def color2(crime):
    color = []
    for i in range(len(crime)):
        if crime[i] < 1000:
            color.append('cyan')
        elif crime[i] < 2000:
            color.append('pink')
        elif crime[i] < 3000:
            color.append('yellow')
        elif crime[i] < 4000:
            color.append('blue')
        elif crime[i] < 5000:
            color.append('purple')
        elif crime[i] < 6000:
            color.append('brown')
        else:
            color.append('black')
    return color

def keyCrime(win):
    color = ['cyan','pink','yellow','blue','purple','brown','black']
    rec = Rectangle(Point(420,150),Point(704,0))
    rec.draw(win)
    rec.setFill('green')
    Text(Point(550,135), "homicide/manslaughterer").draw(win)
    Text(Point(550,115), 'robbery/violence').draw(win)
    Text(Point(550,95), "thievery/burglary/fraud/vandalism").draw(win)
    Text(Point(550,75), "drug related").draw(win)
    Text(Point(550,55), "prostitution/resist officer").draw(win)
    Text(Point(550,35), "traffic accidents/threats").draw(win)
    Text(Point(550,15), "other crimes").draw(win)
    for i in range(7):
        locate = Point(680,int(135-(20*i)))
        circ = Circle(locate,4)
        circ.draw(win)
        circ.setFill(color[i])
        circ.setOutline(color[i])
    return

def circles2(mapFile, xPixels, yPixels, dataFile):
    win = initializeMap(mapFile, xPixels, yPixels)
    keyCrime(win)
    data = readData2(dataFile)
    x = data[0]
    y = data[1]
    color = data[2]
    for i in range (len(data[0])):
        locate = Point(x[i],y[i])
        circ = Circle(locate,4)
        circ.draw(win)
        circ.setFill(color[i])
        circ.setOutline(color[i])
    return
