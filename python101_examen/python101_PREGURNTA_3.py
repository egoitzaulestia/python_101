# Examen Python101
# PREGUNTA_3
# ————————————————————————————————————————————————————————————————————

# Teniendo un rectángulo de 10 metros de base y 3 metros de altura, crear una función para calcular su área.

# Acciones:

# Crear la función (2)
# Ejecutar la función con valores que proporciona el usuario (1)
# Modificar la función para que si el usuario ejecuta area(10), por defecto coge el valor 3 de altura (1)

# ————————————————————————————————————————————————————————————————————

# Creamos función para calcular el área
def calcularArea_1(a, b):
    return a * b

# Creamos función para calcular el área + "si el usuario ejecuta area(10), por defecto coge el valor 3 de altura".
def calcularArea_2(a, b):
    # Si el valor de la base introducida es 10, la altura coge el valor de 3 por defecto. 
    if a == 10:
        b = 3
        return a * b
    # Si no, imprime el valor del area respecto a la base y la altura introducida
    else:
        return a * b


if __name__ == "__main__":

    a = calcularArea_1(10, 5)
    print(a)

    a = calcularArea_2(10, 5)
    print(a)

    base = float(input("Introduce valor de la base: "))
    altura = float(input("Introduce valor de la altura: "))
    area = calcularArea_2(base, altura)
    print(f"El area del rectángulo es: {area:.2f}")


"""
Salida en terminal:

50
30
Introduce valor de la base: 5           # despues de introducir 5
Introduce valor de la altura: 5         # despues de introducir 5
El area del rectángulo es: 25.00

"""
