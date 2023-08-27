"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
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


def guess_number (sum_of_numbers:int, mult_of_numbers:int) ->list:
    result_list = list()    
    for i in range(1, 1001):
        for j in range (1, 1001):
            if i + j == sum_of_numbers and i * j == mult_of_numbers:
                result_list.append((i,j))
    return result_list
                            



S = input_validation_int("Введите сумму загаданных чисел: ")
P = input_validation_int("Введите произведение загаданных чисел: ")
result = guess_number(S, P)
if result != []:
    print(f"Возможные пары загаданных натуральных чисел: {result}")
else:
    print ("Петя плохой студент, не существует двух натуральных чисел с такими свойствами")