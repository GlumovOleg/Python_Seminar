# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найти его и записать в файл.

data = open('file3.txt', 'r')
list = []
for i in data:
    list.append(i)
data.close()

number = 0
a = list[0].split(' ')
a = [int(i) for i in a]
list_1 = list[0].split(' ')
list_1 = [str(i) for i in a]
list_1 = ' '.join(list_1)

print(f'Исходные данные: {a}')

def search_number(num):
    x = [num[i] + 1 for i in range(len(num)-1) if num[i+1] != num[i] + 1]
    return x

number = search_number(a)
number = int(''.join(map(str,number)))
print(f'Недостающее число: {number}')

for i in range(len(a)):
    if i < a[i]-1 != a[i-1]:
        index = i

a.insert(index, number)

res = [str(i) for i in a]
res = ' '.join(res)

print(f'Заполненный порядок чисел: {res}')

data = open('file3_1.txt', 'w') #запись в новый файл, для возможности перезаписи
data.write('Source list:')
data.write(f'\n{list_1}\n')
data.write('\nMissing number:')
data.write(f'\n{number}\n')
data.write('\nNew list:\n')
data.write(f'{res}')
