"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""


def count_of_min (random_list:list)->int:
    counter = 0
    for i in range(1, len(random_list)):
        if random_list[i] > random_list[i - 1]:
            counter+=1
    return counter




s = [0, -1, 5, 2, 3]
print (count_of_min(s))