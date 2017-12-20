from DB import GeradorDB
from Aluno import Aluno
from DadosDoAluno import DadosDoAluno
from DadosDeNascimento import DadosDeNascimento
from DadosDaTurma import DadosDaTurma


#teste da função insert
"""a = DadosDoAluno("Anderson Ferreira Câmara", "Adeilton", "Marineide")
b = DadosDeNascimento("07/03/1994", "Maceió", "Alagoas")
c = DadosDaTurma("3º ano", "Ensino Médio", 2018)
al = Aluno(a, b, c)

gerador = GeradorDB()
gerador.insert(al)"""

#teste da função select
"""gerador = GeradorDB()
imprimir = gerador.select('A')
for i in imprimir:
    print(i)"""

#teste da função update
"""a = DadosDoAluno("Anderson Ferreira 1277", "Adeilton", "Marineide")
b = DadosDeNascimento("07/03/1994", "Maceió", "Alagoas")
c = DadosDaTurma("3º ano", "Ensino Médio", 2018)
al = Aluno(a, b, c)
al.setID(1)

gerador = GeradorDB()
gerador.update(al)"""

#teste da função delete
"""gerador = GeradorDB()
print(gerador.deleteById(1))"""