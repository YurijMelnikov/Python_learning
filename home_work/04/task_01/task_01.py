"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
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

     

#Вначале удаляем все повторы с помощью преобразования во множество set(),
#затем отсортировать эти списки, и циклично сравнивать элементы первого списка, с элементами второго, при нахождении соответствующих
#записывать значение в результирующий список
def gluing_list (list1:list, list2:list) ->list:
    result_list = list()
    list1 = list(set(list1))
    list1 = sorted(list1)       
    list2 = list(set(list2))    
    list2 = sorted(list2)   
    for item in list1:
        for item2 in list2:
            if item == item2:
                result_list.append(item)
                break #т.к. все значения в каждом списке уникальны, после нахождения соответствующих элементов списка, дальнейшее выполнение вложенного цикла не требуется     
    return result_list #т.к. первый и второй списки уже отсортированы, дополнительная сортировка итогового списка не требуется




count1 = input_validation_int("Введите количество целых чисел в первом списке: ")
int_list_1 = []
int_list_2 = []
while int_list_1 == []:
    try: 
        min1 =  input_validation_int("Введите минимальное значение элемента в первом списке: ")
        max1 = input_validation_int("Введите максимальное значение элемента в первом списке: ")
        int_list_1 = [random.randint(min1,max1) for _ in range(count1)]
    except: print("\033[6m\033[31m{}\033[0m".format("Минимальное значение не может быть больше максимального, повторите ввод"))
count2 = input_validation_int("Введите количество целых чисел во втором списке: ")
while int_list_2 == []:
    try:
        min2 = input_validation_int("Введите минимальное значение элемента во втором списке: ")
        max2 = input_validation_int("Введите максимальное значение элемента во втором списке: ")
        int_list_2 = [random.randint(min2,max2) for _ in range(count2)]
    except: print("\033[6m\033[31m{}\033[0m".format("Минимальное значение не может быть больше максимального, повторите ввод"))
print(f"Первый список целых чисел: {int_list_1}")
print(f"Второй список целых чисел: {int_list_2}")
result_list = gluing_list(int_list_1, int_list_2)
print(f"Итоговый список, состоящий из значений, присутствующих в обоих списках без повторов:\n{result_list}")