# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.
import os

clear = lambda: os.system('cls')
clear()

data = open('file2.txt', 'r')
list = []
list1_1 = []
list1_2 = []
for i in data:
    if i != '\n':
        list.append(i)
data.close()

list_2 = list[0].split(' ')
list_3 = list[1].split(' ')
list_2 = [i for i in list_2 if i not in {'+', '0\n', '='}]

for j in list_2:
    if len(j) <= 2:
        list1_1.append(j)
    elif j[-1] == '6':
        if j[1] == '*':
            list1_1.append(j[0])
        elif j[2] == '*':
            list1_1.append(j[:2])
    elif j[-1] == '5':
        if j[1] == '*':
            list1_1.append(j[0])
        elif j[2] == '*':
            list1_1.append(j[:2])
    elif j[-1] == '4':
        if j[1] == '*':
            list1_1.append(j[0])
        elif j[2] == '*':
            list1_1.append(j[:2])
    elif j[-1] == '3':
        if j[1] == '*':
            list1_1.append(j[0])
        elif j[2] == '*':
            list1_1.append(j[:2])
    elif j[-1] == '2':
        if j[1] == '*':
            list1_1.append(j[0])
        elif j[2] == '*':
            list1_1.append(j[:2])
    elif j[-1] == '1':
        if j[1] == '*':
            list1_1.append(j[0])
        elif j[2] == '*':
            list1_1.append(j[:2])
    else:
        list1_1.append(0)

result_1 = [int(i) for i in list1_1]

print(list_2)
print(result_1)

list_3 = [i for i in list_3 if i not in {'+', '0\n', '='}]

for j in list_3:
    if len(j) <= 2:
        list1_2.append(j)
    elif j[-1] == '6':
        if j[1] == '*':
            list1_2.append(j[0])
        elif j[2] == '*':
            list1_1.append(j[:2])
    elif j[-1] == '5':
        if j[1] == '*':
            list1_2.append(j[0])
        elif j[2] == '*':
            list1_2.append(j[:2])
    elif j[-1] == '4':
        if j[1] == '*':
            list1_2.append(j[0])
        elif j[2] == '*':
            list1_2.append(j[:2])
    elif j[-1] == '3':
        if j[1] == '*':
            list1_2.append(j[0])
        elif j[2] == '*':
            list1_2.append(j[:2])
    elif j[-1] == '2':
        if j[1] == '*':
            list1_2.append(j[0])
        elif j[2] == '*':
            list1_2.append(j[:2])
    elif j[-1] == '1':
        if j[1] == '*':
            list1_2.append(j[0])
        elif j[2] == '*':
            list1_2.append(j[:2])
    else:
        list1_2.append(0)

result_3 = [int(i) for i in list1_2]

sum = [x+y for x, y in zip(result_1, result_3)]

print(list_3)

print(result_3)
print(f'Сумма многочленов: {sum}')

data = open('file2_result.txt', 'w')
data.write(f'{sum}\n')
data.close()