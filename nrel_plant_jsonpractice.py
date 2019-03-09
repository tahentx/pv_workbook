import json
with open('nrel-pv_plants.json') as json_file:
    data = json.load(json_file)
fleet = data["features"][0]["properties"]
site = data["features"][0]["properties"]["projname"]

fleet_list = data["features"]
for project in site:
    print(project)
#
# for developer in fleet:
#     if "developer" in fleet:
#         print("test")

# for site in site.items():
#     print(site)
