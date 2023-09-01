"""
Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

например, k=2 -> -x^2 + 3*x - 8 = 0
тут коэффициенты -1,3,-8
например, k=3 -> 3*x^3 - 2*x = 0
тут коэффициенты 3,0,-2,0
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
            print("\033[6m\033[31m{}\033[0m".format(
                "Вы ввели не целое число, повторите ввод"))


def create_polynomial(k: int) -> str:
    try:
        # Создаём список коэффициентов многочлена
        coef_list = [random.randint(-10, 10) for _ in range(k+1)]
        if coef_list != []:
            print("Список случайных коэффициентов многочлена в порядке убывания степени, последний - константа многочлена\n", coef_list)
        result = str()
        counter = 0
        # Цикл для вычисления итератора counter, если первые коэффициент(ы) равны нулю
        for i in range(len(coef_list)):
            if coef_list[i] == 0:
                counter += 1
            else:
                break
        # Обработка условия, если многочлен с первой степенью или все коэффициенты многочлена равны нулю,
        # кроме коэффициента х с первой степенью и возврат строки многочлена
        if counter == k - 1:
            if coef_list[counter] > 1 or coef_list[counter] < -1:
                result += f"{str(coef_list[counter])}*x"
            elif coef_list[counter] == 1:
                result += f"x"
            elif coef_list[counter] == -1:
                result += f"-x"
            if coef_list[counter + 1] > 0:
                result += f" + {str(coef_list[counter+1])}"
            elif coef_list[counter + 1] < 0:
                result += f" - {str(abs(coef_list[counter+1]))}"

            return result
        # Начало сборки многочлена, нужно делать вне цикла, что бы не было лишних "+"
        if coef_list[counter] > 1 or coef_list[counter] < -1:
            result += f"{str(coef_list[counter])}*x^{k-counter}"
        elif coef_list[counter] == 1:
            result += f"x^{k-counter}"
        elif coef_list[counter] == -1:
            result += f"-x^{k-counter}"

        counter += 1
        # Основной цикл сборки многочлена, если коэффициент равен нулю, ни одно условие не выполняется, происходит переход к следующей степени и коэффициенту
        while counter < k - 1:
            if coef_list[counter] > 1:
                result += f" + {str(coef_list[counter])}*x^{str(k - counter)}"
            elif coef_list[counter] < -1:
                result += f" - {str(abs(coef_list[counter]))}*x^{str(k - counter)}"
            elif coef_list[counter] == 1:
                result += f" + x^{str(k - counter)}"
            elif coef_list[counter] == -1:
                result += f" - x^{str(k - counter)}"
            counter += 1

        # Заключительный этап сборки многочлена, выполняется вне цикла, чтобы не было записи вида x^1
        if coef_list[counter] > 1:
            result += f" + {str(coef_list[counter])}*x"
        elif coef_list[counter] < -1:
            result += f" - {str(abs(coef_list[counter]))}*x"
        elif coef_list[counter] == 1:
            result += " + x"
        elif coef_list[counter] == -1:
            result += " - x"

        counter += 1

        if coef_list[counter] > 0:
            result += f" + {str(coef_list[counter])}"
        elif coef_list[counter] < 0:
            result += f" - {str(abs(coef_list[counter]))}"
        return result

    # Если все коэффициенты перед переменными равны нулю или степень многочлена не корректна возникнет исключение index out of range, что будет являться признаком
    # невозможности сборки многочлена с такими коэффициентами
    except:
        print("\033[6m\033[31m{}\033[0m".format(
            "Многочлен с такими коэффициентами или степенью не возможен"))
        return None


k = input_validation_int("Введите максимальную степень многочлена: ")

polynom = create_polynomial(k)
print(
    f"Многочлен с максимальной степенью {k} и случайными целыми коэффициентами в промежутке [-10;10]: \n{polynom}")
