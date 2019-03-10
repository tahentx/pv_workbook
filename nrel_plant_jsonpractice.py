import json
with open('nrel-pv_plants.json') as json_file:
    data = json.load(json_file)
fleet_list = data["features"]
site = data["features"][0]["properties"]
for site in site.items():
    print(site)
