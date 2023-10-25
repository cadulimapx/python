valorcompra=int (input("diga o valor da compra: "))
valorpagamento=int (input("diga o valor do pagamento: "))

if valorpagamento < valorcompra:
    print("pagamento negado")
else:
    troco = valorpagamento - valorcompra
    nota100 = troco//100
    troco%=10
    nota10 = troco//10
    troco%=10
    nota1 = troco
    print("troco=",troco )
    print ("sao ", nota100, " notas de 100")
    print ("sao ", nota10, " notas de 10")
    print ("sao ", nota1, " notas de 1")