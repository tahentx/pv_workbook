from haversine import haversine
lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)
esb = (40.748440, -73.985664)
group = [lyon,paris,esb]
for x in group:
	print(haversine(lyon,x,unit='mi'))
