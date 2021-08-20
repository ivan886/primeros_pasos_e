
numero_intentos = 7

def reducir_intentos():
    global numero_intentos
    numero_intentos = numero_intentos - 1

def seguir_jugando():
    print(numero_intentos)
    if numero_intentos > 0:
        print("puede continuar")
    else:
        print("game over")


def imprimir_numero_intentos():
    print(numero_intentos)


reducir_intentos()
reducir_intentos()
reducir_intentos()
reducir_intentos()
reducir_intentos()
reducir_intentos()
imprimir_numero_intentos()
seguir_jugando()