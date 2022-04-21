# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

list = []
n = int(input('Введите число N: '))
list.append(1)

for i in range(1, n):
    list.append(list[i-1] * (i +1))
print(list)

exit()

list = []
n = int(input('Введите число N: '))
a = 1

for i in range(1, n + 1):
    a *= i
    list.append(a)
print(list)