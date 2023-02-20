"""
Найдите сумму цифр трехзначного числа.

Тесты:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

# number = int(input("Введите число: "))

# amount_number = number % 10
# number = number // 10

# amount_number += number % 10
# number //= 10

# amount_number += number % 10

# print(f"Сумма цифр числа = {amount_number}")



# вариант через цикл

# number = int(input("Введите число: "))
# amount_number = number % 10

# while number > 0:
#     number //= 10
#     amount_number += number % 10

# print(f"Сумма цифр числа = {amount_number}")


"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Тесты:
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""

# total_number = int(input("Введите общее число сделанных журавликов: "))

# petya_number = total_number // 6
# sergey_number = petya_number
# kate_number = (petya_number + sergey_number) * 2

# print("Петя сделал - {} журавликов\nКатя сделала - {} журавликов\nСергей сделал - {} журавликов\n".format(petya_number, kate_number, sergey_number))


"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

Тесты:
385916 -> yes
123456 -> no
"""

# number = int(input("Введите номер билета: "))

# right_amount = 0
# left_amount = 0

# for i in range(3):
#     right_amount += number % 10
#     number //= 10

# for i in range(3):
#     left_amount += number % 10
#     number //= 10

# print("Сумма первых трёх цифр - {}\nСумма последних трех цифр - {}".format(left_amount, right_amount))

# if right_amount == left_amount:
#     print("----YES----")
# else:
#     print("----NO----")


"""
Требуется определить, можно ли от шоколадки размером n x m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

Тесты:
3 2 4 -> yes
3 2 1 -> no
"""

n = 3
m = 2
k = 4

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("----YES----")
else:
    print("----NO----")