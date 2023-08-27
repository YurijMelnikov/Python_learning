"""
Валентина прогуляла лекцию по математике.
Преподаватель решил подшутить над нерадивой студенткой и
попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.
​
Решить такое вручную, как вы понимаете, практически нереально.
Вот Валентина и обратилась к вам за помощью.
Помогите ей (при помощи функции all_divisors(number), которую напишете сами).
Постарайтесь найти самое оптимальное решение.
Результат представьте в виде списка (не забудьте отсортировать по возрастанию).
"""

import math
import itertools
import time


def all_divisors_enumeration(number: int) -> (list):
    all_divisors = list()
    all_divisors.append(1)    
    for i in range(2, number//2+1):
        if number % i == 0:
            all_divisors.append(i)
    all_divisors.append(number)   
    return all_divisors


def prime_divisors(number: int) -> (list):
    n = number
    prime_divisors_list = list()
    i = 2
    while (i < number//2+1):
        if (n % i == 0):
            n /= i
            prime_divisors_list.append(i)
        else:
            i += 1
    return prime_divisors_list


def all_divisors(prime_divisors_list: list, number: int) -> list:
    all_divisors_list = list()
    for i in range(2, len(prime_divisors_list)):
        buff_list = list(itertools.permutations(prime_divisors_list, i))
        for j in range(len(buff_list)):
            all_divisors_list.append(math.prod(buff_list[j]))        
    all_divisors_list.append(1)
    all_divisors_list.append(number)
    all_divisors_list += prime_divisors_list
    all_divisors_list = list(set(all_divisors_list))
    all_divisors_list.sort()
    return all_divisors_list




n = int(input("Введите число: "))
start_time = time.time()
prime_divisors_list = prime_divisors(n)
end_time = time.time()
print (f"Время выполнения поиска простых делителей: {round((end_time - start_time)*1000, 4)}мс")
start_time = time.time()
divisors = list(all_divisors(prime_divisors_list, n))
end_time = time.time()
print (f"Время поиска всех положительных делителей математическим способом: {round((end_time - start_time)*1000, 4)}мс")
print(divisors)
start_time = time.time()
divisors2 = list(all_divisors_enumeration(n))
end_time = time.time()
print (f"Время поиска всех положительных делителей итеративным методом перебора: {round((end_time - start_time)*1000, 4)}мс")
print(divisors2)