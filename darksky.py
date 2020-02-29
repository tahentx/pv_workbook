import requests
import json
import darksky
import pandas as pd

def main():
	lat = 41.172508
	long = -73.438858
	api_key = 'e56fa72ef66e61dd4ce85c58c6cc55aa'
	time = '1559347200'
	exclusion = "exclude="
	ex1 = "currently"
	url = "https://api.darksky.net/forecast/" + str(api_key) + "/" + str(lat) + "," + str(long) + "," + time + "?" + str(exclusion) + str(ex1)
	response = requests.get(url)
	data = pd.read_json(path_or_buf=response.text,orient='index')
	data.to_excel('test.xlsx',sheet_name="Sheet1")

if __name__ == "__main__":
		main()
