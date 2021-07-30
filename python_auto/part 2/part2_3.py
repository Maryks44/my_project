# Посчитать двойной фактариал числа N
number = int(input('Ввведите число N: '))
factorial = 1

if number % 2 == 0:
    for i in range(2, number + 1, 2):
        factorial *= i
else:
    for i in range(3, number + 1, 2):
        factorial *= i
print(factorial)
