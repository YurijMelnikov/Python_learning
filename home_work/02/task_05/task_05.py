"""
Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
Одно число - это не последовательность.

Пример:

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8
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
            print("Вы ввели не целое число, повторите ввод")


def filling_list(count_list: int) -> list:
    result_list = list()
    for i in range(count_list):
        result_list.append(10000-i)
    return result_list


# Идея состоит в том, чтобы составить список списков всех возможных непрерывно возрастающих последовательностей и найти
# самую длинную из них, или несколько, если есть разные последовательности с одинаковым количеством цифр
def max_sequence(random_list: list) -> list:
    # для начала для меньшего количества вычислений и гарантии отсутствия повторяющихся последовательностей: избавимся от одинаковых значений функцией set()
    random_list = list(set(random_list))
    result = list()
    sequence_list = list()

    # Функция для вычисления непрерывно возрастающей последовательности, которая работает рекурсивно, поочерёдно сравнивая каждый следующий элемент последовательности
    # со всем списком, если последовательность прерывается - прерывается и рекурсия
    def list_check_sequence(random_list: list, index: int) -> list:
        for i in range(len(random_list)):
            if random_list[i] == random_list[index] + 1:
                sequence_list.append(random_list[i])
                list_check_sequence(
                    random_list, random_list.index(random_list[i]))
        return sequence_list
    # Проходим по каждому элементу массива и составляя для него возможную последовательность и записывая в список списков
    for i in range(len(random_list)):
        sequence_list.clear()
        sequence_list = list_check_sequence(random_list, i)
        sequence_list.insert(0, random_list[i])
        # Условие на проверку, если в списке последовательности одно значение, то оно не записывается в список последовательностей
        if len(sequence_list) > 1:
            result.append(list(sequence_list))
    # Вычисляем максимальную длину подсписка, который и будет ответом на задачу
    try:
        max = len(result[0])
        for i in range(len(result)):
            if max < len(result[i]):
                max = len(result[i])
    except:
        print("В списке нет сплошных возрастающих последовательностей")
        return None
    final_result = list()
    # Второй цикл нужен, для записи итогового результата в список списков, если есть одинаковые по длине последовательности, они не будут упущены
    for i in range(len(result)):
        if len(result[i]) == max:
            final_result.append(list(result[i]))

    return final_result


# int_list = [1, 5, 3, 4, 1, 7, 8, 15, 13, 14]
# print(int_list)
# print(
#     f"Максимальная(ые) сплошная(ые) возрастающая(ие) последовательность(и) -> {max_sequence(int_list)}")
# int_list = [1, 5, 2, 3, 4, 6, 1, 7]
# print(int_list)
# print(
#     f"Максимальная(ые) сплошная(ые) возрастающая(ие) последовательность(и) -> {max_sequence(int_list)}")
# int_list = [1, 5, 3, 4, 1, 7, 8, 15, 1]
# print(int_list)
# print(
#     f"Максимальная(ые) сплошная(ые) возрастающая(ие) последовательность(и) -> {max_sequence(int_list)}")
# int_list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]
# print(int_list)
# print(
#     f"Максимальная(ые) сплошная(ые) возрастающая(ие) последовательность(и) -> {max_sequence(int_list)}")
# int_list = [1, 3, 5, 7, 9, 11, 13]
# print(int_list)
# print(
#     f"Максимальная(ые) сплошная(ые) возрастающая(ие) последовательность(и) -> {max_sequence(int_list)}")


lenght = input_validation_int("Введите количество элементов списка: ")
list_r = list()
list_r = filling_list(lenght)
result = max_sequence(list_r)
print(list_r)