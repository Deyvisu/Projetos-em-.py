A = float(input("Digite a sua altura: "))
P = float(input("Digite seu peso: "))
S = str(input("Seu sexo é F ou M?: "))

if (S == "F"):
    P = ((62.1*A)-44.7)
    print("Seu peso ideal é: ",P)

elif (S == "M"):
    P = ((72.7*A)-58)
    print("Seu peso ideal é: ",P)

else:
    print("Digite um sexo valido")