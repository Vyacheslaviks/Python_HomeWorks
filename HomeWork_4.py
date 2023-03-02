"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение)
"""

# from random import randint
import random

size_1 = int(input("Введите кол-во элементов первого множества: "))
size_2 = int(input("Введите кол-во элементов второго множества: "))

original_list_1 = []
original_list_2 = []

for i in range(size_1):
    original_list_1.append(random.randint(0, 10))

for i in range(size_2):
    original_list_2.append(random.randint(0, 10))

print("Список 1: ", original_list_1)
print("Список 2: ", original_list_2)

set_1 = set(original_list_1)
set_2 = set(original_list_2)

print("Множество 1: ", set_1)
print("Множество 2: ", set_2)

result_set = set_1.intersection(set_2)

print("Результирующее множество: ", result_set)

result_list = list(result_set)
result_list.sort()
print("Итоговый список: ", result_list)