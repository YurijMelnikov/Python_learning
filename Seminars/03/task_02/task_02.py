#Задача №19. Решение в группах
#Дана последовательность из N целых чисел и число
#K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K –
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]

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
            print("Вы ввели не целое число, повторите ввод")


def filling_list(count_list: int, min: int, max: int) -> list:
    result_list = list()
    for i in range(count_list):
        result_list.append(random.randint(min, max))
    return result_list

def shift_list (random_list:list, k:int) -> list:    
    buff_list = list()
    buff_list2 = list()
    for i in range(len(random_list) - k,len(random_list)):
        buff_list2.append(random_list[i])
    print(buff_list2)     
    for i in range(k):
        buff_list.append(random_list[i])
        for j in range (i + k, len(random_list),k):
            if j < len(random_list) - k:
                buff_list.append(random_list[j])
                random_list[j] = buff_list[-2]
            else:
                buff_list.append(random_list[j])
                random_list[j] = buff_list[-2]
                random_list[i] = buff_list2[i]
        buff_list.clear()
    return random_list


len_list = input_validation_int("Введите количество элементов списка: ")   
min_value = input_validation_int("Введите минимальное значение списка: ")
max_value = input_validation_int("Введите максимальное значение списка: ")
shift_value = input_validation_int("Введите на сколько элементов нужно сдвинуть массив: ")
random_list = filling_list(len_list, min_value, max_value)
# random_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(random_list)
shift_list (random_list, shift_value)
print(random_list)
                
            
