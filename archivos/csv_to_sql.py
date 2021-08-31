import time
import random

path = "c:/Users/iv886/Desktop/proyectos/saces/registro1.csv"


def get_encabezado(ruta_archivo):
    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        encabezado = next(archivo)
    array_encabezado = encabezado.split(";")
    for index in range(len(array_encabezado)):
        array_encabezado[index] = array_encabezado[index].strip()
    return array_encabezado



def get_data(ruta_archivo):
    archivo = open(ruta_archivo, mode="r")
    lineas = archivo.readlines()
    archivo.close()
    lista = []
    for index, linea in enumerate(lineas):
        fila = linea.split(";")

        data = {
                "snies_programa":        isNone(fila[0].strip()),
                "estado":                isNone(fila[1].strip()),
                "resolucion":            isNone(fila[2].strip()),
                "fecha_resolucion":      isNone(fila[3].strip()),
                "vigencia":              isNone(fila[4].strip()),
                "fecha_notificacion":    isNone(fila[5].strip()),
                "fecha_ejecutoria":      isNone(fila[6].strip()),
                "fecha_vencimiento_dec_1330":isNone(fila[7].strip()),
                "ajuste_dec_1330":      isNone(fila[8].strip()),
                "fecha_vencimiento":    isNone(fila[9].strip()),
        }
        lista.append(data)
    del lista[0]
    return lista


def print1(lista):
    f = open("c:/Users/iv886/Desktop/proyectos/saces/insert.sql", "w")
    for index, data in enumerate(lista):
        query = f"""INSERT INTO temporal_registro(snies_programa, estado, resolucion, fecha_resolucion, vigencia, fecha_notificacion, fecha_ejecutoria,fecha_vencimiento_dec_1330, ajuste_dec_1330, fecha_vencimiento) VALUES( {data["snies_programa"]}, {data["estado"]}, {data["resolucion"]}, {data["fecha_resolucion"]}, {data["vigencia"]},{data["fecha_notificacion"]}, {data["fecha_ejecutoria"]}, {data["fecha_vencimiento_dec_1330"]},{data["ajuste_dec_1330"]},{data["fecha_vencimiento"]} );\n"""
        f.write(query)
    f.close()

        

def isNone(valor):
    return "null" if valor == None or "".__eq__(valor)  else f"'{valor}'"


lista = get_data(path)
print1(lista)






