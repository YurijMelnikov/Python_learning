"""
Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата.
*Дополнительно
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов где это возможно
Используйте функции
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

#Рекурсивный метод перевода целого числа из десятичной системы счисления, в любую другую с произвольным основанием
#Сделать через строку как то не вышло, получилось через список, с последующим преобразованием его в строку
def convert_to_binary(number: int, radix:int, result_list: list) -> list:
    if number < radix:
        return result_list.append(number)
    else:
        convert_to_binary(number//radix, radix, result_list)
        return result_list.append(number % radix)




n = input_validation_int("Введите целое число: ")
b = input_validation_int("Введите основание системы счисления, в которую нужно перевести целое десятичное число: ")

result = list()
convert_to_binary(abs(n),b, result)
if n < 0:
    result.insert(0,"-")
if b < 10:
    result = ''.join(map(str, result))
else:
    result = '\''.join(map(str, result)) #если основание больше 10, лучше разделить цифры, например апострофом
print(f"Число {n} в системе счисления с основанием {b} -> {result}")