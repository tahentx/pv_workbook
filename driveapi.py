import requests
def main():
    headers = {
    'Ocp-Apim-Subscription-Key': '9e3627e64373439fa7d33c9eed0324f3',
    }
    url = "https://api.powerfactorscorp.com/drive/v2/plant"
    response = requests.get(url,headers=headers)
    print(response)

if __name__ == "__main__":
		main()
