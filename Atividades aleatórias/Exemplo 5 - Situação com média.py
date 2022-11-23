nome = input("Informe o nome da(o) aluna(o): ")
nota1 = float(input("Insira a nota 1 da(o) aluna(o): "))
nota2 = float(input("Insira a nota 2 da(o) aluna(o): "))
nota3 = float(input("Insira a nota 3 da(o) aluna(o): "))
nota4 = float(input("Insira a nota 4 da(o) aluna(o): "))
media = (nota1 + nota2 + nota3 + nota4)/4

if (media >= 7.0):
    print(nome,"foi aprovada(o), sua média foi: ",media)

elif (media <= 4.9):
    print(nome,"foi reprovada(o), sua média foi: ",media)

else:
    (5.1<=media<=6.9)
    print(nome,"ficou de recuperação, sua média foi: ",media)