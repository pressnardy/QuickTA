import pivots, apirequests
import finplot as fplt
import pandas as pd

candles = apirequests.candles()

# range = pivots.define_range(candles)
resistance_pivots = pivots.get_highs(candles)

for candle in resistance_pivots:
	pivot_high = pd.Series(candle['high'])
	pivot_time = pd.to_datetime(candle['time'], unit='ms')

	end_time = pd.to_datetime(candles[-1]['time'], unit='ms')
	p0 = (pivot_time, pivot_high)
	p1 = (end_time, pivot_high)

	print(p0, p1)
	line = fplt.add_line(p0, p1)


for candle in candles:
	candle['time'] = pd.to_datetime(candle['time'], unit='ms')

candles_df = pd.DataFrame(candles)

fplt.candlestick_ochl(candles_df[['time', 'open', 'close', 'high', 'low']])
fplt.show()

