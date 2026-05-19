class PaperWallet:

    def __init__(self, initial_balance = 1000):

        self.balance = initial_balance

        self.btc_amount = 0

        self.in_position = False

        self.entry_price = 0

    def buy(self, price, usdt_amount):

        if self.in_position:

            print("Ya hay una posicion abierta")

            return
        

        btc_bought = usdt_amount / price

        self.balance -= usdt_amount

        self.btc_amount += btc_bought

        self.entry_price = price 

        self.in_position = True

        print(f"Compra simulada: {btc_bought:.6f} BTC a {price}")

    
    def sell(self, price):

        if not self.in_position:

            print("No hay posicion abierta")

            return 
        
        
        usdt_received = self.btc_amount * price

        profit = usdt_received - (self.btc_amount * self.entry_price)

        self.balance += usdt_received

        print(f"Venta simulada a {price}")

        print(f"Resultado: {profit:.2f} USDT")


        self.btc_amount = 0

        self.entry_price = 0

        self.in_position = False

    def show_balance(self):

        print("\n========== PAPER WALLET ==========")

        print(f"\nBalance USDT: {self.balance:.2f}")

        print(f"\nBTC actual: {self.btc_amount:.6f}")

        print(f"\nEn posicion: {self.in_position}")