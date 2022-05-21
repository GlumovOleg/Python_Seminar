# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
# a) входные и выходные данные хранятся в отдельных текстовых файлах

data = 'aaaaabbbccccccddaaaa'
count = 1
res = ''
start = ''

for i in data:
    if i != start:
        if start != '':
            res += str(count) + start
        count = 1
        start = i
    else:
        count += 1
res += str(count) + data[-1]
        
print(res)