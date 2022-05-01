# Составить список простых множителей натурального числа N.

n = int(input('Введите натуральное число N: '))

for i in range(2, int(n ** 1/2) + 1):
    while (n % i == 0):
        print(i)
        n //= i

if (n != 1):
    print(n)


















# .....Черновики....

# def factors(n):
#     while n % 2 == 0:
#         print(2)
#         n = n / 2
#         for i in range(2, int(n ** 1/2) + 1):
#             while n % i == 0:
#                 print(i)
#                 n = n / i
#         if n > 2:
#             print(n)
#         if n != 1:
#             print(n)

# factors(n)

# n = int(input('Введите натуральное число N: '))

# for i in range(2, n + 1):
#     if n % i == 0:
#         count = 1
#         for j in range(2,(i//2 + 1)):
#             if (i % j == 0):
#                 count = 0
#                 # break
#         if (count == 1):
#             print(i)
