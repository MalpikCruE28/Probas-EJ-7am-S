#calculadora de IMC 
peso=int(input("ingrese el peso de la persona en kg:"))

altura=float(input("ingrese la altura en metros:"))

IMC=(peso/(altura**2))

print(f"el IMC de la persona es de {IMC}")