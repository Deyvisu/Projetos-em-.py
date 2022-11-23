"""largura = int(input("Digite a largura: "))
altura = int(input("Digita a altura: "))

linha = ""

for i in range(largura):
    linha += "@ "

for i in range(altura):
    print(linha)
"""

#tem as duas maneiras de fazer, a de cima e essa: 

largura = int(input("Digite a largura: "))
altura = int(input("Digita a altura: "))

print((("# "*largura)+"\n")*altura)