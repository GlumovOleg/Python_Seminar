# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
# print(round(int(list[0]) - int(list[0]),2))
for i in list:
    list2.append(round(i - int(i), 2))
# print(list2)
max = max(list2)
# print(max)
min = min(list2)
# print(min)
res = max - min
print(list)
print(round(res,3))