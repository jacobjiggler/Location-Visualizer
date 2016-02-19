import os
import csv
import sys

from utils import *

school_lat_min = 42.728205
school_lat_max = 42.732396
school_long_min = -73.684845
school_long_max = -73.671747

crows_lat_min = 42.723935
crows_lat_max = 42.724788
crows_long_min = -73.672665
crows_long_max = -73.672150

robhome_lat_min = 42.732189
robhome_lat_max = 42.732829
robhome_long_min = -73.688261
robhome_long_max = -73.687419

chiphi_lat_min = 42.730768
chiphi_lat_max = 42.731476
chiphi_long_min = -73.677751
chiphi_long_max = -73.677082

office_lat_min = 42.732104
office_lat_max = 42.732778
office_long_min = -73.691276
office_long_max = -73.689881

def atSchool(latitude, longitude):
    if (latitude > school_lat_min and latitude < school_lat_max):
        if (longitude > school_long_min and longitude < school_long_max):
            return True
    return False
    
def atCrows(latitude, longitude):
    if (latitude > crows_lat_min and latitude < crows_lat_max):
        if (longitude > crows_long_min and longitude < crows_long_max):
            return True
    return False

def atRobHome(latitude, longitude):
    if (latitude > robhome_lat_min and latitude < robhome_lat_max):
        if (longitude > robhome_long_min and longitude < robhome_long_max):
            return True
    return False
    
def atChiPhi(latitude, longitude):
    if (latitude > chiphi_lat_min and latitude < chiphi_lat_max):
        if (longitude > chiphi_long_min and longitude < chiphi_long_max):
            return True
    return False

def atOffice(latitude, longitude):
    if (latitude > office_lat_min and latitude < office_lat_max):
        if (longitude > office_long_min and longitude < office_long_max):
            return True
    return False

#should return true
#print(atSchool(42.729320, -73.680688))
#also true
#print(atCrows(42.724140, -73.673135))
#should return false
#print(atCrows(42.724558, -73.672563))
#should return true
#print(atOffice(42.73250, -73.690))

def analyzeLocationData(csvData):
    otherCount = 0
    schoolCount = 0
    crowsCount = 0
    officeCount = 0
    chiphiCount = 0
    robhomeCount = 0
    otherCount = 0
    wrap = CsvWrapper(csvData)
    point = wrap.getPoint()
    if (point == None):
        return
    while(point != None):
        #print(point.lat)
        lat = float(point.lat)
        lon = float(point.lon)
        #chiphi before school because it's contained in the school bounds
        if (atChiPhi(lat, lon)):
            chiphiCount+=1
        elif (atSchool(lat, lon)):
            schoolCount+=1
        elif (atCrows(lat, lon)):
            crowsCount+=1
        elif (atOffice(lat, lon)):
            officeCount+=1
        elif (atRobHome(lat, lon)):
            robhomeCount+=1
        else:
            otherCount+=1
        point = wrap.getPoint()
    print("school count: " + str(schoolCount))
    print("crows count: " + str(crowsCount))
    print("office count: " + str(officeCount))
    print("Chi Phi count: " + str(chiphiCount))
    print("Rob Home count:" + str(robhomeCount))
    print("other location count: " + str(otherCount))
    with open('locationCounts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["school count", "crows count", "office count", "chi phi count", "rob home count", "other count"])
        writer.writerow([schoolCount] + [crowsCount] + [officeCount] + [chiphiCount] + [robhomeCount] + [otherCount])


def analyzeMeetups(csv1,csv2):
    dists = []
    crosses = []
    a = CsvWrapper(csv1)
    b = CsvWrapper(csv2)
    
    #reverse order so they are in chronological order.
    a.flip()
    b.flip()
    
    prevAp = a.getPoint()
    prevBp = b.getPoint()
    ap = a.getPoint()
    bp = b.getPoint()
    
    #Make sure starting times are similar
    if prevAp.time < prevBp.time:
        while ap.time < prevBp.time:
            prevAp = ap
            ap = a.getPoint()
    elif prevBp.time < prevAp.time:
        while bp.time < prevAp.time:
            prevBp = bp
            bp = b.getPoint()
    
    if ap is None or bp is None:
        print("wat")
        return
    
    while True:
    
        #lerp to get position at the same time
        #bpl = lerp(prevBp, bp, ap.time)
        dists.append((ap.time, distance(ap, bp)))
        
        intersection = intersects(prevAp, ap, prevBp, bp)
        if intersection != False:
            crosses.append(intersection)
    
        prevAp = ap
        prevBp = bp
        ap = a.getPoint()
        bp = b.getPoint()
        
        if ap is None or bp is None:
            break

    with open('dists.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["time", "distance"])
        for d in dists:
            writer.writerow([d[0], d[1]])

if __name__ == '__main__':
    #creates file named temp.dot
    #argv[0] is the file
    #argv[1] is the first csv file
    #argv[2] is optional and the second csv if you want to compare
    if (len(sys.argv) == 2):
        print("processing location data")
        analyzeLocationData(sys.argv[1])

    elif(len(sys.argv) == 3):
        print("comparing 2 datasets")
        analyzeMeetups(sys.argv[1], sys.argv[2])
    else:
        print("usage: python generateData csv1 [optional csv2 for comparison]")
