#Prototipo de la aplicación "Calculadora IVA" 
#realizado para el Banco Santander.

#El prototipo debe de falitar al usuario:
#   1 _ Calcular la suma del IVA a un precio que no lleva IVA.
#     + Para ello facilitar al usuario: 
#       - Introduccir precio sin IVA
#       - Intrudición del porcentaje de IVA
#   2 _ Calcular la resta del iva a un precio que incluye iva.
#     + Para ello facilitar al usuario:  
#       - Introducir precio toral con IVA
#       - Introducir porcentaje del IVA que lleva el producto


#Código del programa de la Calculadora IVA
print()
print("///// ""\033[1m" + "Banco Santander | Impulsa Empresa"  + "\033[0m" " \\\\\\\\\\")
print("////////////////////// \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("///// ""\033[1m" + "         Calculadora IVA         " + "\033[0m" " \\\\\\\\\\")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ //////////////////////")
print()
print("Bienvenido a la calculafora IVA del Santander | Impulsa Empresa.")
print()
choice = input("Si quiere sumar el IVA a un precio escriba ""\033[1m" + "\"sumar\"" + "\033[0m" + "\nSi quiere restar el IVA a un precio escriba ""\033[1m" + " \"restar\"" + "\033[0m" + "\nsumar")
print()
if choice == "sumar" or choice == "Sumar" or choice == "SUMAR":
    precio_sin_iva = float(input("///// (introduce) Precio sin IVA: "))
    iva_percentage = float(input("///// (introduce) Porcenta de IVA: "))
    iva_total = precio_sin_iva * (iva_percentage / 100)
    precio_total = precio_sin_iva + iva_total
    print()
    print(f"Porcentage de IVA seleccionado: {iva_percentage} %")
    print(f"Precio sin IVA: {precio_sin_iva:.2f} €")
    print(f"IVA: {iva_total:.2f} €")
    print(f"Precio con IVA: {precio_total:.2f} €")
elif choice == "restar" or choice == "Restar" or choice == "RESTAR":
    precio_total = float(input("///// (introduce) Precio con IVA: "))
    iva_percentage = float(input("///// (introduce) Porcenta de IVA: "))
    superporcentaje_iva = (iva_percentage + 100) 
    iva_total = (precio_total * iva_percentage) / superporcentaje_iva
    precio_sin_iva = precio_total - iva_total
    print()
    print(f"Porcentage de IVA seleccionado: {iva_percentage} %")
    print(f"Precio sin IVA: {precio_sin_iva:.2f} €")
    print(f"IVA: {iva_total:.2f} €")
    print(f"Precio con IVA: {precio_total:.2f} €")
else:
    print("\033[1m" + "¡ERROR!" + "\033[0m")
    print("Lo sentimos, no ha introducido las palabras correctas.")
    print("Reinicie el programa, por favor.")
print()
