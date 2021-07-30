#Найти сумму и произведение элементво списка. Результат вывести на экран
lists = list(input('Укажите последовательность элементов: '))
summ = 0
multiplication = 1
for i in lists:
    summ += i
    multiplication *= i
print(f'Сумма элементов {summ}, произведение элементов {multiplication}')
