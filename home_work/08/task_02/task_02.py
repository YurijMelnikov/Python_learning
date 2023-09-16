"""
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**

1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""
# Странное описание у задачи, надеюсь я правильно понял, что от меня хотят
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


# Надеюсь я правильно понял условие задания
def print_operation_table(num_rows, num_columns, operation=lambda x, y: x * y):
    buff_list = list()
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            buff_list.append(operation(i, j))
        print(*buff_list)
        buff_list.clear()


num_rows = input_validation_int("Введите число строк: ")
num_columns = input_validation_int("Введите число столбцов: ")
print_operation_table(num_rows, num_columns)
