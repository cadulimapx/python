m1=float(input("digite sua media 1: "))
m2=float(input("digite sua media 2: "))
media=(m1+m2)/2 
if  media >= 7:
    print("vc foi aprovado!")
elif   media<7 and media>=3:
    print("vc tera que fazer a prova final!")  
elif media<3:
    print("vc foi reprovado!")