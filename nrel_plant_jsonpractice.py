import json
with open('data.json') as json_file:
    data = json.load(json_file)
# for feature in data['features']:
#     if feature['properties']['developer'] == "SunPower":
#         print(feature['properties']['projname'])
ca = []
print("The California projects: ")
for feature in data['features']:
    if feature['properties']['state'] == "CA":
        ca.append(feature)
        print(feature['properties']['projname'] + " City: " + feature['properties']['city_cnty'] + " State: " + feature['properties']['state'])
