from binance.client import Client
from dotenv import load_dotenv
import os
import pandas as pd

#CARGA DE VARIABLES DEL .VENV
load_dotenv()

#OBTENER CLAVES
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

#CREAR CLIENTE BIANCNE
client = Client(api_key, api_secret)

#FUNCION PARA OBTENER EL PRECIO 
def get_btc_price():

    ticker = client.get_symbol_ticker(symbol= "BTCUSDT")

    return ticker["price"]


def get_klines(symbol= "BTCUSDT", interval= "1m", limit= 50):

    klines = client.get_klines(
        symbol = symbol,
        interval = interval,
        limit = limit
    )

    df = pd.DataFrame(klines, columns=[
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_volume",
        "number_of_trades",
        "taker_buy_base",
        "taker_buy_quote",
        "ignore"
    ])

    #CONVERTIR COLUMNAS NUMERICAS

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df
