# Заполните массив элементами арифметической прогрессии. Её первый
# элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print('введите первый элемент  арифметической прогрессии')
a1 = int(input())
print('введите разность арифметической прогрессии')
d = int(input())
print('введите количество элементов арифметической прогрессии')
n = int(input())
print([a1+(i-1)*d for i in range(1,n+1)])