# a = 10
# print(id(a))
# a = 11
# print(isinstance(a, int))
# print(type(a))

# if a == 10 or a == 11:
#     print("es igual a 10 o 11")
# elif a == 13:
#     print("es igual a 13")
# else:
#     print("otros")
    

# a = 100
# if a > 10:
#     print(f"La variable a con valor {a} es más que 10.")
# else:
#     print(f"La variable a con valor {a} es menor o igual a...")


#_____
#Ejercicio de comparativas

# b = int(input("Introducir un valor:"))
# if  b < 100: 
#     print(f"La variable b con valor {b} es menor que 100.")
# elif b > 100:
#     print(f"La variable b con valor {b} es mayor que 100.")
# elif b >= 100:
#     print(f"La variable b con valor {b} es mayor o igual al 100")
# else:
#     print(f"La variable b con valor {b} es negativo")


#_____
#Preguntar al usuario por su salario.
# salario = int(input("¿Cuál es tu salario actual en tu trabajo?")) #Preguntar al usuario por su salario
# salPy = salario * 10
# print(f"Esta es la cantidad que podrías ganar si fueras experto en Python: {salPy} €")


#_____
#Preguntar al usuario por dos números para después devolverle la suma de ellas
# num1 = int(input("Introduce un número: "))
# num2 = int(input("Introuduce un segurndo número: "))
# suma = num1 + num2
# print(f"La suma de {num1} y de {num2} es {suma}")


#_____
#Pasar números con decimales a numeros íntegros
# accionSan1 = 3.1453
# accionSan2 = 2.987
# accionSan3 = 3.5
# print(f"Estos son los últimos valores íntegros de las Acciones del SANTANDER: {int(accionSan1)}, {int(accionSan2)}, {int(accionSan3)}.")

# accionSantander = float(input("Intruduce el valor de la acciones del Santander: "))
# print(f"El valor integro de las acciones del Santander es: {int(accionSantander)}")

# acciones = [3.234, 4.655, 7.333]

# for accion in acciones:
#     resultado = int(accion)
#     print(f"El mainframe espera: {resultado}")


#_____
#Pasar números con decimales a numeros íntegros
# personas = int(input("¿Cuantas personas habéis ido a cenar? "))
# precio = float(input("¿Cuánto a costado la cena? "))
# pagoPersona = precio / personas
# print(f"Cada uno debe de pagar {pagoPersona:.2f} euros")


#_____
#Convertir kilos a libras //// 1 kilo equivaldria 2,205 libras
print("Bienvenido al convertidor entre kilos y libras.")
choice = input("Si quieres pasar Kilos a Libras pulsa k, si quieres pasar Libras a Kilos pulsa l: ")
if choice == "k" or choice == "K":
    kilos = float(input("Introduce el número de kilos: "))
    libras = kilos * 2.205
    print(f"{kilos} kilos son {libras:.2f} libras.")
elif choice == "l" or choice == "L":
    libras = float(input("Introduce el número de Libras:"))
    kilos = libras / 2.205
    print(f"{libras} libras son {kilos:.2f} kilos.")
else:
    print("No has introducido las letras correctas")

# accion = input("Qui")

# while 

#_____
#Vamos a mirar que tipo de datos son las variables a, b, y c
def numbers():
    return (10, 20, 30)
a, b, c = numbers()
print(f"tipos de datos: {type(a)}")
