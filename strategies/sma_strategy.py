#COMO INTERPRETA LOS DATOS PARA GENERAR SEÑALES DE COMPRA O VENTA

def check_signal(df):

    previous_row = df.iloc[-3]

    last_row = df.iloc[-2]

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