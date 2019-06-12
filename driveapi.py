import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64

def main():
    headers = {
    'Ocp-Apim-Subscription-Key': '9e3627e64373439fa7d33c9eed0324f3',
    }
    url = "https://api.powerfactorscorp.com/drive/v2/plant"
    response = requests.get(url,headers=headers)
    print(response)
    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.powerfactorscorp.com')
        conn.request("GET", "/test/bandwidth-limit?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == "__main__":
		main()
