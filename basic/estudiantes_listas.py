

lista_estudiantes = []



def agregar(nombres, apellidos, telefono,codigo):
    estudiante = { "nombres":nombres, "apellidos": apellidos, "telefono": telefono,"codigo":codigo}
    lista_estudiantes.append(estudiante)


def buscar(codigo):
    cont=0
    for estudiante in lista_estudiantes:
        if estudiante["codigo"] == codigo:
           break
        cont +=1
    return cont


def eliminar(codigo):
    posicion = buscar(codigo)
    del lista_estudiantes[posicion]


def listar():
    for estudiante in lista_estudiantes:
        print(f'Nombres:  {estudiante["nombres"]}  Apellidos: {estudiante["apellidos"]} "Código: {estudiante["codigo"]}" ')




agregar("Mateo", "Jimenez", "31121321",1)

opciones = """
1.  Agregar
2.  Eliminar
3.  Listar
"""
print(opciones)

opcion = 3
while opcion > 0:
    if opcion == 1:
        nombres = input("Nombres: ")
        apellidos = input("Apellidos: ")
        telefono = input("Telefono: ")
        codigo = input("codigo ")
        agregar(nombres, apellidos, telefono, codigo)
    if opcion == 2:
        codigo = int(input("Digite el codigo del estudiante: "))
        eliminar(codigo)
    if opcion == 3:
        listar()
    print(opciones)
    opcion = int(input("Digite la opcion"))














