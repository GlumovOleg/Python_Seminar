# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
from tkinter import *
window = Tk()
window.title('Крестики нолики :) ')
window.geometry('320x320')

def clicked():  
    res = "Привет {}".format(txt.get())  
    lbl.configure(text=res)
    
lbl = Label(window, text="Привет")  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Жми, что бы начать", command=clicked)  
btn.grid(column=2, row=0) 
window.mainloop()