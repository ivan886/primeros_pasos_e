lista = []

lista = ["Juan Camilo ", 22, 2.5, True]

print(lista)

#operaciones
lista.append("Natalia")
print(lista)
lista.insert(1,"Nicolas")
print(lista)
lista.remove("Nicolas")
print(lista)
print(lista.pop(2))
print(lista)
lista.reverse()


for item in lista:
    print(item)