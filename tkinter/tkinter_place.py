#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
from Tkinter import *
def bt_clique():
    if str(ed.get()).isdigit() and str(ed2.get()).isdigit():
        num1 = int(ed.get())
        num2 = int(ed2.get())
        lb["text"]= num1+num2
    else:
        lb["text"] = "Valores invalidos!"
janela = Tk()

lb = Label(janela, text="Calculadora")
lb.place(x=140,y=30)
ed = Entry(janela)
ed.place(x=140, y=60)

ed2 = Entry(janela)
ed2.place(x=140, y=90)

bt = Button(janela, width=20, text="OK", command=bt_clique)
bt.place(x=140, y=170)

#wxh+l+t
janela.title("Calculadora")
janela.geometry("400x200+100+50")
janela.mainloop()