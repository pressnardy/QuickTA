
# level score

level_scores = {
	'200_ema': 7,
	'200_ma': 7,
	'range_low': 7,
	'range_level_pivot': 5,
	'weekly_open': 4,
	'weekly_level': 5,
}

# trigger scores

trigger_scores =  {
	'sfp': 7,
	'failed_auction': 5,
	'cvd_div': 4,
	'rsi_div': 6,
	'rsi_3_step_div': 8,
	'pin_bar': 3,
	'rsi_hidden_div': 4,
	'8/20_ema_cross': 7,
}

def level_score(level_name=''):
	global level_scores
	try:
		return level_scores[level_name]
	except KeyError:
		raise KeyError('level not in list of levels')


def trigger_score(trigger_name=''):
	global trigger_scores
	try:
		return trigger_scores[trigger_name]
	except KeyError:
		raise KeyError('trigger not in list of levels')


