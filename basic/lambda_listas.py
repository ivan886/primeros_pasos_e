mi_lista = [1,3 ,5 ,8, 9, 15 ,20,10,25,13]
pares = []


for valor in mi_lista:
    if valor%2 == 0:
        pares.append(valor)


pares2 = list(filter( lambda valor: (valor%2==0), mi_lista))


mi_lista2 = []
for valor in mi_lista:
    mi_lista2.append(valor*3)


mi_lista3 = list(map(lambda valor: valor * 3, mi_lista ))

print(mi_lista3)
