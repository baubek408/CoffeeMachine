class MoneyMachine:

    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Print the current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns total calculated from coins inserted."""
        print("PLease insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How much {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True if payment is accepted or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round((self.money_received - cost), 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry there is not enough money. Money refunded.")
            self.money_received = 0
            return False
