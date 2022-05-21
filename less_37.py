# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. *
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите степень k: '))
list = [randint(0,101) for i in range(k + 1)]
print(list)
res = [f'{list[i]}*x^{len(list)-i - 1}'\
    if len(list)-i - 1 != 0 else f'{list[i]}'\
    for i in range(len(list)) if list[i] != 0]
# print(res)
print(' + '.join(res) + ' = 0')

data = open('file2.txt', 'a')
data.write(' + '.join(res) + ' = 0\n')
data.close()