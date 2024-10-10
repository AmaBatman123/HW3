class Calc():

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calc):
            amount = self.value + other.value
            return Calc(amount)
        elif isinstance(other, (int, float)):
            return Calc(self.value + other)
        else:
            raise ValueError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Calc):
            amount = self.value - other.value
            return Calc(amount)
        elif isinstance(other, (int, float)):
            return Calc(self.value - other)
        else:
            raise ValueError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Calc):
            amount = self.value * other.value
            return Calc(amount)
        elif isinstance(other, (int, float)):
            return Calc(self.value * other)
        else:
            raise ValueError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Calc):
            if other.value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Calc(self.value / other.value)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Calc(self.value / other)
        else:
            raise ValueError("Unsupported operand type for /")

    def __str__(self):
        return str(self.value)


# Пример использования калькулятора
calc1 = Calc(10)
calc2 = Calc(5)

add_result = calc1 + calc2
sub_result = calc1 - calc2
mul_result = calc1 * calc2
div_result = calc1 / calc2

print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)