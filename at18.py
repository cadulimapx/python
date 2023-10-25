nome= input("diga seu nome: ")
sexo= input("diga seu sexo [F OU M]: ")
estadocivil= input("diga seu estado civil: ")

sexo = sexo.upper()
estadocivil = estadocivil.upper()

if sexo=="F" and estadocivil=="CASADA":
    tempocas= input("informe seu tempo de casada: ")
    print (nome, " tem ", tempocas,"anos de casada")
else:
    print(nome, " é do sexo ",sexo, " e seu estado civil é", estadocivil)