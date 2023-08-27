# Задача №17. Общее обсуждение
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
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

def unique_count (random_list:list) -> int:
    i = 0
    unique_counter = len(random_list)
    while i < len(random_list) - 1:
        j = i + 1
        while j < len(random_list):
            if random_list[j] != None or random_list[j] != None:                             
                if (random_list[j] == random_list[i]):
                    random_list[j] = None
                    unique_counter-=1               
            j+=1
        i+=1
    print (random_list)    
    return unique_counter
  


len_list = input_validation_int("Введите количество элементов списка: ")   
min_value = input_validation_int("Введите минимальное значение списка: ")
max_value = input_validation_int("Введите максимальное значение списка: ")
random_list = filling_list(len_list, min_value, max_value)
print(random_list)
count_of_unique_values = unique_count(random_list)
print(count_of_unique_values)