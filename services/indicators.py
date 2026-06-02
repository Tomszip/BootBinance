import pandas as pd

def add_ema(df, short_period=9, long_period=21):
 
    df["EMA9"] = df['close'].ewm(span=short_period).mean()
    df["EMA21"] = df['close'].ewm(span=long_period).mean()
    
    return df

def add_rsi(df, period=14):
    
    delta = df["close"].diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()

    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    return df



