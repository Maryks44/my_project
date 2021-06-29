#the exercise number 3 https://stepik.org/lesson/5047/step/3?auth=login&unit=1086

a, b, operation = float(input()), float(input()), input()
if b == 0 and (operation == '/' or operation == 'div' or operation == 'mod'):
    print('Деление на 0!')
else:
    if operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '/':
        print(a / b)
    elif operation == '*':
        print(a * b)
    elif operation == 'mod':
        print(a % b)
    elif operation == 'pow':
        print(a**b)
    elif operation == 'div':
        print(a // b)