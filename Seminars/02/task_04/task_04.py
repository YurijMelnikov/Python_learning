import random
def find_max_min_mass(count_watermelon):
    max, min = 1, 21 
    for i in range(count_watermelon):
        mass = random.randrange(1,20)
        print(mass, end = " ")
        if max < mass:
            max = mass
        if min > mass:
            min = mass
    print(end = "\n")
    return min, max

count_watermelon = int(input("Введите кол-во арбузов: "))

print(find_max_min_mass(count_watermelon))