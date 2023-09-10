# Задача 1

class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

a = int(input("Длинна прямоугольника: "))
b = int(input("Ширина прямоугольника: "))
obj = Rectangle(a, b)
print("Площадь прямоугольника:", obj.area())

print()

class Rectangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return (self.a + self.b) * self.c

a = int(input("Длинна прямоугольника: "))
b = int(input("Ширина прямоугольника: "))
c = int(input("Умножение на 2: "))
obj = Rectangle(a, b, c)
print("Периметр прямоугольника:", obj.perimetr())

print()

# Задача 2

class Math():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

a = int(input("Число а: "))
b = int(input("Число b: "))
obj = Math(a, b)
print("Сумма:", obj.addition())

print()

class Math():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiplication(self):
        return self.a * self.b

a = int(input("Число а: "))
b = int(input("Число b: "))
obj = Math(a, b)
print("Сумма:", obj.multiplication())

print()

class Math():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def division(self):
        return self.a / self.b

a = int(input("Число а: "))
b = int(input("Число b: "))
obj = Math(a, b)
print("Сумма:", obj.division())

print()

class Math():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def subtraction(self):
        return self.a - self.b

a = int(input("Число а: "))
b = int(input("Число b: "))
obj = Math(a, b)
print("Сумма:", obj.subtraction())

print()

# Задача 3

class Button:

    def __init__(self, text='Text Box', type='Кнопка', loc=None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}" .format(self.text)

Text_Box = Button('Text Box', 'Кнопка', None)

print(Text_Box.click())