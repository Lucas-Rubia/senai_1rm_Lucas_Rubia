print("\n-----------------------NÚMERO FATORIAL-----------------------\n")


num = int(input("Digite um número para a contagem de fatorial: "))
fat = 1

for cont in range(1, num + 1):
    fat *= cont

print (f"\nO fatorial de {num} é {fat}\n")