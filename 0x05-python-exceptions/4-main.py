#!/usr/bin/python3

from typing import List
list_division = __import__('4-list_division').list_division

my_l_1: List = [10, 8, 4]
my_l_2: List = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1: List = [10, 8, 4, 4]
my_l_2: List = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

