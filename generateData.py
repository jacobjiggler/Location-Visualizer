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

office_lat_min = 42.720513
office_lat_max = 42.721600
office_long_min = -73.693628
office_long_max = -73.693307

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
#print(atOffice(42.721083, -73.693382))




pt1 = Point(school_lat_min, school_long_min, 1234567, 0)
pt2 = Point(school_lat_max, school_long_max, 1234599, 0)
pt3 = Point(school_lat_min, school_long_max, 1234568, 0)
pt4 = Point(school_lat_max, school_long_min, 1234569, 0)

print (lerp(pt1, pt2, 1234588))

print (intersects(pt1, pt2, pt3, pt4))

def analyzeLocationData(csv):
    wrap = CsvWrapper(csv)
    point = wrap.getPoint()
    print(point.lat)
    schoolCount = 0
    crowsCount = 0
    officeCount = 0

def analyzeMeetups(csv1,csv2):
    meetingPoints = []


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
