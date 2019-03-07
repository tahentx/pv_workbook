import json
with open('nrel-pv_plants.json') as json_file:
    data = json.load(json_file)

features = data["features"]
linden = data["features"][0].get("type")
print(linden)
