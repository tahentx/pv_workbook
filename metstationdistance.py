import csv
from haversine import haversine
with open('tucson.csv') as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)
    met = csv.reader(file)
    if has_header:
        next(met)
    met_list = list(met)
print(met_list)
lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)
esb = (40.748440, -73.985664)
#
# backup_mets = []
# for i in range(len(met_list)-1):
# 	backup_mets.append(haversine(met_list[i], met_list[i + 1],unit='mi'))
#
# print(backups)
# print(min(backups))
#
# import csv v >>> exampleFile = open('example.csv') w >>> exampleReader = csv.reader(exampleFile) x >>> exampleData = list(exampleReader) y >>> exampleData
