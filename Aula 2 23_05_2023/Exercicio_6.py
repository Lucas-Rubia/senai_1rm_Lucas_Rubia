numero = int(input("Digite um número para saber a tabuada: "))
i = 0
for n in range(11):
    soma = (numero * i)
    print(F"{numero} x {i} = {soma} ")
    i = i + 1