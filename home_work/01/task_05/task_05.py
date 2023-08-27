# Посчитать сумму цифр любого целого или вещественного числа, число вводит пользователь. Через строку решать нельзя.

from decimal import Decimal
def sum_of_digits(number:Decimal) -> (int):
    sum = 0
    if (number % 1 != 0):
        while (number % 1 != 0):
            number *= 10
            print (number)
    while (number > 0):
        sum += number % 10
        number //= 10
    return sum

n = Decimal(input ("Введите число: "))
print (f"Сумма цифр числа {n} равна {int(sum_of_digits(n))}")