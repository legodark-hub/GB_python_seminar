# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(num, pow):
    if pow == 1:
        return num
    return num*exponentiation(num, pow-1)

print('введите число и степень через пробел')
num, pow = input().split(" ")
num, pow = int(num), int(pow)
print(exponentiation(num, pow))