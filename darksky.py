import requests
import json

# dpath might be the library to use to pull data from complex dictionary
# url and api key to test solaredge api


def main():
	lat = input('latitude:')
	long = input('longitude:')
	api_key = 'e56fa72ef66e61dd4ce85c58c6cc55aa'
	url = "https://api.darksky.net/forecast/" + str(api_key) + "/" + str(lat) + "," + str(long)
	response = requests.get(url)
	print(response.text)


if __name__ == "__main__":
		main()
