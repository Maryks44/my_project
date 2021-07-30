#Для кажого числа от 1 до 100 вывести список чисел меньше текущего и кратного пяти

number = int(input('Укажите число: '))
results = []
for i in range(1, 101):
    if i % 5 == 0 and i < number:
        results.append(i)
print(results)
