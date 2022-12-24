from decimal import Decimal
def accuracy(num,acc):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{acc}"))
print(accuracy(float(input("Введите число :")), float(input("Введите требуемую точность"))))