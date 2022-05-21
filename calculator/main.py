from complex_num import complex_nums as comp
from racional_num import rac_nums as rac
import logging

print('\nДобро пожаловать в калькулятор! \n'
      'Для работы с ним, перед решением примера вначале выберите тип чисел:\n'
      "1 - Рациональные числа"'\n'"2 - Комплексные числа")

start = input('Выберите какой пример хотите решить: ')

case = ('*', '/', '+', '-')

if start == '1':
    a = input('Введете первое число: ')
    b = input('Введете второе число: ')
    c = input(f'Выбирите действие из {case}: ')
    result = rac(a, b, c)

if start == '2':
    a = input('Введете первое число("j" у второго числа можно не указывать): ')
    b = input('Введете второе число("j" у второго числа можно не указывать): ')
    c = input(f'Выбирите действие из {case}: ')
    result = comp(a, b, c)

primer = a, c, b

print(f'\nЗаданный пример: {primer}')
print(f'\nРезультат выражение = {result}')

data = open('result.txt', 'w')
data.write(f'{primer} '+' = ')
data.write(f'{result}')
data.close()