# Найдите сумму цифр трехзначного числа.
print('введите трёхзначное число')
number = input()
if len(number) != 3:
    print("неправильный ввод")
else:
    print(int(number[0]) + int(number[1]) + int(number[2]))