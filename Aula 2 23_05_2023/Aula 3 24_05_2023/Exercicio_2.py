print("\n-----------------------CALCULAR VELOCIDADE-----------------------\n")


velo  =int(input("Qual a velocidade do carro atualmenteh em km/: "))


if velo > 80:
    print(f"Você está a {velo} km/h então você será multado por isso.")
elif velo <= 80:
    print(f"Você está a {velo} km/h, então está dentro do limite e não será multado.")
