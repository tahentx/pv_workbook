import json
with open('nrel-pv_plants.json') as json_file:
    data = json.load(json_file)
print(data)
