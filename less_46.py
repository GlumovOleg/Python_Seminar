# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


list = [1, 2, 3, 5, 1, 5, 3, 10]
res = []

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] == list[j] and i != j:
            break
    else:
        res.append(list[i])
print(res)