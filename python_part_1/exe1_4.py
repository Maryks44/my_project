#the exercise number 4 https://stepik.org/lesson/5047/step/4?auth=login&unit=1086

name = input()
if name == 'треугольник':
    a,b,c = float(input()),float(input()),float(input())
    p = (a + b + c)*0.5
    print((p*(p-a)*(p-b)*(p-c))**0.5)  
elif name == 'прямоугольник':
    a,b = float(input()),int(input())
    print(a*b)
elif name == 'круг':
    r = float(input())
    print(3.14*(r**2))