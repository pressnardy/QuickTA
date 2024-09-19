import requests

host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/currencies'
query_param = ''
response = requests.get(host + prefix + url, headers=headers)

response = response.json()
listed = []
for crypto in response:
	symbol = crypto['currency']
	listed.append(symbol)

for crypto in listed:
	print(crypto)


