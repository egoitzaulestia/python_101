#Prototipo de la aplicación "Calculadora IVA" 
#realizado para el Banco Santander.

#El prototipo debe de facilitar al usuario:
#   1 _ Calcular la suma del IVA a un precio que no lleva IVA.
#     + Para ello facilitar al usuario: 
#       - Introduccir precio sin IVA
#       - Intrudición del porcentaje de IVA
#   2 _ Calcular la resta del iva a un precio que incluye iva.
#     + Para ello facilitar al usuario:  
#       - Introducir precio toral con IVA
#       - Introducir porcentaje del IVA que lleva el producto


###
#Código del programa de la Calculadora IVA:
###

#Impreimimos cabecera del programa
print()
print("///// ""\033[1m" + "Banco Santander | Impulsa Empresa"  + "\033[0m" " \\\\\\\\\\")
print("////////////////////// \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("///// ""\033[1m" + "         Calculadora IVA         " + "\033[0m" " \\\\\\\\\\")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ //////////////////////")
print()
print("Bienvenido a la calculafora IVA del Santander | Impulsa Empresa.") #Saludo de vienvenida al usuario
print()

#la variable "choice" almacena si el usuario quiere sumar o restar el iva a un precio
choice = input("Si quiere sumar el IVA a un precio escriba ""\033[1m" + "\"sumar\"" + "\033[0m" + "\nSi quiere restar el IVA a un precio escriba ""\033[1m" + " \"restar\"" + "\033[0m" + "\n")
print()

if choice == "sumar" or choice == "Sumar" or choice == "SUMAR": #Si el usuario quiere sumar elIVA entrará en el "if"
    precio_sin_iva = float(input("///// (introduce)" + "\033[1m" + " Precio sin IVA: " + "\033[0m")) #Recogemos a través un input el precio sin IVA en la variable "precio_sin_iva"
    iva_percentage = float(input("///// (introduce)" + "\033[1m" + " Porcenta de IVA: " + "\033[0m")) #Recogemos a través de un input el porcentaje de IVA en la variable "iva_percentage"
    iva_total = precio_sin_iva * (iva_percentage / 100) #La variable "iva_total" recoge la fórmula para calcular el precio del IVA
    precio_total = precio_sin_iva + iva_total #La variable "precio_total" guarda el valor total del precio con IVA
    print()
    print("\033[1m" + "Porcentage de IVA seleccionado: " + "\033[0m" + f"{int(iva_percentage)} %") #Mostramos porcentaje de IVA introducido
    print("\033[1m" + "Precio sin IVA: " + "\033[0m" + f"{precio_sin_iva:.2f} €") #Mostramos el precio sin IVA en euros
    print("\033[1m" + "IVA: " + "\033[0m" + f"{iva_total:.2f} €") #Mostramos el precio del IVA en euros
    print("\033[1m" + "Precio con IVA: " + "\033[0m" + f"{precio_total:.2f} €") #Mostramos el precio con IVA en euros 
elif choice == "restar" or choice == "Restar" or choice == "RESTAR": #Si el usuario quiere restar el IVA entrará en el "if"
    precio_total = float(input("///// (introduce)" + "\033[1m" + " Precio con IVA: " + "\033[0m")) #Recogemos a través un input el precio con IVA en la variable "precio_total"
    iva_percentage = float(input("///// (introduce)" + "\033[1m" + " Porcenta de IVA: " + "\033[0m")) #Recogemos a través de un input el porcentaje de IVA en la variable "iva_percentage"
    superporcentaje_iva = (iva_percentage + 100) #La variable "superporcentaje_iva" guarda el valor la suma entre el porcentaje de IVA introducido y 100(%) 
    iva_total = (precio_total * iva_percentage) / superporcentaje_iva #La variable "iva_total" recoge la fórmula oara crear la resta del IVA a un precio con IVA
    precio_sin_iva = precio_total - iva_total #Introducimos el valor del precio sin IVA en la variable "precio_sin_iva" 
    print()
    print("\033[1m" + "Porcentage de IVA seleccionado: " + "\033[0m" + f"{int(iva_percentage)} %") #Mostramos porcentaje de IVA introducido
    print("\033[1m" + "Precio sin IVA: " + "\033[0m" + f"{precio_sin_iva:.2f} €") #Mostramos el precio sin IVA en euros
    print("\033[1m" + "IVA: " + "\033[0m" + f"{iva_total:.2f} €") #Mostramos el precio del IVA en euros
    print("\033[1m" + "Precio con IVA: " + "\033[0m" + f"{precio_total:.2f} €") #Mostramos el precio con IVA en euros
else: #Si el usuario no introduce la palabra sumar/Sumar/SUMAR o restar/Restar/RESTAR entrara en else y le comunicará que el programa ha tenido un error
    print("\033[1m" + "¡ERROR!" + "\033[0m")
    print("Lo sentimos, no ha introducido las palabras correctas.")
    print("Reinicie el programa, por favor.")
print() #FIN del programa
