nota  = ()
nota2 = ()
nota3 = ()
i = 0

for i in range(3):
    n = float(input("Qual é a nota para ser calculada: "))
    i = i + 1
    if i == 1:
        nota = n
    elif i == 2:
        nota2 = n
    elif i == 3:
        nota3 = n

print("\n")

media = (nota + nota2 + nota3) / 3

print(f"\nA média do aluno é de {media}")



