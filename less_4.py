# Показать первую цифру дробной части числа

a = 150.3547

a = int(a * 10) % 10
print(a)

# a = 12.322
# b = str(a)
# for i in range(len(b)):
#     if b[i] == '.':
#         print(b[i+1])
