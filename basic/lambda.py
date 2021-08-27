
def cuadrado(x):
    return x*x

cuadrado1 = lambda x: x*x
print(cuadrado(7))
print(cuadrado1(7))


mayor_edad = lambda edad: True if edad>=18 else False

edad = int(input("Edad:"))
print(mayor_edad(edad))


