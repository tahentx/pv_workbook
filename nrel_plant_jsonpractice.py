import json
with open('data.json') as json_file:
    data = json.load(json_file)
for feature in data['features']:
    print(feature['properties']['projname'])
