# Задача 1

x, y = int(input()), int(input())
if x > y:
    print('x')
else:
    print('y')


# Задача 2

x = int(input('Введите число №1 = '))
y = int(input('Введите число №2 = '))
if ( 'a - b' ) == 0:
    print ('NO')
else:
    print ('YES')


# Задача 3

month = input('Введите номер месяца:')
if int('month') <=0 or int('month') >12:
    print('Неверное номер месяца')
elif int('month') >2 and int('month') <6:
    print ('Весна')
elif int('month') >5 and int('month') <9:
    print('Лето')
elif int('month') >8 and int('month') <12:
    print('Осень')
else:
    print('Зима')


# Задача 4

x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))
if x>10 and y>10 and z>10:
    print('YES')
else:
    print('NO')
