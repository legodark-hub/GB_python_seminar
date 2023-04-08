# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна сумме последних 
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам 
# требуется написать программу, которая проверяет счастливость билета.

print("введите шестизначный номер билета")
number = input()
if len(number) != 6:
    print("неправильный ввод")
else:
    print("билет счастливый" if int(number[0]) + int(number[1]) + int(number[2]) == 
        int(number[3]) + int(number[4]) + int(number[5]) else "билет несчастливый")