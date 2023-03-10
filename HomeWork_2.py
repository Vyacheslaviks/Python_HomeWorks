"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть

Тесты:
5 монет:
1) о, о, р, о, р --> 2
2) р, о, р, р, р --> 1
3) о, о, о, о, о --> 0
"""

# coin_amount = int(input("Введите кол-во монеток: "))
# heads_amount = 0    # кол-во орлов
# tails_amount = 0    # кол-во решек
# count = 0

# print("Сейчас нужно будет ввести положение монет, 0 - это орел, 1 - решка")
# while count < coin_amount:
#     current_coin = int(input("Введите положение монетки: "))
#     if current_coin == 0:
#         heads_amount += 1
#     elif current_coin == 1:
#         tails_amount += 1
#     else:
#         print("Неккореткное значение. Введите значение заново!!!")
#         coin_amount += 1
#     count += 1

# if heads_amount == 0 or tails_amount == 0:
#     print("Монетки не нужно переворачивать, они все в одном положении")
# elif heads_amount < tails_amount:
#     print(f"Нужно перевернуть {heads_amount} монетки с орлами")
# elif tails_amount < heads_amount:
#     print(f"Нужно перевернуть {tails_amount} монетки с решками")


"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.

Тесты:
1) Сумма = 5, Произведение = 6    -->        x = 2, y = 3
2) Сумма = 38, Произведение = 240    -->     x = 30, y = 8
"""

# S = int(input("Введите сумму чисел: "))
# P = int(input("Введите произведение чисел: "))

# discrim = S ** 2 - 4 * P

# # добавил приведение к типу 'int' так как в условиях указанны именно натуральные числа
# x = int((S + discrim ** 0.5) / 2)
# y = int((S - discrim ** 0.5) / 2)

# print(x, y)


"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Тесты:
1) 20    -->    1, 2, 4, 8, 16
2) 256   -->    1, 2, 4, 8, 16, 32, 64, 128, 256
"""

# number = int(input("Введите число: "))
# count = 0

# while number >= 2 ** count:
#     print(2 ** count)
#     count += 1