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



def check_signal(df):

    previous_row = df.iloc[-2]

    last_row = df.iloc[-1]

    previous_ema9 = previous_row["EMA9"]
    previous_ema21 = previous_row["EMA21"]

    current_ema9 = last_row["EMA9"]
    current_ema21 = last_row["EMA21"]

    current_rsi = last_row["RSI"]

    #CRUCE ALCISTA + RSI FUERTE 
    if (
        previous_ema9 < previous_ema21 
        and current_ema9 > current_ema21
        and current_rsi > 50
    ):
        
        return "CRUCE ALCISTA CONFIRMADO - COMPRA"
    
    #CRUCE BAJISTA + RSI DEBIL
    elif (
        previous_ema9 > previous_ema21 
        and current_ema9 < current_ema21
        and current_rsi < 50
    ):

        return "CRUCE BAJISTA CONFIRMADO - VENTA"
    
    else:
        
        return "SIN SEÑAL"