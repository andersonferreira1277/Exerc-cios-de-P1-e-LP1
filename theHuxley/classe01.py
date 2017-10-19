class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def imprimir(self):
        print("Imprimindo")

class Animal(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)
    def imprimir(self):
        print(self.nome)
nome2 = "Anderson"
a = Animal(nome2)
a.imprimir()
print(type(a))