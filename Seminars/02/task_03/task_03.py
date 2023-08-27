import random

def count_plus_day(all_count_day):
    count_day = 0
    max_day = count_day
    for i in range(all_count_day):
        grad_day = random.randrange(-50,50)
        print(grad_day, end = " ")
        if grad_day < 1:
            if max_day < count_day:
                max_day = count_day
            count_day = 0
        else:
            count_day += 1
    print(end = "\n")
    return max_day


try:
    number = int(input("Введите общее кол-во дней: "))
    print(count_plus_day(number))
except:
    print("Ввели неверные данные")