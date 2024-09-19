import requests
import finplot as fplt
import pandas as pd

def candles():
    url = 'https://api.binance.com/api/v3/klines'
    params = {
      'symbol': 'BTCUSDT',
      'interval': '4h'
    }
    response = requests.get(url, params=params).json()
    #print(response)

    time = []
    # candles = {
    #     "open": [],
    #     "high": [],
    #     "low": [],
    #     "close": [],
    # }
    candles = [

    ]

    # time = []
    for data in response:
        try:
            candle = {}
            open_time, open_price, high, low, close = data[:5]
            candle['time'] = open_time
            candle['open'] = float(open_price)
            candle['high'] = float(high)
            candle['low'] = float(low)
            candle['close'] = float(close)

            candles.append(candle)
        except ValueError:
            break
    for candle in candles:
        candle['time'] = pd.to_datetime(candle['time'], unit='ms')
    candles_df = pd.DataFrame(candles) #index=[candle['time'] for candle in candles])
    #candles_df.set_index('time')
    print(candles_df)
    fplt.candlestick_ochl(candles_df[['time', 'open', 'close', 'high', 'low']])
    fplt.show()

candles()









