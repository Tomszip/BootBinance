from services.market_data import get_btc_price
from services.market_data import get_klines
from services.indicators import add_ema, add_rsi
from services.paper_wallet import PaperWallet
from strategies.sma_strategy import check_signal
import time


wallet = PaperWallet()

while True:

    df = get_klines()

    df = add_ema(df)

    df = add_rsi(df)

    signal = check_signal(df)

    last_row = df.iloc[-1]

    print("\n=================================================")

    print(f"Precio actual: {last_row['close']}")

    print(f"EMA9: {last_row['EMA9']:.2f}")

    print(f"EMA21: {last_row['EMA21']:.2f}")

    print(f"RSI: {last_row['RSI']:.2f}")

    print(f"SEÑAL: {signal}")

    if signal == "CRUCE ALCISTA CONFIRMADO - COMPRA":
    
        wallet.buy(
            price=last_row["close"], 
            usdt_amount=100
        )

    elif signal == "CRUCE BAJISTA CONFIRMADO - VENTA":
        
        wallet.sell(
            price=last_row["close"]
        )

    time.sleep(5)

    #print(df[["close", "EMA9", "EMA21"]].tail())

    #print(f"\nSEÑAL ACTUAL: {signal}")

    #print(df[["open", "high", "low", "close", "volume"]].tail())





#while True:

    #price = get_btc_price()

   #print(f"BTCUSDT Price: {price}")

    #time.sleep(5)