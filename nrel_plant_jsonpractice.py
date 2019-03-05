import json
with open('nrel-pv_plants.json') as json_file:
    plants = json.load(json_file)

print(plants)
