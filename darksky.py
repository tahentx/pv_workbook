import requests
import json

def main():
	print("\n Dark Sky API tool \n")
	lat = 41.172508
	long = -73.438858
	api_key = 'e56fa72ef66e61dd4ce85c58c6cc55aa'
	time = '1559347200'
	exclusion = "exclude="
	ex1 = "currently"
	url = "https://api.darksky.net/forecast/" + str(api_key) + "/" + str(lat) + "," + str(long) + "," + time + "?" + str(exclusion) + str(ex1)
	response = requests.get(url)
	print((response.text))


if __name__ == "__main__":
		main()
