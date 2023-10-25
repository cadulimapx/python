l1=float(input("Digite o valor do lado esquerdo do triangulo: "))
l2=float(input("Digite o valor do lado direito do triangulo: "))
l3=float(input("Digite o valor do lado meio do triangulo: "))
if l1==l2==l3:
    print("seu triangulo é equilatero!")
elif l1!=l2 and l2!=l3 and l3!=l1:
    print("seu triangulo é escaleno!")
else:
    print("seu triangulo é isosceles!")