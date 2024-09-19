from binance import Client

client = Client()
prices = client.get_all_tickers()

for ticker in prices:
	pair = ticker['symbol']
	if pair.endswith('USDT'):
		symbol = pair.replace('USDT', '')
		print(symbol)




