class Bank():


    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        sum = input("Enter sum")
        if sum > 0:
            self._balance += sum
        else:
            print(f"Invalid amount")
        return print(f"Balance succsessfully updated. You balance now {self._balance}")

    def _kill(self):
        self._balance = 0
        return print(f"Your balance has been reseted")

    def __jackpot(self):
        self._balance *= 10
        print(f"Congratulations! You hit the jackpot! New Balance: {self._balance}")

    def _merge(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"Balances merged! New Balance: {self._balance}")
        else:
            print("The object is not a Bank instance. Cannot merge balances.")