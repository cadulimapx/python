h=float(input("diga sua altura: "))
sexo= input("diga seu sexo [H ou M]: ")

sexo= sexo.upper()

if sexo== 'H':
    pesoideal=(72.7 * h) - 58
    print("o peso ideial para voce é: ", pesoideal)
elif sexo== 'M':
    pesoideal=(62.1 * h) - 44.7
    print("o peso ideial para voce é: ", pesoideal)