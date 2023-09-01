"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном списке урожайности грядки.
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
            print("\033[6m\033[31m{}\033[0m".format(
                "Вы ввели не целое число, повторите ввод"))


def most_berries(shrub_list: list) -> (int, int):
    for i in range(len(shrub_list)):
        if i == 0:
            sum = shrub_list[i] + shrub_list[i+1] + shrub_list[-1]
            max_sum = sum
            max_index = i
        elif i < len(shrub_list) - 2:
            sum = shrub_list[i-1]+shrub_list[i]+shrub_list[i+1]
            if max_sum < sum:
                max_sum = sum
                max_index = i
        elif i == len(shrub_list) - 1:
            sum = shrub_list[i-1]+shrub_list[i]+shrub_list[0]
            if max_sum < sum:
                max_sum = sum
                max_index = len(shrub_list) - 1
    return max_sum, max_index


# Допустим, на каждом кусте может быть от 30 до 100 ягод
shrub_list = []
while shrub_list == []:
    try:
        shrub_count = input_validation_int(
            "Введите количество кустов на грядке: ")
        if shrub_count >= 3:
            shrub_list = [random.randint(30, 100) for _ in range(shrub_count)]
        else:
            raise
    except:
        print("\033[6m\033[31m{}\033[0m".format(
            "Вы ввели не корректное число кустов, повторите ввод"))
print(f"Список грядок с количеством ягод на каждом кусте: {shrub_list}")
max_berry = most_berries(shrub_list)
print(
    f"Максимальное количество ягод {max_berry[0]} можно собрать пристроившись к {max_berry[1]+1} кусту")
