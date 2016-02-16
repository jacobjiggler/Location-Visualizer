import csv
import sys

class Point:
    def __init__(self, lat, lon, time, acc):
        self.lat = lat
        self.lon = lon
        self.time = time
        self.acc = acc

class CsvWrapper:
	def __init__(self, file):
		with open(file) as csvfile:
			self.points = []
			self.itr = 0
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if (len(row) != 4):
					print("error")
				else:
					points.append(Point(row[0],row[1],row[2],row[3]))

	def getPoint():
		itr+=1
		return points[itr-1]

def lerp(a, b, time):
	"""
	Takes two (lat, lon, time) tuples a and b, and a tmestamp between a and b
	and returns a tuple with the lat and lon at that new time.
	"""
	dlat = b.lat - a.lat
	dlon = b.lon - a.lon
	dt = (time - a.time) / (b.time - a.time)



	return (a.lat + dt * dlat, a.lon + dt * dlon, time)
