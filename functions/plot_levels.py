import pivots, apirequests
import finplot as fplt
import pandas as pd

# Fetch candle data
candles = apirequests.candles()

# Convert candle times to datetime
for candle in candles:
    candle['time'] = pd.to_datetime(candle['time'], unit='ms')

# Create DataFrame from candles
candles_df = pd.DataFrame(candles)

# Plot candlestick chart first
fplt.candlestick_ochl(candles_df[['time', 'open', 'close', 'high', 'low']])

# Get resistance pivots
resistance_pivots = pivots.get_highs(candles)

# Plot resistance pivot lines
for candle in resistance_pivots:
    pivot_high = candle['high']
    pivot_time = pd.to_datetime(candle['time'], unit='ms')
    end_time = pd.to_datetime(candles[-1]['time'], unit='ms')
    p0 = (pivot_time, pivot_high)
    p1 = (end_time, pivot_high)

    # Add color for better visibility
    fplt.add_line(p0, p1, color='#1bbbef')

# Show the plot
fplt.show()

