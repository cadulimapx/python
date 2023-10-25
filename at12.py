n1=float(input("digite seu numero: "))
n2=float(input("digite seu numero: "))
n3=float(input("digite seu numero: "))
if n1==n2==n3:
    print("seu numeros sao iguais!")
elif n1>n2 and n1>n3:
    print(f"seu maior numero é: {n1}")
elif n2>n1 and n2>n3:
    print(f"seu maior numero é: {n2}")

else:
    print(f"seu maior numero é: {n3}")
