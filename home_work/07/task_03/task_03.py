"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

    для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

"""
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
            
def validation_fibonachhi_count():
    count = None
    while count == None:
        try:
         count  = input_validation_int("Введите количество значений ряда негаФибоначчи: ")
         if count < 1:
             raise
        except:
            print("\033[6m\033[31m{}\033[0m".format(
                "Вы ввели не корректное количество значений ряда негаФибоначчи, повторите ввод"))
            count = None
    return count 
  
def nega_fibonachi(count_of_fibonachi:int) -> int:
    nega_fibonachi_list = [1,0,1]
    if count_of_fibonachi == 1:
        return nega_fibonachi_list
    for i in range(2, count_of_fibonachi+1):        
        nega_fibonachi_list.append(nega_fibonachi_list[-1] + nega_fibonachi_list[-2])
        nega_fibonachi_list.insert(0, (-1)**(i+1)*nega_fibonachi_list[-1])
    return nega_fibonachi_list


count_of_fibonachi = validation_fibonachhi_count()
result_list = nega_fibonachi(count_of_fibonachi)
print (f"Ряд негаФибоначчи до {count_of_fibonachi} значения: \n{result_list}")