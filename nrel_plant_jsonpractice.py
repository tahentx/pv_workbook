import json
with open('data.json') as json_file:
    data = json.load(json_file)
# for feature in data['features']:
#     if feature['properties']['developer'] == "SunPower":
#         print(feature['properties']['projname'])
ca = []
for feature in data['features']:
    if feature['properties']['state'] == "CA":
        ca.append(feature)

print("The California projects: ")
