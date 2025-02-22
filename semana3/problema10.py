###det de matriz 3x3

print("Introduce los elementos de la matriz 3x3:")
a = int(input("Elemento [1,1]: "))
b = int(input("Elemento [1,2]: "))
c = int(input("Elemento [1,3]: "))
d = int(input("Elemento [2,1]: "))
e = int(input("Elemento [2,2]: "))
f = int(input("Elemento [2,3]: "))
g = int(input("Elemento [3,1]: "))
h = int(input("Elemento [3,2]: "))
i = int(input("Elemento [3,3]: "))
det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
print(f"El determinante de la matriz es: {det}")