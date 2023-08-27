"""
 На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
 Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
 Выведите минимальное количество монет, которые нужно перевернуть
"""
import random
from decimal import Decimal


#Функция валидациии ввода, при не верном вводе просит повторить его, в цикле, пока ввод не будет корректен
def input_validation_int (invitation_text:str) -> int:
    variable = None
    while variable == None:       
        value = input(invitation_text)        
        try:
            buff = Decimal(value)
            if buff == int(buff):
                variable = int (buff)
                return variable
            else: raise
        except:
            print("Вы ввели не целое число, повторите ввод")


# Создаём список с количеством монет, пусть значение 0 соответствует решке, а 1 - гербу
def filling_list(count_list: int) -> list:
    result_list = list()
    for i in range(count_list):
        if random.randint(0, 1) == 0:
            result_list.append("tail")
        else:
            result_list.append("head")
    return result_list


def upend_min_coins(coins_list: list) -> list:
    tail_of_coin = 0
    head_of_coin = 0
    for i in range(len(coins_list)):
        if coins_list[i] == "tail":
            tail_of_coin += 1
        else:
            head_of_coin += 1
    if tail_of_coin < head_of_coin:
        return ["tail", tail_of_coin]
    else:
        return ["head", head_of_coin]





count_of_coins = input_validation_int("Сколько на столе лежит монет?: ")

coins_list = filling_list(count_of_coins)
min_coins_upend = upend_min_coins(coins_list)
print(coins_list)
if min_coins_upend[1] == len(coins_list) / 2:
    print(
        f"Количество монет повёрнутых решкой или гербом одинаково и равно {min_coins_upend[1]}")
elif min_coins_upend[0] == "tail":
    print(
        f"Количество монет повёрнутых решкой меньше, чем гербом: соответственно минимально нужно повернуть {min_coins_upend[1]} монет")
elif min_coins_upend[0] == "head":
    print(
        f"Количество монет повёрнутых орлом меньше, чем решкой: соответственно минимально нужно повернуть {min_coins_upend[1]} монет")
