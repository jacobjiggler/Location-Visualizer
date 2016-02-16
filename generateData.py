import os
import csv
import sys

school_lat_min = 42.728205
school_lat_max = 42.732396
school_long_min = -73.684845
school_long_max = -73.671747



def atSchool(latitude, longitude):
    if (latitude > school_lat_min and latitude < school_lat_max):
        if (longitude > school_long_min and longitude < school_long_max):
            return True
    return False

#print(atSchool(42.729320, -73.680688))


if __name__ == '__main__':
    #creates file named temp.dot
    #argv[0] is the file
    #argv[1] is the first csv file
    #argv[2] is optional and the second csv if you want to compare
    if (len(sys.argv) == 2):
        print("processing campus data")
    elif(len(sys.argv) == 3):
        print("comparing 2 datasets")
    else:
        print("usage: python generateData csv1 [optional csv2 for comparison]")
