"""
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод: Ввод:
5 5
1 2 3 4 5 1 5 1 5 1
Вывод: Вывод:
0 2
"""
import random

size = 10
random_list = [random.randint(-10, 10) for i in range(size)]
print (random_list)

list_1 = [9,8,15,5, 2, 1, 10]

# count = 0
# for i in range(-1, len(list_1)-1):
#     if list_1[i] > list_1[i+1] and list_1[i] > list_1[i-1]:
#         count +=1
#         print(list_1[i])
# print(count)

# print(sum([1 for x in range(-1, len(list_1)-1) if list_1[x] > list_1[x+1] and list_1[x] > list_1[x-1]]))
# print(sum([1 for x in range(-1, len(list_1)-1) if list_1[x-1] < list_1[x] > list_1[x+1]]))
# random_list = [1, 2, 3, 4, 5]

# result_list = [item for i in range (1, len(random_list)) if ]


counter = 0
for i in range (len(random_list)):
    if i == 0:
        if random_list[i] < random_list[-1] and random_list[i] < random_list[i+1]:
            counter += 1
    elif i !=0 and random_list[i] < random_list[i-1] and random_list[i] < random_list[i+1]:
        counter+=1
    elif i == len(random_list) - 1:
        if random_list[i] < random_list[0] and random_list[i] < random_list[i-1]:
            counter += 1
print (counter)