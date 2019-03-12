import json
with open('data.json') as json_file:
    data = json.load(json_file)
for feature in data['features']:
    if feature['properties']['developer'] == "SunPower":
        print(feature['properties']['projname'])

    # print(feature['properties']['projname'])
