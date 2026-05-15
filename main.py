from services.market_data import get_btc_price
import time
from services.market_data import get_klines
from services.indicators import add_ema, check_signal

df = get_klines()

df = add_ema(df)

signal = check_signal(df)

print(df[["close", "EMA9", "EMA21"]].tail())

print(f"\nSEÑAL ACTUAL: {signal}")

#print(df[["open", "high", "low", "close", "volume"]].tail())





#while True:

    #price = get_btc_price()

   #print(f"BTCUSDT Price: {price}")

    #time.sleep(5)