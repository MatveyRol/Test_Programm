from tkinter import *
from translate import Translator
perevod = Translator(from_lang="ru", to_lang="en")
def clicked(ent):
    lbl.configure(text=perevod.translate(ent))
window = Tk()
window.title =("Translator")
window.geometry('400x300+400+250')
lbl = Label(window, text="Введите слово на русском:", font=("AppleGothic",10))
lbl.grid(column=20, row=0)
ent = Entry(window)
ent.grid(column=20, row=1)
btn = Button(window, text="Перевести", font=("AppleGothic", 40), command=clicked)
btn.grid(column=20, row=2)
window.mainloop()