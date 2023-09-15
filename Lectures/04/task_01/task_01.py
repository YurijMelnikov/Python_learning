"""
В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
"""

import random
from decimal import Decimal


def input_validation_int(invitation_text: str) -> int:
    variable = None
    while variable == None:
        value = input(invitation_text)
        try:
            buff = Decimal(value)
            if buff == int(buff):
                variable = int(buff)
                return variable
            else:
                raise
        except:
            print("\033[6m\033[31m{}\033[0m".format("Вы ввели не целое число, повторите ввод"))

def square_of_even_numbers (random_list:list) -> list:
    square_numbers_list = list()
    for item in random_list:
        if item % 2 == 0:
            square_numbers_list.append((item, item**2))
    return square_numbers_list
min = input_validation_int("Введите минимальное значение списка случайных целых чисел: ")
max = input_validation_int("Введите максимальное значение списка случайных целых чисел: ")
count = input_validation_int("Введите количество элементов списка целых чисел: ")
random_list = [random.randint(min, max) for _ in range (count)]
print (random_list)
result = square_of_even_numbers(random_list)
print (result)