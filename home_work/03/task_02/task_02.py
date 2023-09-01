"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его. 
"""

list_1 = [1, 2, 3, 4, 5]
k = 6
value = list_1[0]
for item in list_1:
    if abs(item - k) < abs(value - k):
        value = item
print (value)