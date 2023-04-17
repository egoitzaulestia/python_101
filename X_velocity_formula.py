# Programa para calcular la velocidad, distancia o tiempo

# Escribimos info sobre la funcion
def calc_velocidad(distancia, tiempo):
    return distancia / tiempo


if __name__ == "__main__": # Si utilizamos funciones
    print("Programa para calcular la velocidad, distancia y tiempo")

    # Preguntamos al usuario que es lo que quiere calcular
    answer = input("Que quieres calcular velocidad, distancia o tiempo? (v, d, t)")

    if answer.upper() == "V":
        distancia = float(input("Introduce valor distancia: "))
        tiempo = float(input("introduce cuantos segundos: "))
        velocidad = calc_velocidad(distancia, tiempo)
        print(velocidad)
    elif answer.upper() == "T":
        distancia = float(input("Introduce valor distancia: "))
        velocidad = float(input("Introduce valor velocidad: "))
        tiempo = distancia / velocidad
        print(tiempo)
    elif answer.upper() == "D":
        velocidad = float(input("Introduce valor velocidad: "))
        tiempo = float(input("introduce cuantos segundos: "))
        distancia = velocidad / tiempo
        print(distancia)