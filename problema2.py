#comparacion de numeros
A=int(input("ingrese el primer numero a comparar"))


B=int(input("ingrese el segundo numero a comparar"))

if A>B:
    print("el primer numero es mayor que el segundo")
else:
    if B>A:
        print("el segundo numero es mayor que el primero")
    else:
        if A==B:
            print("los dos numero son iguales")
            