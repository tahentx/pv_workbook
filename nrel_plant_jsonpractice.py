import json
with open('nrel-pv_plants.json') as json_file:
    plants = json.load(json_file)


# count = plants["features"].count("projname")
# print(count)
sites = []
for i in plants:
    sites.append(plants["features"][0]["properties"])
print(sites)
