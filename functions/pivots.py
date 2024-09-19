
range = [
	{"open":5, "high":5.1, "close": 4.8, "low":4.6},
	{"open": 6, "high":5.8, "close": 4.9, "low":4.9}
]

def define_range(range, lookback):
	highs = get_highs(range, lookback)
	lows = get_lows(range, lookback)
	range_high = highs[0]
	range_low = lows[0]
	return range_high, range_low


def get_highs(range, lookback=5):
	sorted_by_highs = sorted(range[:(len(range) - lookback)], key=lambda k: k["high"], reverse=True)
	pivots = []

	for i in sorted_by_highs:
		for candle in range:
			candle_index = range.index(candle)
			if candle['time'] == i['time'] and candle_index >= lookback:
				candle_range = range[(candle_index-lookback):]
				range_highs = [k['high'] for k in candle_range]
				if candle['high'] == max(range_highs):
					pivots.append(candle)
					range = range[candle_index + 1:]
					break
	return pivots


def get_lows(range, lookback=5):
	sorted_by_lows = sorted(range[:(len(range) - lookback)], key=lambda k: k["high"])
	pivots = []

	for i in sorted_by_highs:
		for candle in range:
			candle_index = range.index(candle)
			if candle['time'] == i['time'] and candle_index >= lookback:
				candle_range = range[(candle_index-lookback):]
				range_lows = [k['low'] for k in candle_range]
				if candle['low'] == max(range_lows):
					pivots.append(candle)
					range = range[candle_index + 1:]
					break
	return pivots


def is_pivot(range, candle, pivot_type, lookback):
	if not pivot_type in ['high', 'low']:
		raise ValueError('enter either "low" or "high" for pivot_type')
	pivots = define_range(range, lookback)
	if (candle['high'] in pivots and pivot_type == 'high') or (candle['low'] in pivots and pivot_type == 'low'):
		return True
	else:
		return False


def pull_back_levels(range, lookback, pullback_type=""):
	if not pullback_type in ["bullish", "bearish"]:
		raise ValueError("missing value for pullback type... enter bullish or bearish for pullback type")

	range_high, range_low = define_range(range, lookback)
	if range_high["time"] <= range_low["time"] and pullback_type == "bullish":
		for candle in range:
			if candle["time"] == range_low["time"]:
				range_low_index = range.index(candle)
				new_range = range[range_low_index - lookback:]
				pullback_levels = get_lows(new_range, lookback)
				break

	if range_high["time"] >= range_low["time"] and pullback_type == "bearish":
		for candle in range:
			if candle["time"] == range_high["time"]:
				range_high_index = range.index(candle)
				new_range = range[range_high_index - lookback:]
				pullback_levels = get_highs(new_range, lookback)
				break

	return pullback_levels


def swing_highs(range, lookback):
	lows = get_lows(range, lookback)
	candle_index = 0
	swing_highs = []
	for candle in lows:
		candle1 = lows.index(candle_index)
		candle2 = lows.index(candle_index + 1)
		swing_slice = swing_slice(range, candle1, candle2)
		swing_high = sorted(swing_slice, key=lambda k: k["high"], reverse=True)[0]
		swing_highs.append(swing_high)
		candle_index += 1
	return swing_highs


def swing_lows(range, lookback):
	highs = get_highs(range, lookback)
	candle_index = 0
	swing_lows = []
	for candle in highs:
		candle1 = highs.index(candle_index)
		candle2 = highs.index(candle_index + 1)
		swing_slice = swing_slice(range, candle1, candle2)
		swing_high = sorted(swing_slice, key=lambda k: k["lows"])[0]
		swing_lows.append(swing_high)
		candle_index += 1

	return swing_lows


def swing_slice(range, candle1, candle2):
	for candle in range:
		if candle["time"] == candle1["time"]:
			for i in range:
				if i["time"] == candle2["time"]:
					candle1_index = range.index(candle)
					candle2_index = range.index(i)
					swing_slice = range[candle1_index:candle2_index]
	return swing_slice





