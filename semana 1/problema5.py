#clculadora de descuentos 
preciooriginal=int(input("ingrese el precio original del producto:"))

descuento=int(input("ingrese el descuento que le desea aplicar:"))

desc=(preciooriginal*descuento)/100
preciofinal=(preciooriginal-desc)
print(f"el precio original del producto es de {preciooriginal}, su descuento fue del {descuento}% y su precio final es de {preciofinal} ")
