import sqlite3

DB_PATH = "data/trades.db"

def create_tables():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            type TEXT,
            price REAL,
            btc_amount REAL,
            usdt_amount REAL,
            profit REAL
        )
    """)

    conn.commit()

    conn.close()

    print("Tabla trades verificada")