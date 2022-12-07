#Varias maneiras de responder a questão 1
#caractere = input("Digite a palavra desejada para a consulta: ")
#qnt = []

#for i in range(len(caractere)):
#   if (i%1 == 0):
#    qnt.append(caractere[i])

#print(qnt)

"""""
palavra = input

while(True):

    letra = input("Insira apenas um caractere: ")
    if (len(letra) == 1):
        break
    else:
        print("Você inseriu mais q1ue um caractere, insira novamente!")


print(f"O caractere '{letra}' na  palavra '{palavra}' apareceu '{checagem} vezes")
"""
"""""
def checarLetra(p,l):
    contador = 0

    for i in range(len(p)):
        if(p[i] == l):
            contador += 1
    return contador

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

print(checarLetra(palavra,letra))
"""

#Várias maneiras de responder a questão 2

"""""
def checagemSenha(s):
    if len(s) >=4 and len(s) <=8:
        if senha.isnumeric():
            print ("Senha inválida")
            global repetir
            repetir = False
        else:
            print(f"Sua senha tem {len(s)} digitos. Escreva uma senha que utilize apenas entre 4 e 8 digitos!")
    else:
        print ("Você digito senha inválida")

repetir = True
while(repetir):
    senha = input("Insira uma senha entre 4 e 8 digitos, que utilize apenas números: ")
    checagemSenha(senha)
"""

#Questão 4
"""""
numero = int(input("Insira um número inteiro: "))

resposta = numero

m = 0
c = 0
d = 0
u = 0

while(resposta != 0):
    if(resposta>=1000):
        resposta -= 1000
        m +=1
    elif (resposta>=100):
        resposta -= 100
        c += 1
    elif (resposta>=10):
        resposta -= 10
        d +=1
    elif (resposta>=1):
        resposta -= 1
        u +=1
    else: break

print(f"No número atual {numero} existem: número de milhares: {m}, número de centenas: {c}, número de dezenas: {d}, número de unidades: {u}.")
"""

alunos = list(range(20))

numerodeEquipes = int(input("Insira o número de equipes: "))

equipes = []

if(len(equipes)!=numerodeEquipes):
        for i in range(numerodeEquipes):
            equipes.append([])
        print(equipes)

while(len(alunos)>0):

    for i in range(len(equipes)):
        if(len(alunos)>0):
            equipes[i].append(alunos[0])
            alunos.pop(0)
            print(equipes)