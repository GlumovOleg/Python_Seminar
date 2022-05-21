# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


print('Игра в конфетки :) Правила игры: \n\
    1. В начале игры укажите количество конфет, которые будут разыгрываться.\n\
    2. Каждый игрок может взять от 1 до 4 конфет за один ход.\n\
    3. Тот игрок, кто забирает последние конфеты побеждает и забирает все конфеты себе :) ')

konfety = int(input('Укажите количество конфект для розыгрыша: '))

# # Игрок против игрока

while konfety > 0:
    player_1 = int(input('Ход первого игрок: '))
    if player_1 >= 1 and player_1 <= 4:
        konfety = konfety - player_1
    else:
        print('Возьмите меньше конфет :)')
        player_1 = int(input('Ход первого игрок: '))
        if player_1 >= 1 and player_1 <= 4:
            konfety = konfety - player_1
    if konfety == 0:
        print('\nКонфеты розыграны :(')
        print('Все конфеты забирает первый игрок!')
        break
    else:
        print(f'Конфет осталось: {konfety}')

    player_2 = int(input('Ход второго игрок: '))
    if player_2 >= 1 and player_2 <= 4:
        konfety = konfety - player_2
    else:
        print('Возьмите меньше конфет :)')
        player_2 = int(input('Ход первого игрок: '))
        if player_2 >= 1 and player_2 <= 4:
            konfety = konfety - player_2
    if konfety == 0:
        print('\nКонфеты розыграны :(')
        print('Все конфеты забирает второй игрок')
        break
    else:
        print(f'Конфет осталось: {konfety}')

# Игрок против бота

# import random

# while konfety > 0:
#     player_1 = int(input('Ход игрока: '))
#     if player_1 >= 1 and player_1 <= 4:
#         konfety = konfety - player_1
#     else:
#         print('Возьмите меньше конфет (от 1 до 4) :)')
#         player_1 = int(input('Ход игрока: '))
#         konfety = konfety - player_1
#     if konfety == 0:
#         print('\nКонфеты розыграны :(')
#         print('Все конфеты забирает игрок!')
#         break
#     else:
#         print(f'Конфет осталось: {konfety}')

#     bot = random.randint(1, 4)
#     print(f'Ход бота: {bot}')
#     konfety = konfety - bot
#     if konfety == 0:
#         print('\nКонфеты розыграны :(')
#         print('Все конфеты забирает бот')
#         break
#     else:
#         print(f'Конфет осталось: {konfety}')
