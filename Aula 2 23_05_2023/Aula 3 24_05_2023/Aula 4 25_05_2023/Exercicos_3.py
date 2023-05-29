print("\n-----------------------TABUADA----------------------\n")


numero = int(input("Digite um número para saber a tabuada: "))
for n in range(11):
    soma = (numero * n)
    print(F"{numero} x {n} = {soma} ")
    