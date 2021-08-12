nombre = 'jennifer margarita guerrero'

print(nombre.capitalize())
print(nombre.upper())
print(nombre.lower())
print(nombre.isdigit())
print(len(nombre))
print(nombre.replace('jennifer', "Anita"))
print(nombre.find('m'))
print(nombre.isalpha())

# Manejo de sub_strings
print(nombre[15])
print(nombre[0:3])
print(nombre[8:-1])
print(nombre[nombre.find('m'):-1])

print(3 * nombre)


# ciclos repetitivos

for character1 in nombre:
    print(character1)
    print("corresponde al bloque de for")
    print("esto tambien ")

print("aqui sali del bloque")

