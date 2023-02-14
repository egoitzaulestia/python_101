#TIPOS DE IVA
#—————
#IVA tipo general       = 21%
#IVA tipo reducido      = 10%
#IVA tipo superreducido = 4%

#_00_
#¿CÓMO CALCULAR EL IVA?
#Pata calcular el IVA que vamos a repercutir o soportar en un factura, 
#hay que terner tres aspectos claros:
#   • La BASE IMPONIBLE que corresponde a cada concepto
#   • El TIPO DE GRAVAMEN que debe aplicarse a cada concepto
#   • La FÓRMULA del IVA

#_00.1_
#FÓRMULA PARA CALCULAR EL IVA
#
#   IVA=i=1nBI¡*Tg¡
#
#   • "IVA" es el importe total del IVA de una factura.
#   • "BI¡" es la base imponible del concepto número "i" de la factura
#   • "TG¡" es el tipo de gravamen que se aplica al concepto "i" de la factura.
#   • Hay "n" conceptos, cada uno con su base imponible y tipo de gravamen


#Código del programa de la Calculadora IVA
print("Calculadora IVA") #Imprimimos título
amount = float(input("(intoduce) Precio sin IVA: "))
print(f"{amount} €")
tax = float(input("(introduce) Porcenta del IVA"))
print(f"{tax}")
