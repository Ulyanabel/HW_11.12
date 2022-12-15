# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

import cmath
x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))
num1 = (x2 - x1) ** 2
num2 = (y2 - y1) ** 2
num = num1 + num2
L = cmath.sqrt(num)
print('Расстояние = ' + str(L))
