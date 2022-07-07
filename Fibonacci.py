def calcularFibonacci(numero):
    aux = 0
    v1 = 0
    v2 = 1
    while True:
        aux = v2
        v2 = v2 + v1
        v1 = aux
        if (numero == v2):
            print("Número está na lista!")
            break
        elif(numero < v2):
            print("Número não presente em lista!")
            break
numero = 3000000
calcularFibonacci(numero)