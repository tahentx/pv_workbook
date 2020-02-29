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

print(coords)
#
# def find_backup_metstation(coordinates: list) -> list:
#     backup_mets = []
#     for i in range(len(coordinates)-1):
#     	backup_mets.append(haversine(coordinates[i], coordinates[i + 1],unit='mi'))
#     print(type(coordinates[i]))
#
# find_backup_metstation(coords)
