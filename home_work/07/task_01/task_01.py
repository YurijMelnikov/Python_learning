"""
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
#Не очень понятно, зачем нужна формула нахождения n элемента арифметической прогрессии, если задача состоит в заполнении списка
#элементами арифметической прогрессии от первого до n элемента
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

def arithmetic_mean (first_element:int, difference:int, quantity:int) ->list:
    arithmetic_mean_list = list()
    arithmetic_mean_list.append(first_element)
    for i in range (1, quantity + 1):
        arithmetic_mean_list.append (arithmetic_mean_list[i-1]+difference)
    return arithmetic_mean_list

first_element = input_validation_int("Введите первый элемент арифметической прогрессии: ")
difference  = input_validation_int("Введите разность арифметической прогрессии: ")
quantity = input_validation_int("Введите количество элементов арифметической прогрессии: ")
result_list = arithmetic_mean (first_element, difference, quantity)
print(f"{quantity} членов арифметической прогрессии:\n{result_list}")