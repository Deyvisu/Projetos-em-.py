# """def helloworld():
#     print("Hello world")


# def hello(meu_nome):
#     print("Hello",meu_nome)

# helloworld()

# hello(input( "Digite seu nome: "))

# nome = (input("Digite seu nome: "))
# hello(nome)


# def hello(meu_nome,minha_idade):
#     print("Olá",meu_nome,"\ Sua idade é: ", minha_idade)

# helloworld()

# nome = (input("Digite seu nome: "))
# idade = (input("Digite a sua idade: "))

# hello(nome, idade)

# """

# #Calcular pagamento definindo funções: 

# #def calcular_pagamento(qtd_horas, valor_hora):
# #    horas = float(qtd_horas)
# #    taxa = float(valor_hora)
# #    if horas <= 40:
# #        salario = horas*taxa
# #    else:
# #        horas_extras = horas - 40
# #        salario = 40*taxa+(horas_extras*(1.5*taxa))
# #    return salario

# #horastrabalhadas = input("Quantas horas você trabalhou?: ")
# #valorDahora = input("Quanto custa a sua hora?: ")

# #salariorecebido = calcular_pagamento(horastrabalhadas,valorDahora)

# #print(f"Você recebeu R${salariorecebido}")

# #def calcular_imc(peso, altura):
#  #   print("Seu imc é: ",peso / altura ** 2)

# #calcular_imc(55, 1.64)

# #def e(b):
#     #a = b * b
#     #return a
# #a = 10

# #e(a)
# #e(a)

# #print(e(a))

# def gorjetaGar(valorTotal):
#     print("O valor da gorjeta é: ",valorTotal*0.1)


# #ou

# #def gorjetaGar(valorTotal):
# #    gorjeta = valorTotal * 0.1
# #    return gorjeta

# #valorGorjeta = gorjetaGar(300)
# #print(valorGorjeta)


def soma(numero1, numero2):
    return float(numero1) + float(numero2)

def subtração(numero1, numero2):
    return float(numero1) - float(numero2)

def divisão(numero1, numero2):
    if (numero2 == "0"):
        return "O número 2 não pode ser 0"
    else:
        return float(numero1) / float(numero2)

def multiplicação(numero1, numero2):
    return float(numero1) * float(numero2)

def calculadora(n1,n2,op):
    
    if(op == "+"):
        print(soma(n1,n2))

    elif(op == "-"):
        print(subtração(n1,n2))

    elif(op == "/"):
        print(divisão(n1,n2))

    elif(op == "*"):
        print(multiplicação(n1,n2))

    else:
        print("Você digitou uma operação inválida!")
        global repetir
        repetir = True

repetir = True
while (repetir):
    repetir = False

    num1 = input("Digite o primeiro valor: ")
    num2 = input("Digite o segundo valor: ")
    operador = input("Digite o operador (+,-,/.,*): ")

    if (num1.isnumeric()) and (num2.isnumeric()):
        calculadora(num1, num2, operador)

    else:
        print("O usuário digitou números inválidos!")
        repetir = True