print("---------------------------CONTAGEM REGRESSIVA----------------------------")




from time import sleep

numeroInicial = int(input("Digite um número para iniciar a contagem regressiva: "))
numeroFinal = -1

def contagem_regresiva(numeroInicial,numeroFinal):
    for i in range(numeroInicial,numeroFinal,-1):
        print(i)
        sleep(0.5)

print(contagem_regresiva(numeroInicial,numeroFinal))