def get_encabezado(ruta_archivo):
    with open(ruta_archivo, mode="r", encoding="utf-8")  as archivo:
        encabezado = next(archivo)
    array_encabezado = encabezado.split(",")
    for index in range(len(array_encabezado)):
        array_encabezado[index] = array_encabezado[index].strip()
    return array_encabezado


def get_valores(ruta_archivo):
    archivo = open(ruta_archivo, mode="r")
    lineas = archivo.readlines()
    archivo.close()
    lista_personajes = []
    for index, linea in enumerate(lineas):
        fila = linea.split(",")
        personaje = {"tipo": fila[0], "vida": fila[1], "ataque": fila[2], "defensa": fila[3], "alcance": fila[4]}
        lista_personajes.append(personaje)
    del lista_personajes[0]
    return lista_personajes







