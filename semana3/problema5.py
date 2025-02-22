##calculo de promedio 

suma=0
A=int(input("cuantas calificaciones deseas sacar el promedio: "))
for i in range (A):
     calificacion=float(input(f"ingrese la calificacion {i+1}: "))
     suma+=calificacion
promedio=suma/A
print(f"la suma de la calificacion es de {suma} y el promedio es {promedio}")
