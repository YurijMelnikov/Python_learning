"""
В некоторой школе решили набрать три новых мат. класса и оборудовать
кабинеты для них новыми партами. За каждой партой может сидеть два ученика. Известно количество учащихся в каждом из трёх классов.
Выведите наименьшее число парт, которые нужно приобрести для них
input: 20 21 22
output: 32
"""

import math
class1 = 20
class2 = 21
class3 = 22
deskCount = math.ceil(class1 / 2) + math.ceil(class2 / 2) + math.ceil(class3 / 2)
print(deskCount)
