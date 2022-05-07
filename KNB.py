# Камень-ножницы-бумага (вариант игрок против игрока и игрок против бота)

import random

# Игрок против бота
list = 'камень', 'ножницы', 'бумага'
p = int(input('Введите количество попыток: '))
i = 1
count_player = 0
count_bot = 0

while i <= p:

    slovo = input(f'Введите один из вариантов ({list}): ')
    player = slovo.lower()
    
    if player not in list:
        print('Не верный вариант')
        break

    print(f'Игрок: {player}')
    # for i in range(100):
    if i >= 2:
        if i-1:
            player == 'камень'
            bot = 'бумага'
        elif player == 'ножницы':
            bot = 'камень'
        elif player == 'бумага':
            bot = 'ножницы'
        print(f'Бот: {bot}')
    else:
        bot = random.choice(list).lower()
        print(f'Бот: {bot}')


    if (player == 'ножницы' and bot == 'камень') or \
        (player == 'бумага' and bot == 'ножницы') or \
        (player == 'камень' and bot == 'бумага'):
        print('\nИгрок проиграл')
        count_bot += 1
            
    elif player == bot:
        print('\nНичья')

    else:
        print('\nИгрок победил')
        count_player += 1
        
    play_again = ''
    play_again = input('\nСыграем ещё? (да/нет):')
    if play_again != 'да':
        break
    
    i += 1
    
if i > p:
    print('Попытки исчерпаны {i} из {p}')
    print(f'Побед игрока: {count_player}')
    print(f'Побед бота: {count_bot}')
    
if play_again == 'нет':
    print(f'Пройдено {i} попыток из {p}')
    print(f'Побед игрока: {count_player}')
    print(f'Побед бота: {count_bot}')
    
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