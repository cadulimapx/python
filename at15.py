km=float (input("informe seu percurso: "))
tipocarro= input("diga o tipo do carro: ")

if tipocarro=="A":
    consumo= km/8
    print ("o consumo de combustivel foi de: ", consumo,"litros")
elif tipocarro=="B":
    consumo= km/9
    print ("o consumo de combustivel foi de: ", consumo,"litros")
elif tipocarro=="C":
    consumo= km/12
    print ("o consumo de combustivel foi de: ", consumo,"litros")
else:
    print("carro invalido")