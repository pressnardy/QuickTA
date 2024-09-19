import numpy
import talib
import apirequests

data = apirequests.candles()
close = [candle['close'] for candle in data]
close = numpy.array(close)
def ema(data, period):
	ema = talib.EMA(close, period)
	return ema

def ma(le):
	...

def hullsuit():
	...

def rsi():
	...

def stochasticrsi():
	...

def cvd():
	...

print(ema(data, period=20))
