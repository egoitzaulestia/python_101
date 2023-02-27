# Crear la función calcular_cuenta en un restaurante con 2 parametros
# Cuenta - lo que hay que pagar en total
# Propina - por defecto 10%, pero es opcional (si el usuario pasa 12%, lo calcula con 12, si no, lo calcula con 10)
# devolver el total de la cuenta para pagar (cuenta + propina)

def calcular_cuenta(cuenta, propina = 10):
    # totalPlus = cuenta * propina / 100
    total = cuenta * (1 + 0.01 * propina)
    total = round(total, 2)
    return total
    

def imprimirDiasSemana(*dias):
    i = 1
    for dia in dias:
        print(f"{dia} es la {i} de la semana.")
        i += 1
    

def get_usuario():
    usuario = input("Introducir tu nombre de usuario")


# Argumentos by value
def ref_demo(x):
    x = 42
    print(x)

# Argumentos by ref/ by objects (por referencia)
def incrementar_ciudad(cities):
    cities.append("Madrid")
    


if __name__ == "__main__":
    # men
    # total = calcular_cuenta(100)
    # print(f"Hay que pagar ${total}")

    # total = calcular_cuenta(100, 15)
    # print(f"Hay que pagar ${total}")


    imprimirDiasSemana("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
    print("-" * 10)
    imprimirDiasSemana("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")


    x = 100
    ref_demo(x)

    ciudades = ["Donostia", "bilbao"]
    incrementar_ciudad(ciudades)
    print(ciudades)
