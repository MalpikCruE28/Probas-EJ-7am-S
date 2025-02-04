#conversion de temperaturas
tempC=int(input("ingrese la temperatura en celsius para convertir a farenheit y kelvin"))
convF=(tempC*9)/5+32
conV=(tempC+273.15)

print(f"la temperatura en celsius es de {tempC}°")
print(f"la temperatura en farenheit es de {convF}°")
print(f"la temperatura en kelvin es de {conV}°")