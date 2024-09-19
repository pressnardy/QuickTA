import pandas as pd
import numpy as np
import finplot as fplt


#create DataFrame
# prices = pd.DataFrame({'open': [25, 22, 21, 19, 23, 21, 25, 29],
#                        'close': [24, 20, 17, 23, 22, 25, 29, 31],
#                        'high': [28, 27, 29, 25, 24, 26, 31, 37],
#                        'low': [22, 16, 14, 17, 19, 18, 22, 26]},)
#                        # index = pd.date_range("2021-01-01", periods=8, freq="d"))
#
#
# print(prices)
# fplt.candlestick_ochl(prices[['open', 'close', 'high', 'low']])
# fplt.show()




dates = pd.date_range('01:00', '01:00:01.200', freq='1ms')
prices = pd.Series(np.random.random(len(dates))).rolling(30).mean() + 4
fplt.plot(dates, prices, width=3)
line = fplt.add_line((dates[100], 4.4), (dates[len(dates)-10], 4.6), color='#9900ff', interactive=True)

## fplt.remove_primitive(line)
text = fplt.add_text((dates[500], 4.6), "I'm here alright!", color='#bb7700')
## fplt.remove_primitive(text)
rect = fplt.add_rect((dates[700], 4.5), (dates[850], 4.4), color='#8c8', interactive=True)
## fplt.remove_primitive(rect)


def save():
    fplt.screenshot(open('screenshot.png', 'wb'))
fplt.timer_callback(save, 0.5, single_shot=True) # wait some until we're rendered

fplt.show()


