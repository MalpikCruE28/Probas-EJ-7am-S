###MCD
a = int(input("introduce el primer numero: "))
b = int(input("introduce el segundo numero: "))
while b != 0:
    a, b = b, a % b  
print(f"El MCD de los números es: {a}")