import statistics
import json
from random import *
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


# Find all of the SPWR projects, and alphabetize them
# ca = []
# for feature in data['features']:
#     if feature['properties']['developer'] == "SunPower":
        # ca.append(feature['properties']['projname'])
# ca.sort()
# print("The SunPower pojects in the NREL data set: " + str(ca))

# capacity = []
# for feature in data['features']:
#     capacity.append(feature['properties']['cap_mw'])
# avg = statistics.mean(capacity)
# std = statistics.pstdev(capacity)
# print("The average system size (MWdc) in NREL database: " + str(avg))

# public = []
# private = []
# unspecified = []
# for feature in data['features']:
#     if feature['properties']['landtype'] == "Private":
#         private.append(feature['properties']['projname'])
#     elif feature['properties']['landtype'] == "Public":
#         public.append(feature['properties']['projname'])
#     else:
#         unspecified.append(feature['properties']['projname'])
#
# print("There are " + str(len(public)) + " C&I projects on public land in the dataset.")
# print(len(private))

for feauture in data['features']:
    feauture['properties']['budget'] = randint(20000,30000)
    feauture['properties']['spend'] = randint(5000,12500)

west = []
east = []
for feature in data['features']:
    if feature['properties']['state'] == "CA":
        west.append(feature['properties'])
    elif feature['properties']['state'] == "NJ" or "NY" or "PA":
        east.append(feature['properties'])

print(east[0]['budget'])
