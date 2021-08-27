#2. Programa que recibe el valor de tres productos y calcula el iva.
#en la impresión debe aparecer el total de los productos, el valor del iva y el total general.

producto1 = int(input("digite el valor del primer producto"))
producto2 = int(input("digite el valor del segundo producto"))
producto3 = int(input("digite el valor del tercer producto"))

valor_neto = producto1 + producto2 + producto3
iva = valor_neto *  0.19
total_general = valor_neto + iva

print("Valor Neto: ", valor_neto)
print("Iva: ", iva)
print("Total: ", total_general)