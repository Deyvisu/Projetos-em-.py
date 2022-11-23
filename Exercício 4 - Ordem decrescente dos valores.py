valorA = float(input("Digite o valor de A: ")) 
valorB = float(input("Digitve o valor de B: "))
valorC = float(input("Digite o valor de C: "))

if (valorA < valorC):
    valorA, valorC = valorC, valorA
    print("A ordem decrescente dos valores é: ",valorA,",",valorB,",",valorC)

elif (valorA < valorB):
    valorA, valorB = valorB, valorA
    print("A ordem decrescente dos valores é: ",valorA,",",valorB,",",valorC)

elif (valorB < valorC):
    valorB, valorC = valorC, valorB
    print("A ordem decrescente dos valores é: ",valorA,",",valorB,",",valorC)

elif (valorA == valorB == valorC):
    print("Os três valores são iguais")
