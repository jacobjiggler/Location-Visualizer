import json
import csv

print("Opening location history data...")

inf = open("Takeout/LocationHistory.json", 'r')
in_data = json.load(inf)
inf.close()

print("Parsing...")

out_data = []
for x in in_data["locations"]:
	out_row = [x["latitudeE7"], x["longitudeE7"], x["timestampMs"], x["accuracy"]]
	out_data.append(out_row)

print("Outputting to CSV...")

of = open("Takeout/parsed.csv", 'w', newline='\n')
csv_file = csv.writer(of)
csv_file.writerow(["lat","lon","time","accuracy"])
for x in out_data:
	csv_file.writerow(x)

print("Done")
	