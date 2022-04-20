# Сложить числа вещественного числа

n = float(input('Введите вещественное число: '))
sum = 0
for i in n:
    if n[i] != '.':
        sum += float(n[i])
print(round(sum))
