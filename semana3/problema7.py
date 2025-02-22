
###calcular la mediana 
entrada = input("Ingresa los números separados por espacio: ")
numeros = [int(x) for x in entrada.split()]
numeros.sort()
n = len(numeros)
if n % 2 == 1:
    mediana = numeros[n // 2]
else:
    mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2

print("La mediana es:", mediana)