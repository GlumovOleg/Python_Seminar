# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day = int(input('Введите день недели: '))

print(list[day-1])
if day == 6 or day == 7:
    print('Выходной')
else:
    print('Будний')
