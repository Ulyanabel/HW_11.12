# типы данных и переменная
# float, int, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))
# s = 'hello world'
# print(s) # вывод строки
# print(a, '-',b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)
# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# Вывод данных
# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, %, //, **
# (), Сокращенные операции
# a = 1.3123
# b = 3
# c = round(a * b, 5)
# print(c)

# Операции присваивания
# a = 3
# # a = a + 5
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# кое-что еще: is, is not, in, not in
# gen
# a = 1 != 2
# print(a)

# Управляющие операции
# if, else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#    print(a)
# else:
#    print(b)

# if, elif
# username = input('Введите имя: ')
# if username == 'Маша':
#    print('Ура, это же Маша')
# elif username == 'Марина':
#    print('Я так ждала вас, Марина')
# elif username == 'Ильнар':
#    print('Ильнар - топ)')
# else:
#    print('Привет, ', username)

# Управляющие конструкции:
# while - позволяет выполнять блок операторов какое-то кол-во раз
# original = 23
# inverted = 0
# while original != 0:
#    inverted = inverted * 10 +(original % 10)
#    original //= 10
# else:
#    print('Пожалуй')
#    print('хватит ')
# print(inverted)

# for
# for i in 1,2,3,4,5:
#    print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#    print(i**2)

# r = range(10)
# for i in r:
#    print(i)