# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = bool(input('Введите значение "true" или "false" для X: '))
y = bool(input('Введите значение "true" или "false" для Y: '))
z = bool(input('Введите значение "true" или "false" для Z: '))

if (not(x or y or z)) == (not x and not y and not z):
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истино')
else:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно')
