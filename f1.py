# tarea 1
# función hola()
# preguntar por el nombre de usuario
# imprimir un mensaje de bienvenida bonito

def hola():
    name = input("cual es tu nombre")
    print(f"Hola {name} !")

# definición a trabajar
def repetir(num):
    for i in num:
        return i


# Pasando parámetros a las funciones
def imprimir(a, b = "Hello"):
    print(a, b)  

# Imprimir muchos valores * es que podomos pasar muchas cosas
def imprimirNumeros(*args):
    print(args)

if __name__ == "__main__":

    # hola()

    # tarea 2
    # repetir 3 veces
    # for i in range(3):
    #     hola()


    # Pasando parámetros a las funciones
    # imprimir("Hola")
    # imprimir("Hola", "Kaixo")
    # imprimir(b = "Hola", a = "Kaixo")


    imprimirNumeros(29, 4593, 678)
