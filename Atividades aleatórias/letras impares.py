"""palavra = input("Escreva uma palavra: ")

i = 0
impares = []

while (i<len(palavra)):
    impares.append(palavra[i])
    i+=2

print(impares)
"""

#usando o for

palavra = input("Digite uma palavra: ")
impares = []

for i in range(len(palavra)):
    if (i%2 ==0):
        impares.append(palavra[i])

print(impares)