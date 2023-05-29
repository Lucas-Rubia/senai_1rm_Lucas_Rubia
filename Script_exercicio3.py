nome = input("Qual é o seu nome? ")
dia = int(input("Que dia você nasceu? "))
mes = input("Que mês você nasceu? ")
ano = int(input("Em que ano você nasceu? "))



if mes == "1":
    mes = "Janeiro"
elif mes == "2":
    mes = "Fevereiro"
elif mes == "3":
    mes = "Março"
elif mes == "4":
    mes = "Abril"
elif mes == "5":
    mes = "Maio"
elif mes == "6":
    mes = "Junho"
elif mes == "7":
    mes = "Julho"
elif mes == "8":
    mes = "Agosto"
elif mes == "9":
    mes = "Setembro"  
elif mes == "10":
    mes = "Outubro"
elif mes == "11":
    mes = "Novembro"
elif mes == "12":
    mes = "Dezembro"    

print("Olá {}! Você nasceu em {} de {} de {}".format(nome,dia,mes,ano))

