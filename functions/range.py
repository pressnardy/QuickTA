
def range_extrems(range):
	# takes a list of dictionaries with ohcl data for every candle as dictoinaries
	sorted_by_highs = sorted(range, key=lambda k: k["high"])
	range_high = sorted_by_highs[0]['high']
	sorted_by_lows = sorted(range, key=lambda k: k["high"])
	range_low = sorted_by_lows[0]['low']
	return range_high, range_low


def candle_in_range(candle, range):
	for i in range:
		if i['high'] == candle['high'] \
				and i['close'] == candle['close'] \
				and i['open'] == candle['open'] \
				and i['close'] == candle['close']:
			return True
	else:
		return False



def is_pivot(candle: dict, range: list[dict], pivot_type = '', look_back_left = 5, look_back_right = 5):

	if not pivot_type in  ['high', 'low']:
		raise ValueError('enter high for resistant pivots and low for support pivotes')

	for i in range:
		if i[pivot_type] == candle[pivot_type] and 	candle_in_range(candle, range) and pivot_type == 'high':
			candle_index = range.index(i)
			lookback_range = range[(candle_index - look_back_left):(candle_index + look_back_right + 1)]
			lookback_highs = [i[pivot_type] for i in lookback_range]
			if candle[pivot_type] >= max(lookback_highs):
				return True

	else:
		return False


def range_pivots(range, pivot_type = '', look_back_right = 5, look_back_left = 5):

	pivots = []
	pivot_values = []
	range_level_pivots = []
	for candle in range:
		if is_pivot(candle, range, pivot_type, look_back_right, look_back_left):
			pivots.append(candle)
			pivot_values.append(candle[pivot_type])

	for candle in pivots:
		candle_index = pivots.index(candle)
		pivot_value = candle[pivot_type]
		candle_slice = pivot_values[candle_index:]
		if (pivot_value >= max(candle_slice) and pivot_type == 'high') or \
				(pivot_value <= min(candle_slice) and pivot_type == 'low'):
			range_level_pivots.append(candle)

	return range_level_pivots










