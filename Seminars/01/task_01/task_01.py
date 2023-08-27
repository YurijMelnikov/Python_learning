"""
За день машина проезжает n километров. Сколько дней нужно для проезда по маршруту m километров
Input:
n = 700
m = 750
Output: 
2
"""
import math
n = 700
m = 750
dayTime = m / n
print(math.ceil(dayTime))