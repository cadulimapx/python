n1=int (input("diga um numero: "))
n2=int (input("diga outro numero: "))
n3=int (input("diga mais um numero: "))

ordem = sorted([n1, n2, n3], reverse=True)
print (ordem)