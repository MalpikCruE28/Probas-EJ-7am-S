##factorial

numerofactorial=int(input("ingrese un numero para calcular su factorial:"))
factorial=1

i=1
while (i<=numerofactorial):
    factorial=factorial*i
    i=i+1 

print(f"el valor del {numerofactorial} en factorial es de {factorial} ")
