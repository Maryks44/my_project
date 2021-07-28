# Сложите цифры целого числа
number = input('Введите целое число: ')
result = 0  # total sum
while len(number) > 0:
    result += int(number) % 10
    number = number[:len(number) - 1]
print(result)