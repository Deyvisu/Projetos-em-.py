notas = []

while len(notas) < 5:
    valores = float(input("Escreva as notas: "))
    notas.append(valores)

print(notas)
soma_das_notas = sum(notas)
media = (soma_das_notas)/5
print("A soma das notas é: ",soma_das_notas)
print("A média das notas é: ",media)
print("Os valores maiores que a média são: ")

for nota in notas:
    if nota > media:
        print(nota)     #Entendi mais ou menos como se faz, porém não ficou claro
