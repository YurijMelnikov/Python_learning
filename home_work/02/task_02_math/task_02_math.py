"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
import math
from decimal import Decimal



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

# Суть решить систему уравнений X + Y = S; X * Y = P
def guess_number(sum_of_numbers: int, mult_of_numbers: int) -> list:
    X1 = Decimal((-sum_of_numbers +
          math.sqrt(math.pow(sum_of_numbers, 2) - 4 * mult_of_numbers))/-2)
    Y1 = Decimal(sum_of_numbers - X1)
    X2 = Decimal((-sum_of_numbers -
          math.sqrt(math.pow(sum_of_numbers, 2) - 4 * mult_of_numbers))/-2)
    Y2 = Decimal(sum_of_numbers - X2)
    return [[X1, Y1], [X2, Y2]]




S = input_validation_int("Введите сумму загаданных чисел: ")
P = input_validation_int("Введите произведение загаданных чисел: ")
#обработаем исключения, если решение уравнения не натуральные числа или решить уравнение не возможно (в случае, если дискриминант < 0)
try:
    result = guess_number(S, P)
    try:
        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][j] == int(result[i][j]) and result[i][j] != 0:
                    result[i][j] = int(result[i][j])                    
                else: raise
        print(f"Возможные пары загаданных натуральных чисел: {result}")
    except:
        print("Петя плохой студент, не существует двух натуральных чисел с такими свойствами, но существуют не натуральные числа:")
        print(result)
except:
    print("Петя ужасный студент, не существует вообще никаких чисел с такими свойствами")