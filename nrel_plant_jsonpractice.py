import json
with open('nrel-pv_plants.json') as json_file:
    data = json.load(json_file)
site = list(data["features"][0]["properties"])
test = data["features"][0:]
if "developer" in site:
    print("yes")

# for site in site.items():
#     print(site)
