# import pandas as pd
# from opencage.geocoder import OpenCageGeocode
#
# key = "59a7db25b3484550bff3fd660d59ed21"
# geocoder = OpenCageGeocode(key)
#
# addresses_df = pd.read_excel("Addresses.xlsx")
#
# addresses = addresses_df["Addresses"].values.tolist()
#
# latitudes = []
# longitudes = []
#
# for address in addresses:
# 	result = geocoder.geocode(address, no_annotations="1")
#
# 	if result and len(result):
# 		longitude = result[0]['geometry']['lng']
# 		latitude = result[0]['geometry']['lat']
# 	else:
# 		longitude = "N/A"
# 		latitude = "N/A"
# 
# 	latitudes.append(latitude)
# 	longitudes.append(longitude)
#
# addresses_df["latitudes"] = latitudes
# addresses_df["longitudes"] = longitudes
#
# addresses_df.to_excel("Addresses_Geocoded.xlsx")

from opencage.geocoder import OpenCageGeocode

key = '59a7db25b3484550bff3fd660d59ed21'
geocoder = OpenCageGeocode(key)

query = u'Bosutska ulica 10, Trnje, Zagreb, Croatia'
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 45.797095;15.982453;hr;Europe/Belgrade
