"""
задача Де моргана необязательная
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
теперь надо проверить ее практически
в цикле 100 раз прогоняем
каждый раз генерируем случайное количество предикат от 3 до 15
и конечно со случайным булевым значением
и засекаем общее время выполнения программы
юзаем библиотеки random и time
предикаты НЕ ЗАДАЕМ как целое число!
"""
import random
import time

def boolean_list() -> (list):
    boolean_list = list()
    rnd = int
    for i in range(15):
        rnd = random.randint(0, 1)
        if rnd == 0:
            boolean_list.insert(i, False)
        else:
            boolean_list.insert(i, True)
    return boolean_list


def de_morgan_check(boolean_list: list) -> (bool):
    rnd = int
    a = bool
    b = bool
    a_string = str
    b_string = str
    random.shuffle(boolean_list)
    a_string = "not(boolean_list[0]"
    rnd = random.randint(3, 15)
    for i in range(1, rnd):
        a_string += f" or boolean_list[{i}]"
    a_string += ')'
    b_string = "not (boolean_list[0])"
    for i in range(1, rnd):
        b_string += f" and not(boolean_list[{i}])"
    a = eval(a_string)
    b = eval(b_string)
    if a == b:
        return True
    else:
        return False


start_time = time.time()
counter = 1
de_morgan = bool
boolean_list = boolean_list()
while counter <= 100:
    de_morgan = de_morgan_check(boolean_list)
    counter+=1
end_time = time.time()
print (f"Общее время выполнения задания {round((end_time - start_time) * 1000, 3)} миллисекунд")


# X = False
# Y = False
# Z = True
# a = not(X or Y or Z)
# b = not (X) and not (Y) and not(Z)
# print (a,b)
