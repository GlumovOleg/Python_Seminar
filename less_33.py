# Найти НОК (наименьшее общее кратное) двух чисел.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число : '))
a1, b1 = a, b
p = a * b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

res = p // (a + b)

print(f'Наименьшее общее кратное (НОК) чисел {a1} и {b1}: {res}')
