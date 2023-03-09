"""
Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. 
Вычислите результат.

Тесты:
1) "8-5+2-1"        -->     4
2) "0+0-1-0"        -->     -1
3) "-1-2+5-0+1"     -->     3
"""

our_string = "-1-2+5-0+1"

# for i in range(len(our_string)):
#     cur_value = ''
#     print(our_string[i], " = ", end = '')
#     if i == 0 and int(our_string[i]):
#         cur_value = our_string[i]
#         cur_value = int(cur_value)
#     elif our_string[i] == "+" or our_string[i] == "-":
#         cur_value = our_string[i] + our_string[i+1]
#         cur_value = int(cur_value)
#     elif int(our_string[i]):
#         cur_value = our_string[i]
    
#     cur_value = int(cur_value)
#     print(cur_value, " --> ", type(cur_value))



cur_value = ''
amount = 0
for i in range(len(our_string)):
    if our_string[i] == '-' or our_string[i] == '+':
        cur_value = our_string[i]
    else:
        cur_value += our_string[i]

    print(cur_value)

    if cur_value != '-' and cur_value != '+':
        cur_value = int(cur_value)
        amount += cur_value
    
print('amount:', amount)