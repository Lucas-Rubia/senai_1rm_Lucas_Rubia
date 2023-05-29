print("\n-----------------------CALCULAR AJUSTE DE SALÁRIO-----------------------\n")

salario = float(input("Para mostrar o ajuste diga.Quanto você ganha:R$ "))


if salario >= 8250:
    reajuste = (salario * 0.10) + salario
    print(f"\nO seu salário teve um reajuste de 10% passando de R$ {salario} para R$ {reajuste}\n")
        
elif salario < 8250:
    reajuste = (salario * 0.15) + salario
    print(f"\nO seu salário teve um reajuste de 15% passando de R$ {salario} para R$ {reajuste}\n")