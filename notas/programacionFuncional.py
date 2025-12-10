
def saluda(nombre): 
    print("Hola, " + nombre + "!")

saluda("Menchu")


def miSuperOperacion(numero):
    return (numero + 2) * 5


nombre = "Felipe" # -> Asigno la variable nombre al valor "Felipe"

miFuncion = saluda # -> Asigno la variable miFuncion a la función saluda
                   #    Aquí no estoy ejecutando la función, solo estoy referenciándola desde otra variable

miFuncion("Federico") # Ejecuto la función a través de la nueva variable

def imprimir_el_doble(numero):
    resultado = numero * 2
    print(resultado)

def imprimir_el_triple(numero):
    resultado = numero * 3
    print(resultado)

def imprimir_la_multiplicacion(numero, multiplicador):
    resultado = numero * multiplicador
    print(resultado)

def imprimir_el_resultado(operacion, numero):
    resultado = operacion(numero)
    print(resultado)

def doblar(numero):
    return numero * 2

def valor_absoluto(numero):
    if numero < 0:
        return -numero
    else:
        return numero

def sumar_tres(numero):
    return numero + 3

imprimir_el_doble(5)
imprimir_el_triple(10)

imprimir_el_resultado(doblar, 7)
imprimir_el_resultado(valor_absoluto, -4)
imprimir_el_resultado(sumar_tres, 10)


imprimir_el_resultado(lambda numero: (numero + 2) * 5, 10)


# En otros lenguajes, tendría esta pinta:    imprimir_el_resultado( numero -> (numero + 2) * 5, 10)

# Cuando una función no quiero reutilizarla
# Y además el tenerla definida de forma tradicional no mejora la legibilidad del código
# Los lenguajes que soportan programaicón funcional ofrecen una nueva forma de definir funciones
# Mediante expresiones lambda

# Una expresion lambda me permite definir una función anónima (sin nombre) dentro de la propia expresión.

# La programación MAP REDUCE hace uso intensivo de funciones lambda para definir operaciones que se aplican a colecciones de datos.