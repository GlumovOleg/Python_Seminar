# Написать программу преобразования десятичного числа в двоичное

number = int(input('Введите десятичное число: '))
num = number
n = ''

while number != 0:
    n =  str(number % 2) + n
    number //= 2
    print(n)
print()
print(f'Число {num} в двоичной системе: {n}')