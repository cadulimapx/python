sb=float(input("digite seu salario bruto: "))
if sb<2000:
    sl=sb-(sb*0.1)
    print(f"seu salario liquido é: {sl}")
else: 
    sl=sb-(sb*0.2)
    print(f"seu salario liquido e: {sl}")