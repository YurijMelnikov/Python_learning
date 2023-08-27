"""
Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
на два прямоугольника).

Выведите yes или no соответственно.
"""
a = 3
b = 2
c = 1

def check (a:int, b:int, c:int) -> (bool):
    if (c % a == 0 or c % b == 0) and (c >= a or c >= b) and (c < a*b):
        return True
    else:
        return False
    
if (check(a,b,c)):
    print ("yes")
else:
    print ("no")