# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

import tkinter as tk


window = tk.Tk()
window.title('Главное меню :) ')
window.geometry('280x60+450+250')
window.resizable(False, False)
player = 1

def menu():
    print('Игра начинается!')
    if btn['state'] == tk.NORMAL:
        btn.config(state=tk.DISABLED)
    window.destroy()
    start_game()

def close_game():
    print('Игра закончена')
    exit()

def clear():
    global dict
    print('Перезапуск игры')
    app.destroy()
    dict = {'00': 0, '01': 0, '02': 0,
        '10': 0, '11': 0, '12': 0,
        '20': 0, '21': 0, '22': 0}  
    start_game()

def start_game():
    global app
    global title
    global game_board
    app = tk.Tk()
    app.title('Крестики - нолики')
    app.geometry('330x380+450+150')
    app.resizable(False, False)
    title = tk.Label(app, font=("FiraCode, 18"), text='Игра началась!')
    btn2 = tk.Button(app, text="Начать заново?", command=clear)
    btn3 = tk.Button(app, text="Завершить игру", command=close_game)
    btn3.pack(side=tk.BOTTOM)
    btn2.pack(side=tk.BOTTOM)
    title.pack(side=tk.TOP)
    game_board = tk.Canvas(app, height=300, width=300, background='white')
    game_board.create_line(100, 5, 100, 295, fill='grey')
    game_board.create_line(200, 5, 200, 295, fill='grey')
    game_board.create_line(5, 100, 295, 100, fill='grey')
    game_board.create_line(5, 200, 295, 200, fill='grey')
    game_board.bind('<Button>', clicked)
    game_board.pack()
    
    
    
def win_line():
    global game_board
    global dict
    if dict['00'] != 0 and dict['00'] == dict['01'] == dict['02']:
        game_board.create_line(25, 50, 275, 50, width=5, fill='green')
        return True
    elif dict['10'] != 0 and dict['10'] == dict['11'] == dict['12']:
        game_board.create_line(25, 150, 275, 150, width=5, fill='green')
        return True
    elif dict['20'] != 0 and dict['20'] == dict['21'] == dict['22']:
        game_board.create_line(25, 250, 275, 250, width=5, fill='green')
        return True
    elif dict['00'] != 0 and dict['00'] == dict['10'] == dict['20']:
        game_board.create_line(50, 25, 50, 275, width=5, fill='green')
        return True
    elif dict['01'] != 0 and dict['01'] == dict['11'] == dict['21']:
        game_board.create_line(150, 25, 150, 275, width=5, fill='green')
        return True
    elif dict['02'] != 0 and dict['02'] == dict['12'] == dict['22']:
        game_board.create_line(250, 25, 250, 275, width=5, fill='green')
        return True
    elif dict['00'] != 0 and dict['00'] == dict['11'] == dict['22']:
        game_board.create_line(25, 25, 275, 275, width=5, fill='green')
        return True
    elif dict['02'] != 0 and dict['02'] == dict['11'] == dict['20']:
        game_board.create_line(275, 25, 25, 275, width=5, fill='green')
        return True
    

    
def clicked(event):
    global player
    global dict
    x = event.x // 100 * 100
    y = event.y // 100 * 100
    position = str(event.y // 100) + str(event.x // 100)
    if dict[position] == 0 and not win_line():
        if player == 1:
            game_board.create_line(x + 20, y + 20, x + 80, y + 80, width=5, fill='red')
            game_board.create_line(x + 20, y + 80, x + 80, y + 20, width=5, fill='red')
            dict[position] = player
            player = 2
        else:
            game_board.create_oval(x + 20, y + 20, x + 80, y + 80, width=5, outline='blue')
            dict[position] = player
            player = 1
    if win_line():
        title.configure(text="Победа!")
    
dict = {'00': 0, '01': 0, '02': 0,
        '10': 0, '11': 0, '12': 0,
        '20': 0, '21': 0, '22': 0}   

lbl = tk.Label(window, text="Для запуска игры нажмите ----->>>")
lbl.grid(column=0, row=0)
btn = tk.Button(window, text="Начать",
                command=menu,
                activebackground='green')

lbl1 = tk.Label(window, text="Для закрытия игры нажмите ---->>>")
lbl1.grid(column=0, row=1)
btn1 = tk.Button(window, text="Завершить",
                 command=close_game,
                 activebackground='red')

btn.grid(column=2, row=0)
btn1.grid(column=2, row=1)

window.mainloop()
