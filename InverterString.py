#Fiz de duas maneiras, não sabia se considerariam a primeira

def inverterString(palavra):
  return palavra[::-1]

palavra = input("Escreva a palavra: ")
print(inverterString(palavra))



palavra = input("Informe uma palavra: ")
inverso = []
for i in range(len(palavra)-1,-1,-1):
    inverso.append(palavra[i])

print(inverso)

