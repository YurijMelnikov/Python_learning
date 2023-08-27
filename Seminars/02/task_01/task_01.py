#Факториал числа

def calc_factorial (number:int) -> int:
    if number == 0:
        return 1
    result = 1
    while number > 1:
        result = result*number
        number-=1
    return result

n = int (input("Введите число: "))
print (f"{n}! = {calc_factorial(n)}")