import requests
import finplot as fplt
import pandas as pd
import numpy as np


def candles():
    url = 'https://api.binance.com/api/v3/klines'
    params = {
      'symbol': 'BTCUSDT',
      'interval': '1h'
    }
    response = requests.get(url, params=params).json()
    #print(response)

    candles = {
        # "time": [],
        "open": [],
        "high": [],
        "low": [],
        "close": []
    }

    time = []

    for data in response:
        try:
            open_time, open_price, high, low, close = data[:5]
            # candles['time'].append(open_time)
            time.append(open_time)
            candles['open'].append(float(open_price))
            candles['high'].append(float(high))
            candles['low'].append(float(low))
            candles['close'].append(float(close))
        except ValueError:
            break
    #print(candles)
    # candles['time'] = [pd.to_datetime(i, unit='ms') for i in candles['time']]

    # candles_df = pd.DataFrame(candles, index=candles['time'])
    candles_df = pd.DataFrame(candles, index=time)
    #candles_df = candles_df.astype({"time": 'str'})

    print(candles_df)

    fplt.candlestick_ochl(candles_df[['open', 'close', 'high', 'low']])
    fplt.show()


candles()








