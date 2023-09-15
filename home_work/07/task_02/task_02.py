"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

На входе : [ 1, 5, 88, 100, 2, -4]
33
200
Ответ: [2, 3]
"""
from decimal import Decimal
import random


class min_max_error(Exception):
    def error_text():
        print("\033[6m\033[31m{}\033[0m".format(
            "Максимальное значение не может быть меньше минимального, повторите ввод"))


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
            print("\033[6m\033[31m{}\033[0m".format(
                "Вы ввели не целое число, повторите ввод"))


def create_index_list_in_range(random_list: list, min_range: int, max_range: int) -> list:
    index_list_in_range = list()
    for i in range(len(random_list)):
        if random_list[i] >= min_range and random_list[i] <= max_range:
            index_list_in_range.append(i)
    return index_list_in_range


len_random_list = input_validation_int(
    "Введите количество элементов в списке целых чисел: ")

min_value = None
max_value = None
while (min_value == None and max_value == None):
    try:
        min_value = input_validation_int(
            "Введите минимальное значение списка целых чисел: ")
        max_value = input_validation_int(
            "Введите максимальное значение списка целых чисел: ")
        if min_value > max_value:
            raise min_max_error
    except min_max_error:
        min_max_error.error_text()
        min_value = None
        max_value = None
random_list = [random.randint(min_value, max_value)
               for _ in range(len_random_list)]
print(
    f"Список, состоящий из случайных целых чисел в заданном диапазоне:\n{random_list}")
min_range = None
max_range = None
while min_range == None and max_range == None:
    try:
        min_range = input_validation_int(
            "Введите минимальное значение диапазона (целые числа) для задания поиска индексов значений массива в заданном диапазоне: ")
        max_range = input_validation_int(
            "Введите минимальное значение диапазона (целые числа) для задания поиска индексов значений массива в заданном диапазоне: ")
        if min_range > max_range:
            raise min_max_error
    except min_max_error:
        min_max_error.error_text()
        min_range = None
        max_range = None
result_index_list = create_index_list_in_range(
    random_list, min_range, max_range)
print(
    f"Индексы значений списка в диапазоне [{min_range}-{max_range}]: {result_index_list}")