# Examen Python101
# PREGUNTA_2
# ————————————————————————————————————————————————————————————————————
# Crear un programa para:
# - Imprimir los valores de la siguiente lista, excluyendo los valores en negativo. (2)
# - Al imprimir, imprimes "Hola numero 6" si el valor es 6. (1)

# lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]

# ————————————————————————————————————————————————————————————————————

# Creamos la lista
lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]

# Creamos un loop con for para recorrer la lista
for num in lista:
    # Hacemos un if para compara si el número es igual o mayor a cero para así descartar cualquier número negativo
    if num >= 0:
        # Si el número coincide con 6 imprimimos "Hola número 6"
        if num == 6:
            print(f"Hola número {num}")
        # Si no es el número 6, solo imprimimos el número
        else:
            print(num)

"""
Salidaen terminal:

5
3
12
1
Hola número 6
8

"""