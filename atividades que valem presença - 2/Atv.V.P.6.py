"""""texto = input("Digite um texto: ")

contagem = {}


for letra in texto:
    contagem[letra] = texto.count(letra)

    print(texto,contagem)

"""
#USANDO A COLEÇÃO

from collections import Counter

texto = input("Escreva um texto: ")

print(Counter(texto))