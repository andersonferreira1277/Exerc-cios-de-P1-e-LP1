#-*- coding: utf-8 -*-
from Tkinter import *
from conta import Conta
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError
import tkMessageBox

contas = {}
class Janela_principal:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Banco')
        self.janela.geometry('500x180')
        self.janela.resizable(width=False,height=False)
        self.bt_cadastrar = Button(text='Cadastrar', command=self.cadastrar)
        self.bt_saldo = Button(text='Saldo', command=self.saldo)
        self.bt_saque = Button(text='Saque', command=self.saque)
        self.bt_deposito = Button(text='Depósito', command=self.deposito)

        self.bt_saldo['width'] = 25
        self.bt_deposito['width'] = 25
        self.bt_cadastrar['width'] = 25
        self.bt_saque['width']=25
        self.bt_cadastrar.grid(row=0,column=0)
        self.bt_saldo.grid(row=1,column=0)
        self.bt_saque.grid(row=2,column=0)
        self.bt_deposito.grid(row=3,column=0)
        self.janela.mainloop()
    def deposito(self):
        self.lb1_deposito = Label(text='Nº conta deposito:')
        self.en_numero_conta = Entry()
        self.lb2_deposito = Label(text='Valor:')
        self.en_valor = Entry()
        self.bt_confirma_deposito = Button(text='Depositar', command=self.fazer_deposito)

        self.lb1_deposito.grid(row=4, column=1)
        self.en_numero_conta.grid(row=4, column=2)
        self.lb2_deposito.grid(row=5, column=1)
        self.en_valor.grid(row=5, column=2)
        self.bt_confirma_deposito.grid(row=5, column=3)
    def fazer_deposito(self):
        if contas.has_key(self.en_numero_conta.get()):
            conta = contas[self.en_numero_conta.get()]
            try:
                conta.op_deposito(float(self.en_valor.get()))
                self.lb_saldo = Label()
                self.lb_saldo['text'] = contas[self.en_numero_conta.get()]
                self.lb_saldo.grid(row=1, column=1)
            except:
                tkMessageBox.showerror('Erro', 'Valor inválido')
        else:
            tkMessageBox.showerror('Erro','Conta inválida')
        self.lb1_deposito.destroy()
        self.en_numero_conta.destroy()
        self.lb2_deposito.destroy()
        self.en_valor.destroy()
        self.bt_confirma_deposito.destroy()
    def saque(self):
        self.lb1_saque = Label(text='Nº conta saque:')
        self.en_numero_conta = Entry()
        self.lb2_saque = Label(text='Valor:')
        self.en_valor = Entry()
        self.bt_confirma_saque = Button(text='Sacar', command=self.sacar)

        self.lb1_saque.grid(row=2, column=1)
        self.en_numero_conta.grid(row=2, column=2)
        self.lb2_saque.grid(row=3, column=1)
        self.en_valor.grid(row=3, column=2)
        self.bt_confirma_saque.grid(row=3, column=3)
    def sacar(self):
        if contas.has_key(self.en_numero_conta.get()):
            conta = contas[self.en_numero_conta.get()]
            try:
                conta.op_saque(float(self.en_valor.get()))
                self.lb_saldo = Label()
                self.lb_saldo['text'] = contas[self.en_numero_conta.get()]
                self.lb_saldo.grid(row=1, column=1)
                tkMessageBox.showinfo('Realiazado', 'Saque realizado com sucesso')
            except:
                tkMessageBox.showerror('Erro', 'Valor inválido')
        else:
            tkMessageBox.showerror('Erro', 'Conta inválida')
        self.lb1_saque.destroy()
        self.en_numero_conta.destroy()
        self.lb2_saque.destroy()
        self.en_valor.destroy()
        self.bt_confirma_saque.destroy()
    def cadastrar(self):
        self.lb_cadastrar = Label(text='Número da conta:')
        self.en_cadastrar = Entry()
        self.bt_salva_cadastro = Button(text='Salvar', command=self.salva_cadastro)

        self.lb_cadastrar.grid(row=0, column=1)
        self.en_cadastrar.grid(row=0, column=2)
        self.bt_salva_cadastro.grid(row=0, column=3)
    def saldo(self):
        self.bt_mostra_saldo = Button(text='Mostrar', command=self.mostra_saldo)
        self.lb_saldo = Label(text='Número da conta:\n')
        self.en_saldo = Entry()

        self.lb_saldo.grid(row=1, column=1)
        self.en_saldo.grid(row=1, column=2)
        self.bt_mostra_saldo.grid(row=1, column=3)
    def mostra_saldo(self):
        if contas.has_key(self.en_saldo.get()):
            self.lb_saldo['text'] = contas[self.en_saldo.get()]

        else:
            self.lb_saldo.destroy()
            self.lb_saldo.destroy()
            tkMessageBox.showerror('Erro','Conta inválida')
        self.en_saldo.destroy()
        self.bt_mostra_saldo.destroy()
    def salva_cadastro(self):
        conta = Conta(self.en_cadastrar.get())
        if self.en_cadastrar.get().isdigit() and not contas.has_key(self.en_cadastrar.get()):
            contas[self.en_cadastrar.get()] = conta

            self.lb_cadastrar.destroy()
            self.en_cadastrar.destroy()
            self.bt_salva_cadastro.destroy()
        elif self.en_cadastrar.get() == '':
            tkMessageBox.showerror('Erro', 'Conta vazia.')
            self.lb_cadastrar.destroy()
            self.en_cadastrar.destroy()
            self.bt_salva_cadastro.destroy()
        elif not self.en_cadastrar.get().isdigit():
            tkMessageBox.showerror('Erro', 'Digite somente números.')
            self.lb_cadastrar.destroy()
            self.en_cadastrar.destroy()
            self.bt_salva_cadastro.destroy()
        else:
            tkMessageBox.showerror('Erro','Conta já existe.')
            self.lb_cadastrar.destroy()
            self.en_cadastrar.destroy()
            self.bt_salva_cadastro.destroy()

programa = Janela_principal()
