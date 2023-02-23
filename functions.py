#FUNCIONES

def imprimirMensaje():
    print("Python es un lenguaje de progamción.")
    print("Me gusta programar con Python")

def imprimirMensaje2(lenguaje): # Le metemos un parametro
    print(f"{lenguaje} es un lenguaje de progamción.")

def calculo(a): # Le metemos un parametro
    return a + a + a

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# Este es el punto de entrada
if __name__ == '__main__':
    print("Python es un lenguaje de progamción.")
    print("Me gusta programar con Python")

    imprimirMensaje()
    imprimirMensaje()

    x = imprimirMensaje2("Python")
    #imprimirMensaje2("Java")
    print(x)
    y = calculo(5)
    print(y)

    s = sumar(5, 10)
    r = restar(5, 10)
    print(s)
    print(r)

    firstNum = int(input("Introduce el primer número: "))
    secondNum = int(input("Introducir el segundo número: "))
    # suma = sum(firstNum, secondNum)
    print(sumar(firstNum, secondNum))

    firstNum = int(input("Introduce el primer número: "))
    secondNum = int(input("Introduce el segundo número: "))
    print(restar(firstNum, secondNum))

    #
