number = int(input())
sum = 0
d = {i : 3*i + 1 for i in range(1,number+1)}

def sequence(number):
    return[round((1 + 1 / i)**i, 2) for i in range (1, number + 1)]          
print(sequence(number))

for i in range(1, number + 1):
    sum += (1 + 1 / i) ** i
print(f'Сумма последовательности чисел равна: {sum}')