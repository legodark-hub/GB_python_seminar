# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)

print('введите числа через пробел')
numbers = [int(i) for i in input().split(" ")]
print('введите минимум')
min = int(input())
print('введите максимум')
max = int(input())
print([f"{numbers.index(i)}({i})" for i in numbers if i>=min and i<=max])