# Вычислить число Пи c заданной точностью d.
# Пример: при d = 0.001, Пи = 3.141. 10 ** (-1) <= d <= 10 ** (-10).

from math import pi

p = pi
d = float(input('Введите значение d в условии (10^(-1) <= d <= 10^(-10)): '))

def new_pi(n, d):
    return (n // d) * d

res = new_pi(p,d)

print(f'Число Пи: {p}')
print(f'Число Пи с точностью до d: {d} = {res}')

# Другой вариант (менее точный с округлением :-) )

# from math import pi

# n = pi
# d = str(input('Введите значение d в условии (10^(-1) <= d <= 10^(-10): '))
# # d = int(len(d) - 2)
# for i in range(int(len(d))):
#     i != '.'
# res = round(n, i)
# print(f'Число Пи: {n}')
# print(f'Число Пи с точностью d (чисел после запятой){d} = {res}')
