

def suma(a=0, b=0):
    #esto hace parte del bloque de la funcion
    return a+b



def saludar(nombres, apellidos):
    print(f"Hola desde construccion de software {nombres} {apellidos}")


def acceso(año_nacimiento):
    edad=2021-año_nacimiento
    if edad >=18:
        print("bienvenido al establecimiento")
    else:
        print("no se le permite el acceso ")

acceso(2018)

