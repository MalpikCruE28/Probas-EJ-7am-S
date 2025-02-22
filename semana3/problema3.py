##funcion lambda

cantidad = int(input("¿Cuántos números quieres sumar? "))

numeros = [float(input(f"Ingresa el número {i + 1}: ")) for i in range(cantidad)]

print(sum(numeros))