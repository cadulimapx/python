peso= float(input("diga seu peso: "))
altura= float(input("diga sua altura: "))

IMC= peso/altura*2

if IMC<18.5:
    print("abaixo do peso")
elif IMC>=18.5 and IMC<25:
    print("peso normal")
elif IMC>=25 and IMC<30:
    print("acima do peso")
elif IMC>=30:
    print("obeso")