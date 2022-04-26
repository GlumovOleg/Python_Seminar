# Реализовать алгоритм перемешивания списка.

import random

list = [1, 18, 2, 6, 4, 5, 77, 24]

print(f'Исходный список: {list}')

list2 = random.sample(list, len(list))

print(f'Перемешаный список: {list2}')