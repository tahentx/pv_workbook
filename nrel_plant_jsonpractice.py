import json
with open('nrel-pv_plants.json') as json_file:
    data = json.load(json_file)
linden = data["features"][0]["properties"].get("projname")
developer = data["features"][0]["properties"].get("developer")
site = data["features"][0]["properties"]
for site in site.items():
    developer = data["features"][0]["properties"].get("developer")
    print(developer)
