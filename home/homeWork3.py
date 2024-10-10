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

