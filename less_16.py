# Написать программу проверки, является ли строка палиндромом


ss = str(input('Введите слово: '))

slovo = ss[::-1]
if ss == slovo:
  print(f'Слово {ss} является палиндромом')
else:
  print(f'Слово {ss} не является палиндромом')
