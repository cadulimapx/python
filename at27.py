precoetiq=float (input("Informe o valor de etiqueta do seu produto: "))
pagamento=float (input("Escolha a forma de pagamento: [1] a vista [2]cartao de credito [3]duas vezes sem juros [4]duas vezes com juros: "))

if pagamento==1:
    total= precoetiq - (precoetiq*0.1)
    print("o total a pagar é: ", total, " com desconto de 10%")
elif pagamento==2:
    total= precoetiq - (precoetiq*0.15)
    print ("o total a pagar é: ", total, " com desconto de 15%")
elif pagamento==3:
    total= precoetiq/2
    print ("o total sera duas parcelas de ", total, " sem juros")
elif pagamento==4:
    total= (precoetiq/2) + (precoetiq*0.1)
    print("o total sera duas parcelas de ",total, " com juros de 10%")