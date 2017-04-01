import csv
import math
from graphics import *

def toRad(x):
    return x*math.pi/180.0;

def distanceMiles(lat1, long1, lat2, long2):
    R = 3958.7558657440545
    dLat = toRad(lat2-lat1)
    dLon = toRad(long2-long1)
    lat1 = toRad(lat1)
    lat2 = toRad(lat2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
    math.sin(dLon/2) * math.sin(dLon/2) * \
    math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return (d)

def Filter(longitude,latitude,distance):
    file = open('estate.csv','r')
    dRdr = csv.DictReader(file)
    price = []
    bedroom = []
    bathroom = []
    total = 0
    for row in dRdr:
        if (distanceMiles(latitude,longitude,float(row['latitude']),float(row['longitude'])) <= distance):
            total = total + 1
            price.append(int(row['price']))
            bedroom.append(int(row['beds']))
            bathroom.append(int(row['baths']))
    file.close()
    return total,price,bedroom,bathroom

def median(data):
    data.sort()
    if (len(data)%2) == 1:
        median = data[int((len(data)-1)/2)]
    else:
        median = (data[int(len(data)/2)] + data[int((len(data)/2)-1)])/2
    return median

def mean(data):
    total = 0
    for i in range(len(data)):
        total = total + data[i]
    mean = total/(len(data))
    return mean

def report(longitude,latitude,distance):
    data = Filter(longitude,latitude,distance)
    file = open('Data Report.txt','w')
    file.write('The location longitude is ')
    file.write(str(longitude))
    file.write(' and latitude is ')
    file.write(str(latitude))
    file.write('.\nThe distance around the location is ')
    file.write(str(distance))
    file.write(' miles.\nThe total number of residences sold is ')
    file.write(str(data[0]))
    file.write('.\nThe highest selling price is ')
    file.write(str(max(data[1])))
    file.write(', lowest is ')
    file.write(str(min(data[1])))
    file.write('.\nThe mean selling price is ')
    file.write(str(mean(data[1])))
    file.write(', median is ')
    file.write(str(median(data[1])))
    file.write('.\nThe mean number of bedrooms is ')
    file.write(str(mean(data[2])))
    file.write(', bathrooms is ')
    file.write(str(mean(data[3])))
    file.write('.')
    file.close()
    return

def interact():
    from HW6_Map import initializeMap
    win = initializeMap('Map.png',707,744)
    message1 = Text(Point(200,100),"Click to choose location")
    message1.draw(win)
    message1.undraw
    p1 = win.getMouse()    
    click1 = pixel(float(p1.getX()),float(p1.getY()))
    message2 = Text(Point(354,765),"Click again to choose distance from location")
    message2.draw(win)
    p2 = win.getMouse()
    message2.undraw
    click2 = pixel(float(p2.getX()),float(p2.getY()))
    distance = distanceMiles(click1[0],click1[1],click2[0],click2[1])
    return click1[0],click1[1],distance,win

def makeLocation():
    from HW6_Map import color1
    data = interact()
    file = open('estate.csv','r')
    dRdr = csv.DictReader('estate.csv')
    x = []
    y = []
    price = []
    for row in dRdr:
        if (distanceMiles(data[0],data[1],float(row['latitude']),float(row['longitude'])) <= distance):
            coords = LatLongToPixels(float(row['latitude']),float(row['longitude']))
            x.append(coords[0])
            y.append(coords[1])
            price.append(int(row['price']))
    file.close()
    return x,y,color1(price),data[3]

def extraCircle():
    from HW6_Map import keyEstate
    data = makeLocation()
    win = data[3]
    keyEstate(win)
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

def pixel(x,y):
    lat = 38.24 + ((39.03-38.24)/744.0)*y
    long = 120.6 + ((121.56-120.6)/707.0)*x
    return lat,long
    
def LatLongToPixels(latitude, longitude):
    y = (744.0/(39.03-38.24))*(abs(latitude) - 38.24)
    x = (707.0/(121.56-120.6))*(abs(longitude) - 120.6)
    return x,y
