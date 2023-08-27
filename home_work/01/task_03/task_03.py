"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
"""
n = 385916


def check_ticket(n:int) -> (bool):
    m = 0
    d = 0
    while n > 999:
        m += n % 10
        n //= 10
    while n > 0:
        d += n % 10
        n //= 10
    if m == d:
        return True
    else:
        return False

if (check_ticket(n)):
    print("YES")
else:
    print("NO")