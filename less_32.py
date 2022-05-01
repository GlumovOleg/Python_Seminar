# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k = int(input('Введите число: '))

def fibonachi(f):
    list = []
    a, b = 1, 1
    for i in range(f):
        list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for j in range(f +1):
        list.insert(0, a)
        a, b = b, a - b
    return list

list = fibonachi(k)
print(f'Список чисел Фибоначчи для числа {k}:\n{fibonachi(k)}')
