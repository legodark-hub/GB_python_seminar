# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках
# записаны N целых чисел Ai. Последняя строка содержит число X
print('введите массив чисел через пробел')
numbers = [int(i) for i in input().split(" ")]
print('введите  число X')
number = int(input())
closenumber = numbers[0]
difference = abs(number - numbers[0])
for i in numbers:
    if abs(number - i) < difference:
        closenumber = i
        difference = abs(number - i)
print(closenumber)
