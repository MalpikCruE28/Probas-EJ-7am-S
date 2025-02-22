###problema 2 
numerosasumar = int(input("¿Cuántos números quieres sumar? "))
suma_total = 0


for i in range(numerosasumar):
    numero = float(input(f"Ingresa el numero {i + 1}:"))
    suma_total += numero
print(f"La suma total es: {suma_total}")