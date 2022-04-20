# Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды
# в 1 дне 86400 секунд
# в 1 часе 3600 секунд
# в 1 минуте 60 секунд


n = int(input('Введите количество секунд: '))

days = n//86400
hours = (n//3600) % 24
minutes = (n//60) % 60
seconds = (n % 60)
if hours < 10:
    hours = '0' + str(hours)
else:
    hours = hours
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = minutes
if seconds < 10:
    seconds = '0' + str(seconds)
else:
    seconds = seconds
print(f'дни: {days} часы: {hours} минуты: {minutes} секунды: {seconds}')
