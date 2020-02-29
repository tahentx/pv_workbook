import requests
import pandas as pd

# dpath might be the library to use to pull data from complex dictionary
# url and api key to test solaredge api
def main():
	url = "https://monitoringapi.solaredge.com/site/581140/energy?timeUnit=QUARTER_OF_AN_HOUR&startDate=2018-10-23&endDate=2018-10-24&api_key=XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4"
	api_key = {'api_key': '47WOTOHKC1QCXHSF101MG9DAI5GA52SH'}
# first use of requests library
	response = requests.get(url,params=api_key)
	payload = response.text
	df = pd.DataFrame(eval(payload))
	

	# print(response.text)


if __name__ == "__main__":
		main()
