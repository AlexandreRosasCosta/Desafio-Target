#def inverterString(texto):
#  return texto[::-1]
#
#texto = input("Escreva a palavra: ")
#print(inverterString(texto))


palavra = input("Informe uma palavra: ")
inverso = []
for i in range(len(palavra)-1,-1,-1):
    inverso.append(palavra[i])

print(inverso)

