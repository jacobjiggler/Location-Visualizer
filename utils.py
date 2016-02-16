def lerp(a, b, time):
	"""
	Takes two (lat, lon, time) tuples a and b, and a tmestamp between a and b
	and returns a tuple with the lat and lon at that new time.
	"""
	dlat = b.lat - a.lat
	dlon = b.lon - a.lon
	dt = (time - a.time) / (b.time - a.time)
	
	
	
	return (a.lat + dt * dlat, a.lon + dt * dlon, time)