# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

print('введите N')
n = int(input())
result = 1
pow = 1
while result < n:
    print(result)
    result = 2**pow
    pow+=1
        
