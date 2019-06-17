from haversine import haversine
lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)
esb = (40.748440, -73.985664)
data = [lyon,paris,esb]

backups = []
for i in range(len(data)-1):
	backups.append(haversine(data[i], data[i +1],unit='mi'))

print(backups)
print(min(backups))
