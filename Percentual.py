totalPercentual = 67836.43 + 36678.66 + 27165.48 + 29229.88 + 19849.53
def calcularPercentual(estado):
    return round((estado*100)/totalPercentual)

opcao = input("Escolha o estado: ")
match opcao:
    case 'SP': estado = 67836.43
    case 'RJ': estado = 36678.66
    case 'ES': estado = 27165.48
    case 'MG': estado = 29229.88
    case default: estado = 19849.53

percentualEstado = calcularPercentual(estado)
print("O percentual do estado de "+opcao+" é de "+str(percentualEstado)+"%")
