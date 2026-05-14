from services.market_data import get_btc_price
import time
from services.market_data import get_klines


df = get_klines()

print(df[["open", "high", "low", "close", "volume"]].tail())





#while True:

    #price = get_btc_price()

   #print(f"BTCUSDT Price: {price}")

    #time.sleep(5)