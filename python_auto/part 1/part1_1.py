# При заданном целом трехзначном числе n посчитайте n + nn + nnn
number = int(input('Введите трехзначное число: '))
print(number + number**2 + number**3)