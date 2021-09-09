path = "c:/Users/iv886/Desktop/proyectos/turismo/insert.csv"


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
            "name": isNone(fila[0].strip()),
            "lat": isNone(fila[1].strip()),
            "lon": isNone(fila[2].strip()),
        }
        lista.append(data)
    return lista


def print1(lista):
    f = open("c:/Users/iv886/Desktop/proyectos/saces/insert.sql", "w")
    for index, data in enumerate(lista):

        query = f"""INSERT   INTO   public.sites(category_id, name, description, lat, lon)  VALUES(41, {data["name"]}, 'des', {data["lat"]}, {data["lon"]} );  """
        print(query)
      #  f.write(query)
    f.close()


def isNone(valor):
    return "null" if valor == None or "".__eq__(valor) else f"{valor}"


lista = get_data(path)
print1(lista)






