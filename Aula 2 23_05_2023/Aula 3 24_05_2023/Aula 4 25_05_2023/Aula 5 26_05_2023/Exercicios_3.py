print("---------------------------DESCOBRINDO O NÚMERO MAIOR----------------------------")

numeros=[]

def maior (numeros):
    for i in range(0,3):
        num1 = int(input("Digite um número: "))
        numeros.append(num1)

    numeros.sort(reverse=True)
    resposta = numeros[0]
    return resposta
    
print(f"\nO maior número dos números digitados é {maior(numeros)}")


