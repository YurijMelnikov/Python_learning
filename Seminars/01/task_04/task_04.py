"""
Дано натуральное число.
Определите, является ли год с данным номером високосным
Год является високосным если его номер кратен 4, но не кратен 100, а так же если он кратен 400
"""

def leap_year_check (year:int) -> (bool):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input("Введите год:  "))
if leap_year_check(year):
    print("Год високосный")
else:
    print("Год не високосный")