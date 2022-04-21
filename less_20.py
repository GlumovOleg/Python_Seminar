# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

list = []
n = int(input('Введите число N: '))
sum = 0

for i in range(1, n + 1):
    a = (1 + 1/i)**i
    list.append(a)
for i in list:
    sum += i
print(sum)
