"""
Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
"""
import math



def input_validation_float (invitation_text:str) -> float:
    variable = None
    while variable == None:       
        value = input(invitation_text)        
        try:
            variable = float (value)
            return variable
        except:
            print("Вы ввели не число, повторите ввод")

def integer_powers_of_two(number: float) -> list:
    list_powers_of_two = list()
    for i in range(math.ceil(number) + 1):
        if pow(2, i) <= number:
            list_powers_of_two.append(pow(2, i))
        else:
            return list_powers_of_two


N = input_validation_float("Введите число: ")

list_powers_of_two = integer_powers_of_two(N)
print(
    f"Целые степени двойки, не превосходящие число {N}: \n{list_powers_of_two}")
