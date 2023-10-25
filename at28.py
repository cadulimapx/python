num_chamada=int (input("informe o seu numero da chamada: "))
n1=float (input("informe sua nota parcial: "))
n2=float (input("informe sua nota bimestral: "))
n3=float (input("informe sua nota processual: "))

media = (n1+n2+n3)/3
media_aproveitamento = (n1 + n2*2 + n3*3 + media)/7

if media_aproveitamento >= 9:
    print("o aluno ", num_chamada, " sua nota parcial foi: ", n1, " sua bimestral foi: ", n2, " sua processual foi: ", n3, " sua media foi: ", media, " sua media de aprovetamento foi: ", media_aproveitamento, "[A] e ele foi aprovado.")
elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
    print("o aluno ", num_chamada, " sua nota parcial foi: ", n1, " sua bimestral foi: ", n2, " sua processual foi: ", n3, " sua media foi: ", media, " sua media de aprovetamento foi: ", media_aproveitamento, "[B] e ele foi aprovado.")
elif media_aproveitamento >= 6 and media_aproveitamento < 7.5:
    print("o aluno ", num_chamada, " sua nota parcial foi: ", n1, " sua bimestral foi: ", n2, " sua processual foi: ", n3, " sua media foi: ", media, " sua media de aprovetamento foi: ", media_aproveitamento, "[C] e ele foi aprovado.")
elif media_aproveitamento >= 4 and media_aproveitamento < 6:
    print("o aluno ", num_chamada, " sua nota parcial foi: ", n1, " sua bimestral foi: ", n2, " sua processual foi: ", n3, " sua media foi: ", media, " sua media de aprovetamento foi: ", media_aproveitamento, "[D] e ele foi reprovado.")
elif media_aproveitamento < 4:
    print("o aluno ", num_chamada, " sua nota parcial foi: ", n1, " sua bimestral foi: ", n2, " sua processual foi: ", n3, " sua media foi: ", media, " sua media de aprovetamento foi: ", media_aproveitamento, "[E] e ele foi reprovado.")