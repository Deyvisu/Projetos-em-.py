"""def helloworld():
    print("Hello world")


def hello(meu_nome):
    print("Hello",meu_nome)

helloworld()

hello(input( "Digite seu nome: "))

nome = (input("Digite seu nome: "))
hello(nome)


def hello(meu_nome,minha_idade):
    print("Olá",meu_nome,"\ Sua idade é: ", minha_idade)

helloworld()

nome = (input("Digite seu nome: "))
idade = (input("Digite a sua idade: "))

hello(nome, idade)

"""

#Calcular pagamento definindo funções: 

def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas*taxa
    else:
        horas_extras = horas - 40
        salario = 40*taxa+(horas_extras*(1.5*taxa))
    return salario

horastrabalhadas = input("Quantas horas você trabalhou?: ")
valorDahora = input("Quanto custa a sua hora?: ")

salariorecebido = calcular_pagamento(horastrabalhadas,valorDahora)

print(f"Você recebeu R${salariorecebido}")