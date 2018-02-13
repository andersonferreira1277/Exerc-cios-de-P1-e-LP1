#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
from Tkinter import *
def Imprmir():
    texto["text"] = "mudando..."
i = Tk()
i.title("Olá mundo")
i.geometry("800x600")

texto = Label(i, text = "Olá mundo",bg = "red", fg = "white")
texto.pack()

ent = Entry(i)
ent.pack()

b = Button(i, text ="Clique", command = Imprmir)
b.pack()

i.mainloop()