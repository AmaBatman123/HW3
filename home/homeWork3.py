class Bank():


    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        sum = int(input())
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

# Создание экземпляров
bank1 = Bank("Bank1", 1000)
bank2 = Bank("Bank2", 2000)

print(bank1._balance)
print(bank2._balance)

print("\nAdding money to Bank1:")
bank1.moneyX()

print("\nResetting balance of Bank2:")
bank2._kill()
print(bank2._balance)

print("\nApplying jackpot to Bank1:")
bank1._Bank__jackpot()
print(bank1._balance)

print("\nMerging balance of Bank2 into Bank1:")
bank1._merge(bank2)
print(bank1._balance)
print(bank2._balance)