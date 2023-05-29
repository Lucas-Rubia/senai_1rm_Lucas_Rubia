print("---------------------------DESCOBRINDO A ARÉA----------------------------")


largura = float(input("Qual é a largura do terreno? "))
comprimento = float(input("Qual é o comprimento do terreno? "))

def area(largura,comprimento):
    total = largura * comprimento
    return total


print(f"A área do reterno é {area(largura,comprimento)}m²")