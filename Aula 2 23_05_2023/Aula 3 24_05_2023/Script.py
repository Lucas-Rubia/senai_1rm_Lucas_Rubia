print("\n-----------------------CALCULAR MÉDIA-----------------------\n")
nota1 = float(input("Digite a 1° nota do aluno(a): "))
nota2 = float(input("Digite a 2° nota do aluno(a): "))
nota3 = float(input("Digite a 3° nota do aluno(a): "))

media = (nota1 + nota2 + nota3)/3
print(f"A média calulada das notas é: {media:.2f}\n")

if media >= 6:
    print(f"O(A) aluno(a) foi APROVADO(A) com média {media:.1f}\n")
elif media >= 5:
   print(f"O(A) aluno(a) foi REPROVADO(A) com média {media:.1f} porém pode ir para o conselho de classe")
elif media < 5:
   print(f"O(A) aluno(a) foi REPROVADO(A) com média {media:.1f}\n")

