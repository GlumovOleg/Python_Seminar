# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

line = 'Привет, мир'
line1 = 'Привет'

count = 0
slin = line.split(',')

for i in range(len(slin)):
    if line1 == slin[i]:
        count +=1
print(count)

        
