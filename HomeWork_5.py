"""
Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. 
Вычислите результат.

Тесты:
1) "8-5+2-1"        -->     4
2) "0+0-1-0"        -->     -1
3) "-1-2+5-0+1"     -->     3
"""

# our_string = "-1-2+5-0+1"

# cur_value = ''
# amount = 0
# for i in range(len(our_string)):
#     if our_string[i] == '-' or our_string[i] == '+':
#         cur_value = our_string[i]
#     else:
#         cur_value += our_string[i]

#     print(cur_value)

#     if cur_value != '-' and cur_value != '+':
#         cur_value = int(cur_value)
#         amount += cur_value
    
# print('amount:', amount)


"""
Словом в данной задаче считается последовательность букв, 
ограниченная пробелами или началом или концом строки.
Выведите все слова из строки в столбик. 
НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

Тесты:
1) "Hello, world!"               -->     "Hello," "world!"
2) "My heart in the Highland"   -->     "My" "heart" "in" "the" "Highland"
"""

our_string = "My heart in the Highland"
cur_string = ''

for i in range(len(our_string)):
    cur_string += our_string[i]
    if our_string[i] == ' ' or i == len(our_string) - 1:
        print(cur_string)
        cur_string = ''