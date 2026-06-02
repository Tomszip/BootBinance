class PaperWallet:

    def __init__(self, initial_balance = 1000):

        self.balance = initial_balance

        self.btc_amount = 0

        self.in_position = False

        self.entry_price = 0

        self.stop_loss_price = 0

        self.take_profit_price = 0

        self.trade_history = []

        self.fee_rate = 0.001

    def buy(self, price, usdt_amount):

        if self.in_position:

            print("Ya hay una posicion abierta")

            return
        

        if usdt_amount > self.balance:

            print("Balance insuficiente")

            return

        fee = usdt_amount * self.fee_rate

        net_usdt = usdt_amount - fee

        self.balance -= usdt_amount

        btc_bought = net_usdt / price

        self.btc_amount = btc_bought

        self.entry_price = price 

        self.stop_loss_price = price * 0.98

        self.take_profit_price = price * 1.04

        self.in_position = True

        self.trade_history.append({
            "type": "BUY",
            "price": price,
            "btc_amount": btc_bought,
            "usdt_amount": usdt_amount

        })

        print(f"Compra simulada: {btc_bought:.6f} BTC a {price}")

    
    def sell(self, price):

        if not self.in_position:

            print("No hay posicion abierta")

            return 
        
        
        usdt_received = self.btc_amount * price

        fee = usdt_received * self.free_rate

        usdt_received -= fee

        profit = usdt_received - (self.btc_amount * self.entry_price)

        self.balance += usdt_received

        print(f"Venta simulada a {price}")

        print(f"Resultado: {profit:.2f} USDT")

        self.trade_history.append({
            "type": "SELL",
            "price": price,
            "btc_amount": self.btc_amount,
            "usdt_amount": usdt_received,
            "profit": profit

        })

        self.btc_amount = 0

        self.entry_price = 0

        self.stop_loss_price = 0

        self.take_profit_price = 0

        self.in_position = False


    def show_balance(self):

        print("\n========== PAPER WALLET ==========")

        print(f"\nBalance USDT: {self.balance:.2f}")

        print(f"\nBTC actual: {self.btc_amount:.6f}")

        print(f"\nEn posicion: {self.in_position}")

        print(f"\nStop loss: {self.stop_loss_price:.2f}")

        print(f"\nTake profit: {self.take_profit_price:.2f}")