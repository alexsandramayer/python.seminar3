# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# list = []
# for i in range(10):
#     list.append(randint(1, 11))
# print(list)

# sum = 0
# i = 0
# for i in range(len(list)):
#     if i%2 != 0:
#         sum += list[i]
# print(sum)



# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# from random import randint
# number = int(input("Введите количество чисел в списке: "))
# list1 = []
# list2 = []
# for i in range(number):
#     list1.append(randint(1, 11))
# print(list1)

# i = 0
# while i < len(list1) / 2:
#     number -= 1
#     a = list1[i] * list1[number]
#     list2.append(a)
#     i += 1
# print(list2)



# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform
# number = int(input("Введите количество чисел в списке: "))
# list = []
# for i in range(number):
#     a = uniform(1, 11)
#     list.append(round(a, 2))
# print(list)

# list2 = []
# for i in range(number):
#     a = list[i] - (int(list[i]) )
#     list2.append(round(a, 2))

# res = max(list2)-min(list2)


# print(max(list2), min(list2))
# print(round(res, 3))



#  Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# n = int(input("Введите число: "))
# a = ''

# while n != 0:
#     a = str(n % 2) + a
#     n = n // 2
# print(a)





# задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# n = int(input("Введите число: "))
# def fib_num(n):
#     fib = []
#     a, b = 1, 1
#     for i in range(n):
#         fib.append(a)
#         a, b = b, a + b
#     a, b = 0, 1 
#     for i in range(n + 1):
#         fib.insert(0, a)
#         a, b = b, a - b
#     print(fib)
# fib_num(n)
