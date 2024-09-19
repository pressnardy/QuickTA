import requests

def candles():
	url = 'https://api.binance.com/api/v3/klines'
	params = {
	  'symbol': 'BTCUSDT',
	  'interval': '4h'
	}
	response = requests.get(url, params=params).json()

	candles = []
	for data in response:
		try:
			candle = {}
			open_time, open_price, high, low, close, volume = data[:6]
			candle['time'] = open_time
			candle['open'] = float(open_price)
			candle['high'] = float(high)
			candle['low'] = float(low)
			candle['close'] = float(close)
			candle['volume'] = float(volume)
			candles.append(candle)
		except ValueError:
			break

	return candles

# print(candles())








