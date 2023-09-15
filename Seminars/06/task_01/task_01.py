"""
from random import randint
from easygui import *


def random_list(size):
    result = []
    for _ in range(size):
        result.append(randint(-10,10))
    return result


# sp = [-5, 8, -9, 1, 7, 2]

# print([x for x in sp])
# print([x**2 for x in sp])
# print([x**2 for x in sp if x > 0])
# print([x**2 if x > 0 else 0 for x in sp ])

# print({str(i): randint(1,100) for i in range(10)})
size = int(enterbox("Введите размер"))
msgbox(str({str(i): randint(1,100) for i in range(size)}))

#второй список на основе первого если элемент >0 то возвести в квадрат иначе 0 

# print(random_list(10))

# print([randint(1,100) for _ in range(10)])
"""

"""
Семинар 6. Повторение списков
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
"""
import random

size = 10
random_list1 = [random.randint(-10,10) for i in range(size)]
print(random_list1)
random_list2 = [random.randint(-10,10) for i in range(size)]
print(random_list2)
result_list =  [item for item in random_list1 if item not in random_list2]
print (result_list)