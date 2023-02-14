#_____
# listas - tipo de dato
# numeros = [5, 12, 10]

# for n in numeros:
#     print(n)


# datos = ["tenis", 23, 5.234, "Jon"]
# for dato in datos:
#     print(dato)


#_____
# range - tipo de dato, FOR
# a = range(10)
# print(type(a))
# print(a)

# for i in range(10):
#     print(i)
# print()

# for j in range(2, 20):
#     print(j)
# print()

#Loops "for" con salto
# for f in range(10, 100, 5):
#     print(f)

# for i in range(10):
#     print("Ego!")

# for i in range(5):
#     x = input("¿1?")
#     c = input("¿2?")
#     g = input("¿...?")


# Programa para imprimir to nombre 50 veces
# nombre = input("¿Cuál es tu nombre? ")
# for i in range(50):
#     print(f"{i + 1} _ {nombre}")
#     i = i + S1

# Programa para contar
accion = input("¿Teclear \"up\" para contar en positivo desde cero o teclear \"down\" para contar en negativo? ")

if accion == "up" or accion == "Up" or accion == "UP":
    numero_de_veces = int(input("¿Cuántas veces quieres repetir? "))
    for i in range(numero_de_veces):
        print(i)
        i = i + 1
elif accion == "down" or accion == "Down" or accion == "DOWN":
    numero_de_veces = int(input("¿Cuántas veces quieres repetir? "))
    for i in range(numero_de_veces, -1, -1):
        print(i)
else:
    print("ERROR: input incorrecto! Escribe bien la elección")


#_____
#Programa para gestionar los invitados de la fiesta
gente = int(input("Cuánta gente acudirá a la fiesta? "))
MAX_INVITADOS = 5

if gente > MAX_INVITADOS:
    print(f"Lo siento, solo {MAX_INVITADOS} personas pueden acudir a la fiesta.")
else:
    #preguntar el usuario por el nombre de cada invitado - repetir X veces
    #imprimir un mensaje individual para cada invitado

    #avanzado - guardad cada nombre en una lista e imprimir un mensaje individual para cada invitado
