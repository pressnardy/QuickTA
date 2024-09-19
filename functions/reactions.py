

candle = {"open": 0.5, "high": 0.51, "close": 0.45, "low": 0.4}

def unpack(candle):
	return [values for key, values in candle.items()]


def is_hammer_reaction(candle, level, fib):
	open, high, close, low = unpack(candle)
	size = high - low
	is_hammer = high - fib * size < min(open, close)
	if is_hammer and low < level:
		return True

def is_shooting_star_reaction(candle, level, fib):
	open, high, close, low = unpack(candle)
	size = high - low
	is_shoot = low + fib * size > max(open, close)
	if is_shoot and high > level:
		return True

def is_positive_sfp_reaction(candle, level):
	open, high, close, low = unpack(candle)
	return true if low < level and close > level and close > open else False

def is_negative_sfp_reaction(candle, level):
	open, high, close, low = unpack(candle)
	return True if high > level and close < level and close < open else False

def is_reaction(candle, level, fib):
	if is_hammer_reaction(candle, level, fib) \
		or is_shooting_star_reaction(candle, level, fib) \
		or is_positive_sfp_reaction(candle, level)\
		or is_negative_sfp_reaction(candle, level):
		return True
	else:
		return False


try:
	is_reaction(candle, level, fib)
except NameError:
	print("missing data for candle, level or fib")



