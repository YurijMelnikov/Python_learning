"""
Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
456 -> 3
0 -> 1
89,126 -> 5
0,001->4
"""
# Т.к. в программе присутствуют сравнения чисел с плавающей запятой, вместо типа float разумнее использовать тип Decimal
from decimal import Decimal


def input_validation_decimal(invitation_text: str) -> Decimal:
    variable = None
    while variable == None:
        value = input(invitation_text)
        try:
            variable = Decimal(value)
            return variable
        except:
            print("Вы ввели не число, повторите ввод")


def count_of_digits(number: Decimal) -> int:

    #Функция преобразования числа в целое
    def convert_number_to_int(number: Decimal) -> int:
        while number % 1 != 0:
            number *= 10
        return int(number)

    #Функция подсчёта количества цифр и целом числе
    def count_of_digits_in_int(number: Decimal) -> int:
        counter = 0
        while number >= 1:
            number //= 10
            counter += 1
        return int(counter)

    number = abs(number)
    #если модуль числа меньше 1, соответственно в цикле увеличиваем его на порядок и проверяем, стало ли оно целым, при этом счётчик
    #отсчитывает с 1, т.к. первая цифра всегда ноль, когда число стало целым - значение счётчика и будет искомым ответом 
    if number < 1:
        counter = 1
        while number % 1 != 0:
            number *= 10
            counter += 1
        return counter
    elif number >= 1:
        return count_of_digits_in_int(convert_number_to_int(number))#Если модуль числа >=1, вначале преобразуем его в целое, далее считаем цифры, в нём
                                                                    #последовательно целочисленно деля его на 10


N = input_validation_decimal("Введите число: ")
print(f"Количество цифр в числе {N}: {count_of_digits(N)}")
