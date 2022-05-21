# # Дан список чисел. Создать список в который попадают числа,описывающие возрастающую последовательность
# # и содержащие максимальное количество элементов.
# # Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# #    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# #    ***!!!Порядок элементов менять нельзя!!!***

list = [1, 5, 2, 3, 4, 6, 1, 7]

new_list = []

for i in range(len(list)-1):
    index = i
    temp = [list[i]]
    while i < len(list) - 1:
        min_list = [i for i in list[index:] if i > temp[-1]]
        if len(min_list) != 0:
            pos_min = min(min_list)
        else:
            break
        temp.append(pos_min)
        index += list[index:].index(pos_min)
    if len(temp) > len(new_list):
        new_list = temp.copy()
        
print(f'Самая длинная последовательность: {new_list}')