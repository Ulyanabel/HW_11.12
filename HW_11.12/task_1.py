# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

print('Введите день недели: ')
n = int(input())
if n < 6:
    print('нет')
else:
    print('да')