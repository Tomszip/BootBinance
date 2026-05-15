import pandas as pd

def add_ema(df, short_period=9, long_period=21):
 
    df["EMA9"] = df['close'].ewm(span=short_period).mean()
    df["EMA21"] = df['close'].ewm(span=long_period).mean()
    
    return df


def check_signal(df):

    last_row = df.iloc[-1]

    ema9 = last_row["EMA9"]
    ema21 = last_row["EMA21"]

    if ema9 > ema21:
        return "COMPRA"
    
    elif ema9 < ema21:
        return "VENTA"
    
    else:
        return "NEUTRO"