# Определить, присутствует ли в заданном списке строк, некоторое число

list = ['a , b, c', 'd , r ,g', 'w, y, i']

n = 'e'
a = False

for i in range(len(list)):
    for j in list[i]:
        if j == str(n):
            print('Присутствует')
            break
        else:
            print('нет')
            continue
     
exit()
   
list = ['a , b, c', 'd , r ,g', 'w, y, i']

n = 'd'
a = False

for i in range(len(list)):
    for j in list[i]:
        if j == str(n):
            f = True
            
print(f)