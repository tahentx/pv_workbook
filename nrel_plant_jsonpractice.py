import json
with open('nrel-pv_plants.json') as json_file:
    data = json.load(json_file)

features = data["features"]
linden = data["features"][0]["properties"].get("projname")
linden_developer = data["features"][0]["properties"].get("developer")
print("The first project in the NREL database is " + str(linden))
