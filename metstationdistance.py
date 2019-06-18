import csv
from haversine import haversine
with open('tucson.csv') as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)
    met = csv.reader(file)
    if has_header:
        next(met)
    met_list = list(met)
coords = []
for x in met_list:
    coords.append(x[1:])
backup_mets = []
for i in range(len(coords)-1):
	backup_mets.append(haversine(coords[i], coords[i + 1],unit='mi'))
#
print(backup_mets)
