#-*- coding: utf- 8-*-
texto = open("mensagem.txt")
saida = open("cripto.txt", "w")
for linha in texto.readlines():
    for letra in linha:
        if letra in "aeiou":
            saida.write("*")
        else:
            saida.write(letra)