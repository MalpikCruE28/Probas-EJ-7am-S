def es_palindromo():
    cadena = input("Introduce un texto para determinar si es palíndromo: ")
    cadena = cadena.replace(" ", "").lower()
    cadena2 = ""
    n = len(cadena)
    for i in range(n - 1, -1, -1):
        cadena2 += cadena[i]
    return cadena == cadena2

resultado = es_palindromo()
print("¿Es palíndromo?", resultado)