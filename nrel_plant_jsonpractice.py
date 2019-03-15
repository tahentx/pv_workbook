import json
with open('data.json') as json_file:
    data = json.load(json_file)

# print project name
# for feature in data['features']:
#     if feature['properties']['developer'] == "SunPower":
#         print(feature['properties']['projname'])

# print california projects
# ca = []
# print("The California projects: ")
# for feature in data['features']:
#     if feature['properties']['state'] == "CA":
#         ca.append(feature)
#         print(feature['properties']['projname'] + " City: " + feature['properties']['city_cnty'] + " State: " + feature['properties']['state'])

ca = []
for feature in data['features']:
    if feature['properties']['developer'] == "SunPower":
        ca.append(feature)
        print(feature['properties']['projname'])
