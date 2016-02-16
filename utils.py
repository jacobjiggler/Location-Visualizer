import csv
import sys

class Point:
    def __init__(self, lat, lon, time, acc):
        self.lat = lat
        self.lon = lon
        self.time = time
        self.acc = acc

    def __str__(self):
        return "{lat: " + '%.7f'%self.lat + ", lon: " + '%.7f'%self.lon + ", time: " + '%.2f'%self.time + ", acc: " + str(self.acc) + "}"

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

def intersects(a0, a1, b0, b1):
    """
    Checks two line segments for intersection
    """
    #Coefficients for a0-a1
    aa = a0.lon - a1.lon
    ab = a1.lat - a0.lat
    ac = -(a0.lat * a1.lon - a1.lat * a0.lon)

    #Coefficients for b0-b1
    ba = b0.lon - b1.lon
    bb = b1.lat - b0.lat
    bc = -(b0.lat * b1.lon - b1.lat * b0.lon)

    #intersection
    d =  aa * bb - ab * ba
    dx = ac * bb - ab * bc
    dy = aa * bc - ac * ba
    if d != 0:
        x = dx / d
        y = dy / d
        time = a0.time + ((x - a0.lat) / (a1.lat - a0.lat)) * (a1.time - a0.time)
        return Point(x, y, time, 0)
    else:
        return False
