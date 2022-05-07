# Камень-ножницы-бумага (вариант игрок против игрока и игрок против бота)

import random

# Игрок против бота

while True:

    list = ("Камень", "Ножницы", "Бумага")
    slovo = input(f'Введите один из вариантов {list}: ')

    player = slovo
    print(f'Игрок: {player}')
    bot = random.choice(list)
    print(f'Бот: {bot}')

    if (player == 'Ножницы' and bot == 'Камень') or \
        (player == 'Бумага' and bot == 'Ножницы') or \
        (player == 'Камень' and bot == 'Бумага'):
        print('Игрок проиграл')
        
    elif player == bot:
        print('Ничья')

    else:
        print('\nИгрок победил')
    
    play_again = ''
    play_again = input('\nСыграем ещё? (да/нет):\n')
    if play_again != 'да':
        break

exit()
# Игрок против игрока

list = ("Камень", "Ножницы", "Бумага")
slovo = input(f'Первый игрок - введите один из вариантов {list}: ')
slovo2 = input(f'Второй игрок - введите один из вариантов {list}: ')

player = slovo
print(f'Первый игрок: {player}\n')
player2 = slovo2
print(f'Второй игрок: {player2}\n')

if (player == 'Ножницы' and player2 == 'Камень') or \
    (player == 'Бумага' and player2 == 'Ножницы') or \
    (player == 'Камень' and player2 == 'Бумага'):
    print('Победил второй игрок')

elif player == player2:
    print('Ничья')
else:
    print('Победил первый игрок')