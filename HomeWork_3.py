"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

Тесты:
1) [0, 1, 0, 1, -2, 1], 0    -->    2
2) [0, 1, 0, 1, -2, 1], 1    -->    3
2) [0, 1, 0, 1, -2, 1], 2    -->    0
"""

# some_list = [0, 1, 0, 1, -2, 1]
# sought_number = int(input("Введите искомое число: "))

# count = 0

# for i in some_list:
#     if sought_number == i:
#         count += 1
    
# print(f"Искомое число всетрчается в списке {count} раз")


"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

Тесты:
1) [3, 3, 10, -5, 8], -3    -->     [3] = -5
2) [3, 3, 10, -5, 8], 9     -->     [2] = 10, [4] = 8
3) [3, 3, 10, -5, 8], 10     -->    [2] = 10
"""

some_list = [3, 3, 10, -5, 8]
number = 9

min_difference = 0
min_difference_idx = 0

for i in range(0, len(some_list)):
    if some_list[i] - number < 0:
        difference = number - some_list[i]
    else:
        difference = some_list[i] - number

    print(difference)

    if i == 0:
        min_difference = difference
        min_difference_idx = i

    if difference < min_difference:
        min_difference = difference
        min_difference_idx = i

print(f"[{min_difference_idx}] = {some_list[min_difference_idx]} (разница - {min_difference})")