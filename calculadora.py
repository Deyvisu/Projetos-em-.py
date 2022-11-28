repetir = True
while(repetir):

    repetir = False
    num1 = input("Digite o primeiro valor: ")
    if (num1.isnumeric()):

        num1 = float(num1)
        num2 = input("Digite o segundo número: ")

        if(num2.isnumeric()):
            num2 = float(num2)

        operador = input("Digite a operação ([+ ou SOMAR],[- ou SUBTRAIR],[/ ou DIVIDIR],[* ou MULTIPLICAR]): ")



        if (operador == "+" or operador.lower() == "somar"):
            
            print("A soma dos valores é: ",num1+num2)

        elif(operador == "-" or operador.lower() == "subtrair"):
            
            print("A subtração dos valores é: ",num1-num2)

        elif(operador == "/" or operador.lower() == "dividir"):
            
            if (num2 == 0):
                repetir = True
                print("Você tentou dividir por 0, a operação é inválida! Tente novamente!")
            else:
                print("A divisão dos valores é: ",num1/num2)

        elif(operador == "*" or operador.lower() == "multiplicar"):
            
            print("A multiplicação dos valores é: ",num1*num2)

        else:
            repetir = True
            print("O operador que você digitou é inválido!")
            print("Tente novamente!")

            #o codigo ta incompleto
