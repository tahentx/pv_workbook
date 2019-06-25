import pandas as pd
import numpy as np
import matplotlib as plt
import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64

def main():
    headers = {
    'Ocp-Apim-Subscription-Key': 'e6b0b9743f174073a26f4b94a3e7af09',
    }
    url = "https://api.powerfactorscorp.com/sfconnect/v1/workorders"
    response = requests.get(url,headers=headers)
    print(response)
    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.powerfactorscorp.com')
        conn.request("GET", "/sfconnect/v1/workorders/3016%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == "__main__":
		main()
